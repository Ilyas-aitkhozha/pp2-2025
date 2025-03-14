from pathlib import Path

path = Path(input("enter your path: "))

directories = []
all = list(path.iterdir())
for item in all:
    if item.is_dir():
        directories.append(item)
files = []
for item in all:
    if item.is_file():
        files.append(item)
print(f"directories: \n {directories} \n files: \n {files}")


