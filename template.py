import os
from pathlib import Path

list_of_files = [
    "rufus/__init__.py",
    "rufus/client.py",
    "rufus/scraper.py",
    "rufus/synthesizer.py",
    "rufus/api.py",
    "rufus/utils.py",
    "examples/example_usage.py",
    "tests/test_scraper.py",
    "tests/test_synthesizer.py",
    "requirements.txt",
    "setup.py"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file