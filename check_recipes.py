import glob
from pathlib import Path
import re
import sys

ingredients_re = re.compile(r"^\s*#+\s+ingredients?\s*$", re.IGNORECASE | re.MULTILINE)
instructions_re = re.compile(r"^\s*#+\s+instructions?\s*$", re.IGNORECASE | re.MULTILINE)

paths = Path(__file__).parent.glob("*/*.md")
errors = 0
for path in paths:
    text = path.read_text()
    if not ingredients_re.search(text):
        print(f'File {path} is missing a section: "## Ingredients" (or similar)')
        errors += 1
    if not instructions_re.search(text):
        print(f'File {path} is missing a section: "## Instructions" (or similar)')
        errors += 1

if errors:
    sys.exit(1)
