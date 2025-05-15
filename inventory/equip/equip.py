import json
from pathlib import Path
from uuid import uuid4
import os
import inventory.equip.weapons.weapon as weaponmanager
import inventory.equip.armor.armor as armormanager
import inventory.equip.unique.unique as uniquemanager
from inventory.equip.weapons.weapon import Weapon
from inventory.equip.armor.armor import Armor
from inventory.equip.unique.unique import Unique


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class EquipmentManager:
    def __init__(self):
        self.weapons = []
        self.armor = []
        self.unique = []
        self.inventory = []
        #self.load_weapons()

    def kEquip(self, filename = "inventory/equip/kEquip.json"):
        self.filename = filename
        self.kweapon = []
        self.karmor = []
        self.kunique = []
        self.kequip = []
        self.load_kris()
        self.save_kris()

    def aEquip(self, filename = "inventory/equip/aEquip.json"):
        self.filename = filename
        self.aweapon = []
        self.aarmor = []
        self.aunique = []
        self.aequip = []
        self.load_abigail()
        self.save_abigail()


    def mEquip(self, filename = "inventory/equip/mEquip.json"):
        self.filename = filename
        self.mweapon = []
        self.marmor = []
        self.munique = []
        self.mequip = []
        self.load_monte()
        self.save_monte()


    def load_kris(self, kw = "inventory/equip/weapons/Krisweapon.json", ka = "inventory/equip/armor/Krisarmor.json", ku = "inventory/equip/unique/Krisunique.json", ke = "inventory/equip/kEquip.json"):
        """Load weapons from JSON file."""
        self.kw = kw
        self.ka = ka
        self.ku = ku
        self.ke = ke
        if not (os.path.exists(self.kw) or os.path.exists(self.ka) or os.path.exists(self.ku)):
            return
        try:
            with open(self.kw, 'r') as file:
                wdata = json.load(file)
                self.kweapon = [Weapon.from_dict(weapon) for weapon in wdata]
            with open(self.ka, 'r') as file:
                adata = json.load(file)
                self.karmor = [Armor.from_dict(armor) for armor in adata]
            with open(self.ku, 'r') as file:
                udata = json.load(file)
                self.kunique = [Unique.from_dict(unique) for unique in udata]
            self.kequip = ([weapon.to_dict() for weapon in self.kweapon],[armor.to_dict() for armor in  self.karmor],[unique.to_dict() for unique in self.kunique])
            return self.kequip

        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.weapons = []
            self.inventory = []

    def save_kris(self, filename = "inventory/equip/kEquip.json"):
        with open(self.filename, 'w') as file:
            json.dump(self.kequip, file, indent=4)

    def load_abigail(self, aw = "inventory/equip/weapons/Abigailweapon.json", aa = "inventory/equip/armor/Abigailarmor.json", au = "inventory/equip/unique/Abigailunique.json", ae = "inventory/equip/aEquip.json"):
        """Load weapons from JSON file."""
        self.aw = aw
        self.aa = aa
        self.au = au
        self.ae = ae
        if not (os.path.exists(self.aw) or os.path.exists(self.aa) or os.path.exists(self.au)):
            return
        try:
            with open(self.aw, 'r') as file:
                wdata = json.load(file)
                self.aweapon = [Weapon.from_dict(weapon) for weapon in wdata]
            with open(self.aa, 'r') as file:
                adata = json.load(file)
                self.aarmor = [Armor.from_dict(armor) for armor in adata]
            with open(self.au, 'r') as file:
                udata = json.load(file)
                self.aunique = [Unique.from_dict(unique) for unique in udata]
            self.aequip = ([weapon.to_dict() for weapon in self.aweapon],[armor.to_dict() for armor in  self.aarmor],[unique.to_dict() for unique in self.aunique])
            return self.aequip

        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.weapons = []
            self.inventory = []

    def save_abigail(self, filename = "inventory/equip/aEquip.json"):
        with open(self.filename, 'w') as file:
            json.dump(self.aequip, file, indent=4)

    def load_monte(self, mw = "inventory/equip/weapons/Monteweapon.json", ma = "inventory/equip/armor/Montearmor.json", mu = "inventory/equip/unique/Monteunique.json", me = "inventory/equip/mEquip.json"):
        """Load weapons from JSON file."""
        self.mw = mw
        self.ma = ma
        self.mu = mu
        self.me = me
        if not (os.path.exists(self.mw) or os.path.exists(self.ma) or os.path.exists(self.mu)):
            return
        try:
            with open(self.mw, 'r') as file:
                wdata = json.load(file)
                self.mweapon = [Weapon.from_dict(weapon) for weapon in wdata]
            with open(self.ma, 'r') as file:
                adata = json.load(file)
                self.marmor = [Armor.from_dict(armor) for armor in adata]
            with open(self.mu, 'r') as file:
                udata = json.load(file)
                self.munique = [Unique.from_dict(unique) for unique in udata]
            self.mequip = ([weapon.to_dict() for weapon in self.mweapon],[armor.to_dict() for armor in  self.marmor],[unique.to_dict() for unique in self.munique])
            return self.mequip

        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.weapons = []
            self.inventory = []

    def save_monte(self, filename = "inventory/equip/mEquip.json"):
        with open(self.filename, 'w') as file:
            json.dump(self.mequip, file, indent=4)



eManager = EquipmentManager()

eManager.kEquip()
eManager.aEquip()
eManager.mEquip()

