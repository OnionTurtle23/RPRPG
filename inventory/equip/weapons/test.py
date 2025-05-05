import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


    

def whats_in_my_base():
    print(BASE_DIR)

    for p in BASE_DIR.iterdir():
        print(p)



