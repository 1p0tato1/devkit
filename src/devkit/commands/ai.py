import typer
import subprocess
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from devkit.utils.gh import gh, gh_json

app = typer.Typer()
console = Console()

# --- STEP 7: Integrating Copilot CLI ---

@app.command()
def explain(command: str = typer.Argument(..., help='Shell command to explain')):
    """Ask Copilot CLI to explain a shell command."""
    # On utilise la syntaxe suggérée par ton erreur : gh copilot -p "explain ..."
    full_cmd = f'gh copilot -p "explain {command}"'
    
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True, 
        text=True
    )
    
    output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
    console.print(Panel(output, title='[purple]Copilot Explanation[/purple]', border_style="purple"))

@app.command()
def suggest(task: str = typer.Argument(..., help='Task to accomplish')):
    """Ask Copilot CLI to suggest a command."""
    # Même logique pour suggest
    full_cmd = f'gh copilot -p "suggest {task}"'
    
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True, 
        text=True
    )
    
    output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
    console.print(Panel(output, title='[purple]Copilot Suggestion[/purple]', border_style="purple"))


# --- STEP 8: The AI Review Pipeline ---

@app.command()
def review(
    pr_number: int = typer.Argument(..., help='PR number to review'),
    model: str = typer.Option('gemini', help='AI tool: gemini or claude'),
):
    """AI-powered code review of a pull request."""
    with Progress(SpinnerColumn(), TextColumn('{task.description}')) as progress:
        t = progress.add_task('Fetching PR diff...')
        try:
            diff = gh('pr', 'diff', str(pr_number))
            progress.update(t, description=f'Running {model} review...')
            
            if model == 'gemini':
                # Appelle ton simulateur /usr/local/bin/gemini
                result = subprocess.run(['gemini', f'Review: {diff[:2000]}'], capture_output=True, text=True)
            else:
                result = subprocess.run(['claude', '--no-interactive', f'Review: {diff[:2000]}'], capture_output=True, text=True)
            
            output = result.stdout.strip() if result.stdout.strip() else "No feedback received."
            console.print(Panel(output, title=f'[cyan]AI Review — PR #{pr_number}[/cyan]', border_style="cyan"))
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


# --- STEP 9: Smart Commit Message Generator ---

@app.command()
def commit():
    """Generate a commit message from staged changes using AI."""
    try:
        diff = subprocess.check_output(['git', 'diff', '--staged'], text=True)
        if not diff.strip():
            console.print('[yellow]No staged changes. Use "git add" first.[/yellow]')
            return

        with console.status("[bold green]Generating commit message...[/bold green]"):
            result = subprocess.run(['claude', '--no-interactive', 'Generate commit message'], capture_output=True, text=True)
            suggested = result.stdout.strip()

        console.print(Panel(suggested, title='[green]Suggested Commit Message[/green]'))
        
        if Confirm.ask('Use this message?'):
            subprocess.run(['git', 'commit', '-m', suggested])
            console.print("[bold green]✓ Committed![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
