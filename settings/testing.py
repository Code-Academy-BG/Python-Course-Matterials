import os
from pathlib import Path

BASE_DIR = Path(os.path.abspath(__file__)).parent.parent

INPUT_DIR = os.path.join(BASE_DIR, 'test_files', 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'test_files', 'output')
