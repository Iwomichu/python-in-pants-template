import typer

app = typer.Typer()


@app.command()
def main() -> None:
    print("Hello, World!")


@app.command()
def info() -> None:
    print("Made with love")


if __name__ == '__main__':
    app()
