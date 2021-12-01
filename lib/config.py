import os
import sys
from pathlib import Path

try:
    DIR = Path(os.environ["SS_DIR"])
except KeyError as e:
    print("ERROR: $SS_DIR not set")
    sys.exit(1)
