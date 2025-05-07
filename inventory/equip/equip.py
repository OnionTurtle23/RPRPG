import json
from pathlib import Path
from uuid import uuid4


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class EquipWeapon:

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

"""
def whats_in_my_base():
    print(BASE_DIR)

    for p in BASE_DIR.iterdir():
        print(p)



"""
