from rich.console import Console
from rich.table import Table


def print_table(cols, rows):
    t = Table()
    for col in cols:
        t.add_column(col, no_wrap=True)

    for row in rows:
        t.add_row(*row)

    c = Console()
    c.print(t)
