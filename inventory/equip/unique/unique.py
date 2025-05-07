import json
import os
from uuid import uuid4

class Unique:
    def __init__(self, uname, utype, boon, mastery, mastered_boon, mboon_avail=False, is_avail=False):
        self.id = str(uuid4())  # Unique identifier for each unique
        self.uname = uname
        self.utype = utype
        self.boon = boon
        self.mastery = mastery
        self.mastered_boon = mastered_boon
        self.mboon_avail = mboon_avail  
        self.is_avail = is_avail    # Whether the unique is unlocked

    def to_dict(self):
        """Convert Unique object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "uname": self.uname,
            "utype": self.utype,
            "boon": self.boon,
            "mastery": self.mastery,
            "mastered_boon": self.mastered_boon,
            "mboon_avail": self.mboon_avail,
            "is_avail": self.is_avail
        }

    @classmethod
    def from_dict(cls, data):
        """Create Unique object from dictionary."""
        return cls(
            data["uname"],
            data["utype"],
            data["boon"],
            data["mastery"],
            data["mastered_boon"],
            data["mboon_avail"],
            data["is_avail"]
        )

    def display(self):
        """Display unique details."""
        print(f"Name: {self.uname}")
        print(f"Type: {self.utype}")
        print(f"Boon: {self.boon}")
        print(f"Mastery: {self.mastery}")
        print(f"Mastered Boon: {self.mastered_boon}")
        print(f"M. Boon Unlocked: {self.mboon_avail}")
        print(f"Unlocked: {self.is_avail}")

class UniqueManager:
    def __init__(self, filename="inventory/equip/unique/uniquelist.json"):
        self.filename = filename
        self.uniques = []
        self.inventory = []
        self.load_uniques()

    def load_uniques(self):
        """Load uniques from JSON file."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.uniques = [Unique.from_dict(unique) for unique in data]
                self.inventory = [unique for unique in self.uniques if unique.is_avail]
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.uniques = []
            self.inventory = []

    def save_uniques(self):
        """Save uniques to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([unique.to_dict() for unique in self.uniques], file, indent=4)

    def add_unique(self, uname, utype, boon, mastery, mastered_boon, mboon_avail=False, is_avail=False):
        """Add a new unique and save to file."""
        unique = Unique(uname, utype, boon, mastery, mastered_boon, mboon_avail, is_avail)
        self.uniques.append(unique)
        if is_avail:
            self.inventory.append(unique)
        self.save_uniques()
        print(f"Added {uname} to uniques list.")
        return unique

    def unlock_unique(self, unique_name):
        """Unlock a unique and add to inventory."""
        for unique in self.uniques:
            if unique.uname.lower() == unique_name.lower():
                if unique.is_avail:
                    print(f"{unique_name} is already unlocked.")
                else:
                    unique.is_avail = True
                    self.inventory.append(unique)
                    self.save_uniques()
                    print(f"Unlocked {unique_name} and added to inventory.")
                return
        print(f"Unique {unique_name} not found.")

    def display_inventory(self):
        """Display all uniques in inventory."""
        if not self.inventory:
            print("Your inventory is sadly empty... go get stuff!")
        else:
            print("Your inventory:")
            for unique in self.inventory:
                print(f"- {unique.uname} (Type: {unique.utype}, Boon: {unique.boon}, Mastery/Mastered Boon: {unique.mastery}/{unique.mastered_boon})")

    def search_uniques(self, key, value):
        """Search for uniques by key-value pair."""
        for unique in self.uniques:
            return [unique for unique in self.uniques if hasattr(unique, key) and getattr(unique, key) == value and unique.is_avail]

# Example usage

utype = {
    "Headband": "Mind-Focusing",
    "Superconductor": "Energy Producing",
    "Bionic": "Strength Enhancing",
    "Nanotech": "Health Boosting",
    "Shielding": "Defensive",
    "Mind-Body Sync": "Speed Altering",
    "Ancient": "Holy"
    }

    # Initialize uManager
uManager = UniqueManager()

    # Add initial uniques
all_uniques = [
    ("Brainwave Stim", "Headband", "Mind-Focusing", 1, "ATB Increae"),
    ("Compact Cell", "Superconductor", "Energy Producing", 1, "Techs Iterate Twice"),
    ("Robotic Suit", "Bionic", "Strength Enhancing", 1, "Attacks Iterate Twice"),
    ("Tubeless Nanobot Pump", "Nanotech", "Health Boosting", 1, "All Stat Small Boost"),
    ("Holtzman Shield", "Shielding", "Defensive", 1, "Gain Regenerating Overshield"),
    ("Military Exosuit", "Mind-Body Sync", "Speed Altering", 1, "All Stat Med. Boost"),
    ("Mysterious Scabbard", "Ancient", "Holy", 1, "L. Stat Boost & Ailment Resistant"),
    ("Mysterious Bracelet", "Ancient", "Holy", 1, "L. Stat Boost & Ailment Resistant"),
    ("Mysterious Gunbelt", "Ancient", "Holy", 1, "L. Stat Boost & Ailment Resistant")
    ]

    # Add uniques if file is empty
if not uManager.uniques:
    for unique in all_uniques:
        uManager.add_unique(*unique)
"""
    # Unlock some uniques
uManager.unlock_unique("Brainwave Stim")
uManager.unlock_unique("Compact Cell")

    # Display inventory
uManager.display_inventory()

    # Search for uniques by type
print("\nSearching for Superconductor uniques:")
superconductor_uniques = uManager.search_uniques("utype", "Superconductor")
for unique in superheated_uniques:
    unique.display()

    # Search for uniques by mastered boon availability
print("\nSearching for Mastered uniques:")
mastered_uniques = uManager.search_uniques("mboon_avail", True)
for unique in mastered_uniques:
    unique.display()

"""
