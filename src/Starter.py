from time import sleep
from rich.console import Console

console = Console()
tasks = [f"Successfully launched! " for _ in range(1, 2)]  # Fixed the list comprehension

with console.status("[bold green]Launching DDos, please wait a few seconds...[/bold green]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(5)
        console.log(f"{task} DDOS")
