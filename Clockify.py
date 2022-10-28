from tools import task_list, time_list, number_of_tasks, all_spent_time, task_name, task_date, task_duration

import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()


@app.command(short_help='Show all tasks')
def tasks():
    table = Table(show_header=True, header_style='bold white')
    table.add_column('№', style='bold white')
    table.add_column('Task', style='bold white')

    for i in range(0, number_of_tasks):
        table.add_row(str(i + 1), task_list[i])
        table.add_row()

    console.print(table)


@app.command(short_help='Show all tasks and time spent')
def task_time():
    table = Table(show_header=True, header_style='bold white')
    table.add_column('№', style='bold white')
    table.add_column('Task', style='bold white')
    table.add_column('Time spent:', justify='right')

    for i in range(0, number_of_tasks):
        table.add_row(str(i + 1), task_list[i], time_list[i])
        table.add_row()

    console.print(table)


@app.command(short_help='Show spent time for all tasks')
def spent_time():
    table = Table(show_header=True, header_style='bold white')
    table.add_column('Number of tasks', style='bold white')
    table.add_column('Time spent:', justify='right')

    table.add_row(str(number_of_tasks), all_spent_time)

    console.print(table)


@app.command(short_help='Show spent time for all tasks')
def log():
    table = Table(show_header=True, header_style='bold white')
    table.add_column('Number of log', style='bold white')
    table.add_column('Task', style='bold white')
    table.add_column('Time spent:')
    table.add_column('Date and time:')

    for i in range(0, len(task_name)):
        table.add_row(str(i + 1), task_name[i], task_duration[i], task_date[i])
        table.add_row()

    console.print(table)


if __name__ == '__main__':
    app()
