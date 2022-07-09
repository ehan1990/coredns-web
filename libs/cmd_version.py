import click
from libs.constants import VERSION


@click.command(name="version")
def version_cmd():
    print(f"CLI Version: {VERSION}")
