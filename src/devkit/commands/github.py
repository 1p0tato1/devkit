import typer
from rich.console import Console
from rich.table import Table
from devkit.utils.gh import gh_json

app = typer.Typer()
console = Console()

@app.command()
def issues(
    repo: str = typer.Option('', help='owner/repo (par défaut: repo actuel)'),
    limit: int = typer.Option(15, help='Nombre max d\'issues'),
):
    """Liste les issues ouvertes dans un beau tableau."""
    args = ['issue', 'list', '--json', 'number,title,state,labels', '--limit', str(limit)]
    if repo:
        args += ['--repo', repo]
    
    try:
        data = gh_json(*args)
        
        table = Table(title="Issues Ouvertes", border_style="green")
        table.add_column("#", style="cyan", width=6)
        table.add_column("Titre", min_width=30)
        table.add_column("Labels", width=20)

        for issue in data:
            labels = ", ".join(l['name'] for l in issue.get('labels', []))
            table.add_row(str(issue['number']), issue['title'], labels or "—")
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]Erreur lors de la récupération des issues : {e}[/red]")
# ... garde le code précédent et ajoute ceci :

@app.command()
def pr_summary(number: int):
    """Affiche un résumé d'une Pull Request (Titre, corps et fichiers modifiés)."""
    try:
        # On récupère les infos de base
        pr = gh_json('pr', 'view', str(number), '--json', 'title,body,files')
        
        console.rule(f"[bold]PR #{number} : {pr['title']}[/bold]")
        console.print(f"\n[italic]{pr['body'] or 'Pas de description.'}[/italic]\n")
        
        table = Table(title="Fichiers modifiés", border_style="yellow")
        table.add_column("Fichier")
        for f in pr.get('files', []):
            table.add_row(f['path'])
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]PR introuvable ou erreur : {e}[/red]")

@app.command()
def run_status():
    """Affiche le statut des derniers lancements CI/CD (GitHub Actions)."""
    try:
        runs = gh_json('run', 'list', '--limit', '5', '--json', 'displayTitle,status,conclusion,headBranch')
        
        table = Table(title="Derniers Runs CI/CD", border_style="blue")
        table.add_column("Workflow")
        table.add_column("Branche", style="cyan")
        table.add_column("Statut")

        for r in runs:
            color = "green" if r['conclusion'] == "success" else "red" if r['conclusion'] == "failure" else "yellow"
            status = f"[{color}]{r['conclusion'] or r['status']}[/{color}]"
            table.add_row(r['displayTitle'], r['headBranch'], status)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]Erreur Actions : {e}[/red]")
