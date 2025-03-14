from pathlib import Path
import os

path = Path(input("enter path of ur file: "))

if os.path.exists(path) and os.access(path, os.W_OK) and os.access(path, os.R_OK):
    os.remove(path)
else:
    print("u dont have access or this file doesnt exist")


