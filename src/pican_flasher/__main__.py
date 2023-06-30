import click
import sys


@click.command()
@click.option('--username', default="", type=str)
def cli(username):
    print(f"hello {username}")

if __name__ == "__main__":
    cli()
