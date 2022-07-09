import click
import json
from libs import cmd_helper
from libs.constants import HTTP
from libs import table


@click.group(name="record")
def record_cmd():
    pass


@record_cmd.command(name="add")
@click.option('--rname', required=True)
@click.option('--zname', required=True)
@click.option('--rval', required=True)
@click.option('--rtype', required=True)
@click.option('--owner', default="shield-prod", required=True)
@click.option('--ttl', default=60)
def add_record(rname, zname, rval, rtype, owner, ttl):
    data = {
        "rname": rname,
        "zname": zname,
        "rval": rval,
        "rtype": rtype,
        "ttl": ttl,
        "owner": owner
    }
    try:
        res = cmd_helper.call_api("records", HTTP.POST, json.dumps(data))
        if res.status_code == 200:
            print(f"added record {rname}")
            return
        print(res.content)
    except Exception as e:
        print(f"unable to add record {rname}, {e}")


@record_cmd.command(name="ls")
def list_records():
    try:
        res = cmd_helper.call_api("records", HTTP.GET)
        if res.status_code == 200:
            cols = ["[bold cyan]rname", "[bold cyan]zname", "[bold cyan]rtype", "[bold cyan]rval", "[bold cyan]ttl", "[bold cyan]owner"]
            rows = []

            data = res.json()
            for d in data:
                rows.append([d["record_name"], d["zone_name"], d["record_type"], d["record_value"], str(d["ttl"]), d["owner"]])
            table.print_table(cols, rows)
            return
        print(res.content)
    except Exception as e:
        print(f"unable to retrieve records, {e}")
