import json
import random
from uuid import uuid4
import os
"""FINAL - 5/8/25"""
class Enemy:
    def __init__(self, ename, hp, eng, atk, tech, resist, weak, isAlive):
        self.id = str(uuid4()) 
        self.ename = ename
        self.hp = hp
        self.eng = eng
        self.atk = atk
        self.tech = tech
        self.resist = resist
        self.weak = weak
        self.isAlive = isAlive

    def to_dict(self):
        """Convert Enemy object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "ename": self.ename,
            "hp": self.hp,
            "eng": self.eng,
            "atk": self.atk,
            "tech": self.tech,
            "resist": self.resist,
            "weak": self.weak,
            "is_alive": self.isAlive,
            "type": "Enemy"
        }

    @classmethod
    def from_dict(cls, data):
        """Create enemy object from dictionary."""
        return cls(
            data["ename"],
            data["hp"],
            data["eng"],
            data["atk"],
            data["tech"],
            data["resist"],
            data["weak"],
            data["is_alive"]
        )

    def display(self):
        """Display enemy details."""
        print(f"Name: {self.ename}")
        print(f"HP: {self.hp}")
        print(f"Energy: {self.eng}")
        print(f"Attack: {self.atk}")
        print(f"Tech: {self.tech}")
        print(f"Resistance: {self.resist}")
        print(f"Weakness: {self.weak}")

class Enemy_chief(Enemy):
    def __init__(self, ename, hp, eng, atk, tech, tech2, resist, weak, isAlive):
        super().__init__(ename, hp, eng, atk, tech, resist, weak, isAlive)
        self.tech2 = tech2

    def to_dict(self):
        """Convert Enemy_chief object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "ename": self.ename,
            "hp": self.hp,
            "eng": self.eng,
            "atk": self.atk,
            "tech": self.tech,
            "tech2": self.tech2,
            "resist": self.resist,
            "weak": self.weak,
            "is_alive": self.isAlive,
            "type": "Enemy_chief"
        }

    @classmethod
    def from_dict(cls, data):
        """Create enemy object from dictionary."""
        return cls(
            data["ename"],
            data["hp"],
            data["eng"],
            data["atk"],
            data["tech"],
            data["tech2"],
            data["resist"],
            data["weak"],
            data["is_alive"]
        )

    def display(self):
        """Display enemy details."""
        print(f"Name: {self.ename}")
        print(f"HP: {self.hp}")
        print(f"Energy: {self.eng}")
        print(f"Attack: {self.atk}")
        print(f"Tech: {self.tech}")
        print(f"Second Tech: {self.tech2}")
        print(f"Resistance: {self.resist}")
        print(f"Weakness: {self.weak}")

