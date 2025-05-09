import json

class PlayableCharacter:
    def __init__(self, name, lvl, exp, hp, eng, stg, ig, con, wis, pdef, tbar, agi):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.hp = hp
        self.eng = eng
        self.stg = stg
        self.ig = ig
        self.con = con
        self.wis = wis
        self.pdef = pdef
        self.tbar = tbar
        self.agi = agi


    """
    Stats: hit points, energy is MP,
    stg (strength) is physical attack, 
    ig (intelligence) tech attack strength
    con (Constitution) adds to HP
    wis (wisdom) addds to eng
    pdef (physical defense) mitigates physical damage
    tbar (tech barrier) mitigates tech damage
    agi (Agility) increses ATB and dodge
    """
        
               
    def display_char(self):
        """Display character details."""
        CharacterManager.load_chars()
        print(f"Name: {self.name}")
        print(f"Level: {self.lvl}")
        print(f"XP: {self.exp}")
        print(f"HP: {self.hp}")
        print(f"Energy: {self.eng}")
        print(f"Strength: {self.stg}")
        print(f"Intelligence: {self.ig}")
        print(f"Constitution: {self.con}")
        print(f"Wisdom: {self.wis}")
        print(f"Phys. Defense: {self.pdef}")
        print(f"Tech Barrier: {self.tbar}")
        print(f"Agility: {self.agi}")
        return

    def to_dict(self):
        """Convert PC object to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "lvl": self.lvl,
            "exp": self.exp,
            "hp": self.hp,
            "eng": self.eng,
            "stg": self.stg,
            "ig": self.ig,
            "con": self.con,
            "wis": self.wis,
            "pdef": self.pdef,
            "tbar": self.tbar,
            "agi": self.agi
        }

    @classmethod
    def from_dict(cls, data):
        """Create PC object from dictionary."""
        return cls(
            data["name"],
            data["lvl"],
            data["exp"],
            data["hp"],
            data["eng"],
            data["stg"],
            data["ig"],
            data["con"],
            data["wis"],
            data["pdef"],
            data["tbar"],
            data["agi"],
        )

class CharacterManager:
    def __init__(self, filename="party/p_list.json"):
        self.filename = filename
        self.kFile = "party/pcs/Kris/kris.json"
        self.aFile = "party/pcs/Abigail/abigail.json"
        self.mFile = "party/pcs/Monte/monte.json"
        self.party = []
        self.load_chars()

    def load_chars(self):
        with open (self.kFile, "r") as kfile:
            kdata = json.load(kfile)
            for kris in kdata:
                self.party.append(PlayableCharacter.from_dict(kris))
        with open (self.aFile, "r") as afile:
            adata = json.load(afile)
            for abigail in adata:
                self.party.append(PlayableCharacter.from_dict(abigail))
        with open (self.mFile, "r") as mfile:
            mdata = json.load(mfile)
            for monte in mdata:
                self.party.append(PlayableCharacter.from_dict(monte))
        return self.party

    def save_party(self):
        with open(self.filename, 'w') as file:
            json.dump([char.to_dict() for char in self.party], file, indent=4)
        print("Party is set")


"""
    def load_party(self):
         if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.party = []
                for character in data:
                    char_name = character.get("name")
                    if char_name == "Kris":
                        self.party.append(.from_dict(enemy))
                    elif char_name == "Beast":
                        self.enemies.append(Beast.from_dict(enemy))
                    else:
                        self.enemies.append(Enemy.from_dict(enemy))
                self.encounter = [enemy for enemy in self.enemies if enemy.isAlive]
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format.")
            self.enemies = []
            self.encounter = []

    def load(self):
        self.filename = "enemies/basic/enemylist2.json"
        with open(self.filename, 'w') as file:
            json.dump([enemy.to_dict() for enemy in self.enemies], file, indent=4)

    def update_char(self, name, lvl, exp, hp, eng, stg, ig, con, wis, pdef, tbar, agi):
        enemy = Enemy(ename, hp, eng, atk, tech, resist, weak, isAlive)
        self.enemies.append(enemy)
        print(f"Added {ename} to enemies list.")
        return enemy

"""


kris = PlayableCharacter("Kris", 1, 0, 150, 80, 20, 15, 25, 15, 20, 20, 15)
abigail = PlayableCharacter("Abigail", 1, 0,110, 100, 12, 22, 15, 20, 15, 18, 17)
monte = PlayableCharacter("Monte", 1, 0, 120, 90, 15, 20, 15, 18, 20, 20, 20)
all_chars = [kris, abigail, monte]


kFile = "party/pcs/Kris/kris.json"
aFile = "party/pcs/Abigail/abigail.json"
mFile = "party/pcs/Monte/monte.json"
cManager = CharacterManager()
kris.display_char()
