import click


@click.command()
@click.argument('username')
def main(username):
    print(f"hello {username}")


if __name__ == "__main__":
    main()
