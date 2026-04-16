import typer
from devkit.commands import github, ai

app = typer.Typer(name="devkit")

app.add_typer(github.app, name="gh")
app.add_typer(ai.app, name="ai")

if __name__ == "__main__":
    app()
