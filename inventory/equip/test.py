import runpy
from pathlib import Path

path = str(Path(__file__).parent.parent.parent + "testmain.py")

print(path)
runpy.run_path(path)
