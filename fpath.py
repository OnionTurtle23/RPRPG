import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import inventory.equip.unique.unique as uniquemodule
import inventory.equip.equip as equipmodule
from inventory.equip.weapons.weapon import Weapon
from inventory.equip.armor.armor import Armor
from inventory.equip.unique.unique import Unique
import json
import runpy
from pathlib import Path

armormodule.aManager.aEquip("Basic Buckler", "Kris")
weaponmodule.wManager.unlock_weapon("Fiery Scimitar")
weaponmodule.wManager.wEquip("Fiery Scimitar")
uniquemodule.uManager.uEquip("Compact Cell", "Kris")
equipmodule.eManager.kEquip()

#armormodule.aManager.aEquip("Basic Leather", "Abigail")
