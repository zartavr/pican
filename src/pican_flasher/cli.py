import click


@click.command()
@click.option('--username', default="", type=str)
def cli(username):
    print(f"hello {username}")