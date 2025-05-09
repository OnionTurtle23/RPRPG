import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import inventory.equip.unique.unique as uniquemodule
import inventory.equip.equip as equipmodule
import party.char as charmodule
from inventory.equip.weapons.weapon import Weapon
from inventory.equip.armor.armor import Armor
from inventory.equip.unique.unique import Unique
from enemies.enemy import Enemy, Enemy_chief, Beast
from party.char import PlayableCharacter
import json
import runpy
from pathlib import Path

def generate_encounter():
    import enemies.enemy as basics
    basics.eManager.randEnc()


"""
armormodule.aManager.aEquip("Basic Buckler", "Kris")
weaponmodule.wManager.unlock_weapon("Fiery Scimitar")
weaponmodule.wManager.wEquip("Fiery Scimitar")
uniquemodule.uManager.uEquip("Compact Cell", "Kris")
equipmodule.eManager.kEquip()

#armormodule.aManager.aEquip("Basi Leather", "Abigail")
"""

charmodule.cManager.load_chars()
#charmodule.PlayableCharacter.kris.display_char()
charmodule.cManager.save_party()
