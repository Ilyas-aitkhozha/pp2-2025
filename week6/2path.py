from pathlib import Path
import os

path = Path(input("enter ur path: "))

if path.exists():
    path_str = str(path)
    if os.access(path_str, os.R_OK):
        print("Reading is working good\n")
    else: 
        print("Reading is working not good")
    if os.access(path_str, os.W_OK):
        print("Writing is working good\n")
    else: 
        print("Writing is working not good\n")
    if os.access(path_str, os.X_OK):
        print("Existence is working good\n")
    else: 
        print("Existence is working not good")
else:
    print("cannot test anything because path doesnt exist")

