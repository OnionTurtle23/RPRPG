import json
import os
from uuid import uuid4
from pathlib import Path

class Armor:
    def __init__(self, aname, atype, slots, slot_link, physmit, techmit, is_avail=False):
        self.id = str(uuid4())  # Unique identifier for each armor
        self.aname = aname
        self.atype = atype
        self.slots = slots
        self.slot_link = slot_link
        self.physmit = physmit
        self.techmit = techmit  # Character who can use the armor
        self.is_avail = is_avail    # Whether the armor is unlocked

    def to_dict(self):
        """Convert Armor object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "aname": self.aname,
            "atype": self.atype,
            "slots": self.slots,
            "slot_link": self.slot_link,
            "physmit": self.physmit,
            "techmit": self.techmit,
            "is_avail": self.is_avail
        }

    @classmethod
    def from_dict(cls, data):
        """Create Armor object from dictionary."""
        return cls(
            data["aname"],
            data["atype"],
            data["slots"],
            data["slot_link"],
            data["physmit"],
            data["techmit"],
            data["is_avail"]
        )

    def display(self):
        """Display armor details."""
        print(f"Name: {self.aname}")
        print(f"Type: {self.atype}")
        print(f"Slots: {self.slots}")
        print(f"Slot Link: {self.slot_link}")
        print(f"Physical Mitigation: {self.physmit}")
        print(f"Tech Mitigation: {self.techmit}")
        print(f"Unlocked: {self.is_avail}")

class ArmorManager:
    def __init__(self, filename="inventory/equip/armor/armorlist.json"):
        self.filename = filename
        self.armor = []
        self.inventory = []
        self.load_armor()

    def load_armor(self):
        """Load armor from JSON file."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.armor = [Armor.from_dict(armor) for armor in data]
                self.inventory = [armor for armor in self.armor if armor.is_avail]
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.armor = []
            self.inventory = []

    def save_armors(self):
        """Save armors to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([armor.to_dict() for armor in self.armor], file, indent=4)

    def add_armor(self, aname, atype, slots, slot_link, physmit, techmit, is_avail=False):
        """Add a new armor and save to file."""
        armor = Armor(aname, atype, slots, slot_link, physmit, techmit, is_avail)
        self.armor.append(armor)
        if is_avail:
            self.inventory.append(armor)
        self.save_armors()
        print(f"Added {aname} to armors list.")
        return armor

    def unlock_armor(self, armor_name):
        """Unlock a armor and add to inventory."""
        for armor in self.armor:
            if armor.aname.lower() == armor_name.lower():
                if armor.is_avail:
                    print(f"{armor_name} is already unlocked.")
                else:
                    armor.is_avail = True
                    self.inventory.append(armor)
                    self.save_armors()
                    print(f"Unlocked {armor_name} and added to inventory.")
                return
        print(f"Armor {armor_name} not found.")

    def display_inventory(self):
        """Display all armors in inventory."""
        if not self.inventory:
            print("Your inventory is sadly empty... go get stuff!")
        else:
            print("Your inventory:")
            for armor in self.inventory:
                print(f"- {armor.aname} (Type: {armor.atype}, Phys Def: {armor.physmit}, Tech Def: {armor.techmit} Slots/Linked: {armor.slots}/{armor.slot_link})")

    def search_armors(self, key, value):
        """Search for armors by key-value pair."""
        for armor in self.armor:
            return [armor for armor in self.armor if hasattr(armor, key) and getattr(armor, key) == value and armor.is_avail]


    def aEquip(self, armor_name, equip_on):
        for armor in self.inventory:
            if armor.aname.lower() == armor_name.lower():
                print(f"Equipped {armor.aname}")
                if equip_on == "Kris":
                    kFilepath = "inventory/equip/armor/Krisarmor.json"
                    self.kFilename = kFilepath
                    with open(self.kFilename, "w") as file:
                        json.dump([armor.to_dict()], file, indent=4)
                elif equip_on == "Abigail":
                    aFilepath = "inventory/equip/armor/Abigailarmor.json"
                    self.aFilename = aFilepath
                    with open(self.aFilename, "w") as file:
                        json.dump([armor.to_dict()], file, indent=4)
                elif equip_on == "Monte":
                    mFilepath = "inventory/equip/armor/Montearmor.json"
                    self.mFilename = mFilepath
                    with open(self.mFilename, "w") as file:
                        json.dump([armor.to_dict()], file, indent=4)
                else:
                    break

atype = {
    "Normal": "None",
    "Flame-Retardant": "Fire",
    "Water-Tight": "Water",
    "Grounded": "Electric",
    "Fur-Lined": "Ice",
    "Wind Resistive": "Wind",
    "Ancient": "Holy"
    }

    # Initialize aManager
aManager = ArmorManager()

    # Add initial armors
all_armors = [
    ("Wooden Shield", "Normal", 2, 1, 20, 10),
    ("Basic Leather", "Normal", 3, 1, 10, 15),
    ("Basic Buckler", "Normal", 2, 1, 20, 20),
    ("Racing Suit", "Flame-Retardant", 4, 2, 30, 30),
    ("Wet Suit", "Water-Tight", 5, 2, 30, 30),
    ("Rubber Suit", "Grounded", 3, 1, 30, 30),
    ("Snow Suit", "Fur-Lined", 6, 3, 35, 40),
    ("Wind-Breaker", "Wind Resistive", 7, 3, 35, 40),
    ("Divine Breastplate", "Ancient", 8, 4, 100, 100),
    ("Overcomer's Diadem", "Ancient", 8, 4, 100, 100),
    ("Shield of Hope", "Ancient", 8, 4, 100, 100)
    ]

    # Add armors if file is empty
if not aManager.armor:
    for armor in all_armors:
        aManager.add_armor(*armor)

"""
aManager.aEquip("Basic Buckler", "Monte")
aManager.aEquip("Basic Leather", "Abigail")

    # Unlock some armors
aManager.unlock_armor("Wooden Shield")

    # Display inventory
aManager.display_inventory()

    # Search for armors by type
print("\nSearching for Flame-Retardant armors:")
superheated_armors = aManager.search_armors("atype", "Flame-Retardant")
for armor in superheated_armors:
    armor.display()

 

"""
