#!/usr/bin/env python
import click
from libs.cmd_healthcheck import healthcheck_cmd
from libs.cmd_record import record_cmd
from libs.cmd_zone import zone_cmd
from libs.cmd_version import version_cmd


@click.group()
def cli():
    pass


cli.add_command(healthcheck_cmd)
cli.add_command(record_cmd)
cli.add_command(version_cmd)
cli.add_command(zone_cmd)


if __name__ == "__main__":
    cli()
