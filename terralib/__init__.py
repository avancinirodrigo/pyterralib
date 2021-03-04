import os
import sys
from pathlib import Path

if sys.platform == 'linux':
	os.environ['LD_LIBRARY_PATH'] = str(Path(__file__).parent.absolute())
