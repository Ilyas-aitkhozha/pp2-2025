import os
from pathlib import Path

path = Path(input("enter a path: "))

if path.exists():
    print(f"name of the file: {path.name}\n")
    print(f"name of the portion directory: {path.parent}")
else:
    print("path doesnt exist")