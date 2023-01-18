import click

from app import app
from app.init_db import init_db


@click.command()
def run():
    app.run(host='127.0.0.1', port=3000, debug=True)

@click.command()
def db():
    init_db()

@click.group()
def cli():
    pass

cli.add_command(run)
cli.add_command(db)

if __name__ == '__main__':
    cli()
