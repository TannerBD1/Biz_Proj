# Highlight if Error Predicted
from rich.console import Console
#   Title
print(f'Highlight if Error Predicted\n')
#   Variables
correct_count = int(input('Enter a Number(right); '))
correct_item = input('Enter an item; ')
incorrect_count = int(input('Enter a Number(wrong); '))
incorrect_item = input('Enter an item; ')

#   Init Console
console = Console()
console.print(f"Ordering [bold green]{correct_count}[/bold green]; {correct_item}!")

console = Console()
console.print(f"Ordering [bold red]{incorrect_count}[/bold red]; {incorrect_item}!")
