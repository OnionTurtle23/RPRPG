import json
import os
from uuid import uuid4
from pathlib import Path

class Weapon:
    def __init__(self, wname, wtype, slots, slot_link, damage, is_unique, is_avail=False):
        self.id = str(uuid4())  # Unique identifier for each weapon
        self.wname = wname
        self.wtype = wtype
        self.slots = slots
        self.slot_link = slot_link
        self.damage = damage
        self.is_unique = is_unique  # Character who can use the weapon
        self.is_avail = is_avail    # Whether the weapon is unlocked

    def to_dict(self):
        """Convert Weapon object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "wname": self.wname,
            "wtype": self.wtype,
            "slots": self.slots,
            "slot_link": self.slot_link,
            "damage": self.damage,
            "is_unique": self.is_unique,
            "is_avail": self.is_avail
        }

    @classmethod
    def from_dict(cls, data):
        """Create Weapon object from dictionary."""
        return cls(
            data["wname"],
            data["wtype"],
            data["slots"],
            data["slot_link"],
            data["damage"],
            data["is_unique"],
            data["is_avail"]
        )

    def display(self):
        """Display weapon details."""
        print(f"Name: {self.wname}")
        print(f"Type: {self.wtype}")
        print(f"Slots: {self.slots}")
        print(f"Slot Link: {self.slot_link}")
        print(f"Damage: {self.damage}")
        print(f"Who Uses: {self.is_unique}")
        print(f"Unlocked: {self.is_avail}")

class WeaponManager:
    def __init__(self, filename="inventory/equip/weapons/weaponlist.json"):
        self.filename = filename
        self.weapons = []
        self.inventory = []
        self.load_weapons()

    def load_weapons(self):
        """Load weapons from JSON file."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.weapons = [Weapon.from_dict(weapon) for weapon in data]
                self.inventory = [weapon for weapon in self.weapons if weapon.is_avail]
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.weapons = []
            self.inventory = []

    def save_weapons(self):
        """Save weapons to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([weapon.to_dict() for weapon in self.weapons], file, indent=4)

    def add_weapon(self, wname, wtype, slots, slot_link, damage, is_unique, is_avail=False):
        """Add a new weapon and save to file."""
        weapon = Weapon(wname, wtype, slots, slot_link, damage, is_unique, is_avail)
        self.weapons.append(weapon)
        if is_avail:
            self.inventory.append(weapon)
        self.save_weapons()
        print(f"Added {wname} to weapons list.")
        return weapon

    def unlock_weapon(self, weapon_name):
        """Unlock a weapon and add to inventory."""
        for weapon in self.weapons:
            if weapon.wname.lower() == weapon_name.lower():
                if weapon.is_avail:
                    print(f"{weapon_name} is already unlocked.")
                else:
                    weapon.is_avail = True
                    self.inventory.append(weapon)
                    self.save_weapons()
                    print(f"Unlocked {weapon_name} and added to inventory.")
                return
        print(f"Weapon {weapon_name} not found.")

    def display_inventory(self):
        """Display all weapons in inventory."""
        if not self.inventory:
            print("Your inventory is sadly empty... go get stuff!")
        else:
            print("Your inventory:")
            for weapon in self.inventory:
                print(f"- {weapon.wname} (For: {weapon.is_unique}, Type: {weapon.wtype}, Damage: {weapon.damage}, Slots/Linked: {weapon.slots}/{weapon.slot_link})")

    def search_weapons(self, key, value):
        """Search for weapons by key-value pair."""
        for weapon in self.weapons:
            return [weapon for weapon in self.weapons if hasattr(weapon, key) and getattr(weapon, key) == value and weapon.is_avail]

    def wEquip(self, weapon_name):
        ePath = Path(__file__).parent.parent
        eFilepath = str(ePath) + "/equiplist.json"
        self.eFilename = eFilepath
        for weapon in self.inventory:
            if weapon.wname.lower() == weapon_name.lower():
                print(f"Equipped {weapon.wname}")
                with open(self.eFilename, "w") as file:
                    json.dump([weapon.to_dict()], file, indent=4)

# Example usage

wtype = {
    "Normal": "None",
    "Superheated": "Fire",
    "Precipitative": "Water",
    "Discharging": "Electric",
    "Frostbitten": "Ice",
    "Jet Turbined": "Wind",
    "Seismic": "Rock",
    "Ancient": "Holy"
    }

    # Initialize wManager
wManager = WeaponManager()

    # Add initial weapons
all_weapons = [
    ("Basic Sword", "Normal", 3, 1, 20, "Kris"),
    ("Basic Staff", "Normal", 4, 2, 10, "Abigail"),
    ("Basic Pistol", "Normal", 2, 1, 25, "Monte"),
    ("Fiery Scimitar", "Superheated", 4, 2, 35, "Kris"),
    ("Rain Stick", "Precipitative", 5, 2, 25, "Abigail"),
    ("Electro Rifle", "Discharging", 3, 1, 40, "Monte"),
    ("Masamune", "Frostbitten", 5, 2, 60, "Kris"),
    ("Hurricane Staff", "Jet Turbined", 7, 3, 45, "Abigail"),
    ("Heavy Shotgun", "Seismic", 5, 2, 70, "Monte"),
    ("Archangel Blade", "Ancient", 8, 4, 100, "Kris"),
    ("Staff of the Prophets", "Ancient", 8, 4, 100, "Abigail"),
    ("Judgement Day", "Ancient", 8, 4, 100, "Monte")
    ]

    # Add weapons if file is empty
if not wManager.weapons:
    for weapon in all_weapons:
        wManager.add_weapon(*weapon)
"""
    # Unlock some weapons
wManager.unlock_weapon("Basic Sword")
wManager.unlock_weapon("Fiery Scimitar")
wManager.unlock_weapon("Electro Rifle")
wManager.unlock_weapon("Basic Staff")

    # Display inventory
wManager.display_inventory()

    # Search for weapons by type
print("\nSearching for Superheated weapons:")
superheated_weapons = wManager.search_weapons("wtype", "Superheated")
for weapon in superheated_weapons:
    weapon.display()

    # Search for weapons by character
print("\nSearching for Kris's weapons:")
kris_weapons = wManager.search_weapons("is_unique", "Kris")
for weapon in kris_weapons:
    weapon.display()

"""
