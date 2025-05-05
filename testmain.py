from pathlib import Path
import importlib.util
import sys


def wImport(wmodPath):

    mod_file_name = wmodPath.stem
    wSpec = importlib.util.spec_from_file_location(mod_file_name, str(wmodPath))
    if wSpec is None:
        print(f"Could not find module at: {wmodPath}")
        return None
    module = importlib.util.module_from_spec(wSpec)
    sys.modules[mod_file_name] = module
    try:
        wSpec.loader.exec_module(module)
    except Exception as e:
        print(f"Error during module execution: {e}")
        del sys.modules[mod_file_name]
        return None
    return module

wmodPath = Path("inventory/equip/weapons/weapon1.py").expanduser()

my_module = wImport(wmodPath)


my_module.manager.unlock_weapon("Basic Sword")
my_module.manager.display_inventory()
