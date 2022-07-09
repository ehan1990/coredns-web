import click
import json
from libs import cmd_helper
from libs.constants import HTTP
from libs import table


@click.group(name="zone")
def zone_cmd():
    pass


@zone_cmd.command(name="add")
@click.option('--name', required=True)
@click.option('--owner', default="shield-prod", required=True)
def add_zone(name, owner):
    data = {
        "name": name,
        "owner": owner
    }
    try:
        res = cmd_helper.call_api("zones", HTTP.POST, json.dumps(data))
        if res.status_code == 200:
            print(f"added zone {name}")
            return
        print(res.content)
    except Exception as e:
        print(f"unable to add zone {name}, {e}")


@zone_cmd.command(name="delete")
@click.option('--name', required=True)
def delete_zone(name):
    try:
        res = cmd_helper.call_api(f"zones/{name}", HTTP.DELETE)
        if res.status_code == 200:
            print(f"deleted zone {name}")
            return
    except Exception as e:
        print(f"unable to delete zone {name}, {e}")


@zone_cmd.command(name="ls")
def list_zones():
    try:
        res = cmd_helper.call_api("zones", HTTP.GET)
        if res.status_code == 200:
            cols = ["[bold cyan]Zone Name", "[bold cyan]Owner"]
            rows = []

            data = res.json()
            for d in data:
                rows.append([d["zone_name"], d["owner"]])
            table.print_table(cols, rows)
            return
        print(res.content)
    except Exception as e:
        print(f"unable to retrieve zones, {e}")


@zone_cmd.command(name="show")
@click.option('--name', required=True)
def get_one_zone(name):
    try:
        res = cmd_helper.call_api(f"zones/{name}", HTTP.GET)
        if res.status_code == 200:
            cols = ["[bold cyan]Key", "[bold cyan]Value"]
            rows = []

            data = res.json()
            rows.append(["Zone Name", data["zone_name"]])
            rows.append(["Owner", data["owner"]])
            table.print_table(cols, rows)
            return
        print(res.content)
    except Exception as e:
        print(f"unable to retrieve zone, {e}")


@zone_cmd.command(name="update")
@click.option('--name', required=True)
@click.option('--owner', required=True)
def update_one_zone(name, owner):
    try:
        data = {"owner": owner}
        res = cmd_helper.call_api(f"zones/{name}", HTTP.PUT, json.dumps(data))
        if res.status_code == 200:
            print(f"updated {name}'s owner to {owner}")
            return
    except Exception as e:
        print(f"unable to update zone, {e}")
