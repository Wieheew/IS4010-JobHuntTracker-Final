import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from src import storage  # Imports our storage.py module

# Initialize Typer app and Rich console
app = typer.Typer()
console = Console()

@app.command()
def add(company: str, role: str, link: str = ""):
    """
    Add a new job application.
    Usage: python src/main.py add "Google" "Senior Dev"
    """
    job = storage.add_job(company, role, link)
    console.print(f"[bold green]Success![/bold green] Added {company} ({role}) to your tracker.")

@app.command()
def list(status: Optional[str] = None):
    """
    List all job applications.
    Usage: python src/main.py list
    """
    jobs = storage.load_jobs()
    
    if not jobs:
        console.print("[yellow]No jobs found. Use 'add' to get started![/yellow]")
        return

    # Create a nice looking table
    table = Table(title="My Job Applications")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Company", style="magenta")
    table.add_column("Role", style="white")
    table.add_column("Status", style="green")
    table.add_column("Date Applied", style="blue")

    # Filter and add rows
    for job in jobs:
        if status and job["status"].lower() != status.lower():
            continue
            
        # Color code the status
        status_str = job["status"]
        if status_str == "Rejected":
            status_str = f"[red]{status_str}[/red]"
        elif status_str == "Interviewing":
            status_str = f"[bold yellow]{status_str}[/bold yellow]"

        table.add_row(
            str(job["id"]), 
            job["company"], 
            job["role"], 
            status_str, 
            job["date_applied"]
        )

    console.print(table)

@app.command()
def update(job_id: int, status: str):
    """
    Update the status of a job application.
    Usage: python src/main.py update 1 "Interviewing"
    """
    updated_job = storage.update_job_status(job_id, status)
    
    if updated_job:
        console.print(f"[green]Updated Job #{job_id} status to '{status}'[/green]")
    else:
        console.print(f"[red]Error: Job #{job_id} not found.[/red]")

if __name__ == "__main__":
    app()