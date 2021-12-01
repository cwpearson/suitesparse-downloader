import os
import sys
from pathlib import Path

from lib import matrix

try:
    DIR = Path(os.environ["SS_DIR"])
except KeyError as e:
    print("ERROR: $SS_DIR not set")
    sys.exit(1)

SS_ROOT_URL = "https://sparse.tamu.edu"



