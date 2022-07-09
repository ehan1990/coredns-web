import click
import json
from libs import cmd_helper


@click.command(name="healthcheck")
def healthcheck_cmd():
    res = cmd_helper.call_api("/healthcheck")
    if res.status_code == 200:
        print(json.dumps(res.json(), indent=2))
    else:
        print("api server is offline")