class Beast(Enemy):
    def __init__(self, ename, hp, eng, atk, atk2, tech, resist, weak, isAlive):
        super().__init__(ename, hp, eng, atk, tech, resist, weak, isAlive)
        self.atk2 = atk2

    def to_dict(self):
        """Convert Beast object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "ename": self.ename,
            "hp": self.hp,
            "eng": self.eng,
            "atk": self.atk,
            "atk2": self.atk2,
            "tech": self.tech,
            "resist": self.resist,
            "weak": self.weak,
            "is_alive": self.isAlive,
            "type": "Beast"
        }

    @classmethod
    def from_dict(cls, data):
        """Create enemy object from dictionary."""
        return cls(
            data["ename"],
            data["hp"],
            data["eng"],
            data["atk"],
            data["atk2"],
            data["tech"],
            data["resist"],
            data["weak"],
            data["is_alive"]
        )

    def display(self):
        """Display enemy details."""
        print(f"Name: {self.ename}")
        print(f"HP: {self.hp}")
        print(f"Energy: {self.eng}")
        print(f"Attack: {self.atk}")
        print(f"Second Attack: {self.atk2}")
        print(f"Tech: {self.tech}")
        print(f"Resistance: {self.resist}")
        print(f"Weakness: {self.weak}")

class EnemyManager:
    def __init__(self, filename="enemies/basic/enemylist.json"):
        self.filename = filename
        self.enemies = []
        self.encounter = []
        self.load_enemies()

    def load_enemies(self):
        """Load enemies from JSON file."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.enemies = []
                for enemy in data:
                    enemy_type = enemy.get("type", "Enemy")
                    if enemy_type == "Enemy_chief":
                        self.enemies.append(Enemy_chief.from_dict(enemy))
                    elif enemy_type == "Beast":
                        self.enemies.append(Beast.from_dict(enemy))
                    else:
                        self.enemies.append(Enemy.from_dict(enemy))
                self.encounter = [enemy for enemy in self.enemies if enemy.isAlive]
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.enemies = []
            self.encounter = []

    def save_enemies(self):
        """Save enemies to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([enemy.to_dict() for enemy in self.enemies], file, indent=4)

    def save_enemies2(self):
        """Save enemies to JSON file."""
        self.filename = "enemies/basic/enemylist2.json"
        with open(self.filename, 'w') as file:
            json.dump([enemy.to_dict() for enemy in self.enemies], file, indent=4)

    def add_enemy(self, ename, hp, eng, atk, tech, resist, weak, isAlive=True):
        """Add a new enemy and save to file."""
        enemy = Enemy(ename, hp, eng, atk, tech, resist, weak, isAlive)
        self.enemies.append(enemy)
        print(f"Added {ename} to enemies list.")
        return enemy

    def add_chief(self, ename, hp, eng, atk, tech, tech2, resist, weak, isAlive=True):
        """Add a new enemy and save to file."""
        enemy = Enemy_chief(ename, hp, eng, atk, tech, tech2, resist, weak, isAlive)
        self.enemies.append(enemy)
        print(f"Added {ename} to enemies list.")
        return enemy

    def add_beast(self, ename, hp, eng, atk, atk2, tech, resist, weak, isAlive=True):
        """Add a new enemy and save to file."""
        enemy = Beast(ename, hp, eng, atk, atk2, tech, resist, weak, isAlive)
        self.enemies.append(enemy)
        print(f"Added {ename} to enemies list.")
        return enemy

    def randEnc(self):
        """Load enemies from JSON lists, pick random enemies and quantities, save to a new JSON file, and print the number and type of enemies."""
    
        # Load enemy lists from JSON files
        enemyList1 = []
        enemyList2 = []
        try:
            with open("enemies/basic/enemylist.json", 'r') as file:
                enemyList1 = json.load(file)
            with open("enemies/basic/enemylist2.json", 'r') as file:
                enemyList2 = json.load(file)
        except FileNotFoundError:
            print("Error: One or both JSON files not found.")
            return
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in one or both files.")
            return

        # Choose a random enemy list
        enc_choice = random.choice([enemyList1, enemyList2])
        enc_list = []
    
        # Select random quantities
        x = random.randint(1, 3)  # Number of first enemy type
        y = random.randint(1, 3)  # Number of second enemy type

        # Pick first enemy
        a = random.choice(enc_choice)
        enemy_a = None
        if a["type"] == "Enemy_chief":
            enemy_a = Enemy_chief.from_dict(a)
        elif a["type"] == "Beast":
            enemy_a = Beast.from_dict(a)
        else:
            enemy_a = Enemy.from_dict(a)
    
        # Add x copies of enemy_a to enc_list
        for _ in range(x):
            enc_list.append(enemy_a.to_dict())

        # Pick second enemy
        b = random.choice(enc_choice)
        enemy_b = None
        if b["type"] == "Enemy_chief":
            enemy_b = Enemy_chief.from_dict(b)
        elif b["type"] == "Beast":
            enemy_b = Beast.from_dict(b)
        else:
            enemy_b = Enemy.from_dict(b)
    
        # Add y copies of enemy_b to enc_list
        for _ in range(y):
            enc_list.append(enemy_b.to_dict())

        # Print encounter details
        if a["ename"] == b["ename"]:
            z = x + y
            print(f"You encounter {z} {a['ename']}s")
        elif x == 0:
            if y > 1:
                print(f"You encounter {y} {b['ename']}s")
            else:
                print(f"You encounter {y} {b['ename']}")
        elif y == 0:
            if x > 1:
                print(f"You encounter {x} {a['ename']}s")
            else:
                print(f"You encounter {x} {a['ename']}")
        else:
            if x > 1 and y > 1:
                print(f"You encounter {x} {a['ename']}s and {y} {b['ename']}s")
            elif x > 1 and y == 1:
                print(f"You encounter {x} {a['ename']}s and {y} {b['ename']}")
            elif x == 1 and y > 1:
                print(f"You encounter {x} {a['ename']} and {y} {b['ename']}s")
            else:
                print(f"You encounter {x} {a['ename']} and {y} {b['ename']}")

        # Save encounter to a new JSON file
        with open("enemies/encounter.json", 'w') as file:
            json.dump(enc_list, file, indent=4)

"""
    def wEquip(self, enemy_name):
        for enemy in self.inventory:
            if enemy.ename.lower() == enemy_name.lower():
                print(f"Equipped {enemy.ename}")
                if enemy.is_unique == "Kris":
                    kFilepath = "inventory/equip/enemies/Krisenemy.json"
                    self.kFilename = kFilepath
                    with open(self.kFilename, "w") as file:
                        json.dump([enemy.to_dict()], file, indent=4)
                elif enemy.is_unique == "Abigail":
                    aFilepath = "inventory/equip/enemies/Abigailenemy.json"
                    self.aFilename = aFilepath
                    with open(self.aFilename, "w") as file:
                        json.dump([enemy.to_dict()], file, indent=4)
                elif enemy.is_unique == "Monte":
                    mFilepath = "inventory/equip/enemies/Monteenemy.json"
                    self.mFilename = mFilepath
                    with open(self.mFilename, "w") as file:
                        json.dump([enemy.to_dict()], file, indent=4)
                else:
                    break
"""
# Example usage
resist = {
    "Normal": "None",
    "Superheated": "Fire",
    "Precipitative": "Water",
    "Discharging": "Electric",
    "Frostbitten": "Ice",
    "Jet Turbined": "Wind",
    "Seismic": "Rock",
    "Ancient": "Holy"
}
weak = {
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
eManager = EnemyManager()

goblin = Enemy("Goblin", 50, 10, 5, "None", "Normal", "Discharging", True)
gob_chief = Enemy_chief("Goblin Chief", 80, 20, 10, "Fire", "Heal", "Superheated", "Discharging", True)
gob_heavy = Enemy("Heavy Goblin", 100, 30, 25, "Missile", "Normal", "Discharging", True)
cave_spider = Beast("Cave Spider", 60, 10, 5, 15, "Poison Bite", "Poison", "Superheated", True)
fang_mole = Beast("Fang Mole", 80, 10, 10, 20, "Fang", "Normal", "Superheated", True)
enemyList1 = [goblin, gob_chief, gob_heavy]
enemyList2 = [cave_spider, fang_mole]

if not eManager.enemies:
    for enemy in enemyList1:
        eManager.enemies.append(enemy)
        if enemy.isAlive:
            eManager.encounter.append(enemy)
    eManager.save_enemies()

eManager.enemies = []
eManager.encounter = []
for enemy in enemyList2:
    eManager.enemies.append(enemy)
    if enemy.isAlive:
        eManager.encounter.append(enemy)
eManager.save_enemies2()



