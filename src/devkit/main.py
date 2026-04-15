import typer
from devkit.commands import github

app = typer.Typer(name="devkit", help="Mon assistant de dev IA")

# On ajoute le groupe de commandes 'gh'
app.add_typer(github.app, name="gh")

if __name__ == "__main__":
    app()
