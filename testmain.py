from pathlib import Path
import importlib.util
import sys


def wImport(wmodPath):

    mod_file_name = wmodPath.stem
    wSpec = importlib.util.spec_from_file_location(mod_file_name, str(wmodPath))
    print(wmodPath)
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


def aImport(amodPath):

    mod_file_name = amodPath.stem
    aSpec = importlib.util.spec_from_file_location(mod_file_name, str(amodPath))
    if aSpec is None:
        print(f"Could not find module at: {amodPath}")
        return None
    module = importlib.util.module_from_spec(aSpec)
    sys.modules[mod_file_name] = module
    try:
        aSpec.loader.exec_module(module)
    except Exception as e:
        print(f"Error during module execution: {e}")
        del sys.modules[mod_file_name]
        return None
    return module

def uImport(umodPath):

    mod_file_name = umodPath.stem
    uSpec = importlib.util.spec_from_file_location(mod_file_name, str(umodPath))
    if uSpec is None:
        print(f"Could not find module at: {umodPath}")
        return None
    module = importlib.util.module_from_spec(uSpec)
    sys.modules[mod_file_name] = module
    try:
        uSpec.loader.exec_module(module)
    except Exception as e:
        print(f"Error during module execution: {e}")
        del sys.modules[mod_file_name]
        return None
    return module

umodPath = Path("inventory/equip/unique/unique.py").expanduser()

uniquemodule = uImport(umodPath)


amodPath = Path("inventory/equip/armor/armor.py").expanduser()

armormodule = aImport(amodPath)

wmodPath = Path("inventory/equip/weapons/weapon.py").expanduser()

weaponmodule = wImport(wmodPath)

uniquemodule.uManager.uEquip("Robotic Suit", "Kris")


"""
Testing Functions, etc.
armormodule.aManager.unlock_armor("Basic Buckler")
armormodule.aManager.aEquip("Wooden Shield", "Kris")
armormodule.aManager.aEquip("Basic Buckler", "Monte")

weaponmodule.wManager.unlock_weapon("Basic Staff")
weaponmodule.wManager.wEquip("Basic Sword")
weaponmodule.wManager.wEquip("Basic Staff")
weaponmodule.wManager.wEquip("Basic Pistol")


weaponmodule.wManager.unlock_weapon("Basic Sword")
weaponmodule.wManager.display_inventory()


armormodule.aManager.unlock_armor("Wooden Shield")
armormodule.aManager.display_inventory()

uniquemodule.uManager.unlock_unique("Robotic Suit")
uniquemodule.uManager.display_inventory()

"""
