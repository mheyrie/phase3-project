import click

@click.command()
@click.option('--number', '-n')

def main(number):
    click.echo(f"Your number is {number}")


if __name__=="__main__":
    main()