import json
import os
from math import floor
import math


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
    def __init__(self, filename="party/pcs/p_list.json"):
        self.filename = filename
        self.kFile = "party/pcs/Kris/kris.json"
        self.aFile = "party/pcs/Abigail/abigail.json"
        self.mFile = "party/pcs/Monte/monte.json"
        self.party = []
        self.ap_list = []
        self.names = []
        self.in_party = []
        self.fullxp = []
        self.halfxp = []
        self.create_chars()
        self.load_chars()
        self.save_party()

    def create_chars(self):
        if not os.path.exists(self.kFile):
            try:
                with open(self.kFile, "w") as kfile:
                    json.dump([kris.to_dict()], kfile, indent = 4)
                    print("Kris file created")
            except json.JSONDecodeError:
                print("Error: Invalid JSON file format.")
        if not os.path.exists(self.aFile):
            try:
                with open(self.aFile, "w") as afile:
                    json.dump([abigail.to_dict()], afile, indent = 4)
                    print("Abigail file created")
            except json.JSONDecodeError:
                print("Error: Invalid JSON file format.")
        if not os.path.exists(self.mFile):
            try:
                with open(self.mFile, "w") as mfile:
                    json.dump([monte.to_dict()], mfile, indent = 4)
                    print("Monte file created")
            except json.JSONDecodeError:
                print("Error: Invalid JSON file format.")
        if not os.path.exists("party/pcs/p_list.json"):
            try:
                with open("party/pcs/p_list.json", "w") as pl:
                    json.dump([kris.to_dict()], pl, indent = 4)
            except json.JSONDecodeError:
                print("Error: Invalid JSON file format.")

        if not os.path.exists("party/active_party.json"):
            try:
                with open("party/active_party.json", "w") as ap:
                    json.dump([kris.to_dict()], ap, indent = 4)
            except json.JSONDecodeError:
                print("Error: Invalid JSON file format.")
        else:
            return

    def load_chars(self):
        self.party = []
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

    def save_party(self):
        with open(self.filename, 'w') as file:
            json.dump([char.to_dict() for char in self.party], file, indent=4)

    def active_party(self, active_list):
        self.ap_list = []
        self.active_list = active_list
        with open ("party/active_party.json", "w") as ap:
            for i in self.active_list:
                if i == "kris":
                    with open(self.kFile, "r") as kfile:
                        kdata = json.load(kfile)
                        for kris in kdata:
                            self.ap_list.append(PlayableCharacter.from_dict(kris))
                if i =="abigail":
                    with open(self.aFile, "r") as afile:
                        adata = json.load(afile)
                        for abigail in adata:
                            self.ap_list.append(PlayableCharacter.from_dict(abigail))
                if i == "monte":
                    with open(self.mFile, "r") as mfile:
                        mdata = json.load(mfile)
                        for monte in mdata:
                            self.ap_list.append(PlayableCharacter.from_dict(monte))
            json.dump([char.to_dict() for char in self.ap_list], ap, indent = 4)

    def gain_xp(self, xp_gained):
        self.party = []
        with open (self.filename, "r") as pl:
            characters = json.load(pl)
        for char in characters:
            array = PlayableCharacter.from_dict(char)
            self.party.append(array)
            self.names.append(array.name)
        with open ("party/active_party.json", "r") as ap:
            party = json.load(ap)
        for char in party:
            p = PlayableCharacter.from_dict(char)
            self.ap_list.append(p)
            self.in_party.append(p.name)
        for char in self.names:
            if char not in self.in_party:
                self.halfxp.append(char.lower())
            else:
                self.fullxp.append(char.lower())
        print(f"Full XP: {self.fullxp} \n Half XP: {self.halfxp}")
        updated_characters = []
        for char_dict in characters:
            char_name = char_dict["name"].lower()
            if char_name in self.fullxp:
                char_dict["exp"] = char_dict.get("exp") + xp_gained
                print(f"Granted {xp_gained} XP to {char_dict['name']} (Full XP)")
            elif char_name in self.halfxp:
                half_xp = xp_gained // 2
                char_dict["exp"] = char_dict.get("exp") + half_xp
                print(f"Granted {half_xp} XP to {char_dict['name']} (Half XP)")
            current_lvl = int(char_dict["lvl"])
            x_modifier = (current_lvl // 10) + 68
            xp_needed_to_lvl = floor((100 * ((current_lvl + 1) ** 2)) - 100 * current_lvl + (current_lvl * x_modifier * (current_lvl -1)))
            updated_characters.append(char_dict)
            if char_dict.get("exp") >= xp_needed_to_lvl:
                CharacterManager.level_up(self, char_dict["name"].title(), updated_characters)
                
            if char_dict["name"].title() == "Kris":
                try:
                    with open(self.kFile, "w") as kfile:
                        json.dump([char_dict], kfile, indent=4)
                    print(f"Updated character XP saved to {self.kFile}")
                except Exception as e:
                    print(f"Error saving to {self.kFile}: {e}")
            if char_dict["name"].title() == "Abigail":
                try:
                    with open(self.aFile, "w") as afile:
                        json.dump([char_dict], afile, indent=4)
                    print(f"Updated character XP saved to {self.aFile}")
                except Exception as e:
                    print(f"Error saving to {self.aFile}: {e}")
            if char_dict["name"].title() == "Monte":
                try:
                    with open(self.mFile, "w") as mfile:
                        json.dump([char_dict], mfile, indent=4)
                    print(f"Updated character XP saved to {self.mFile}")
                except Exception as e:
                    print(f"Error saving to {self.mFile}: {e}")
        CharacterManager.active_party(self, self.fullxp)
        CharacterManager.load_chars(self)
        CharacterManager.save_party(self)
        for i in updated_characters:
            print(i)


    def level_up(self, character_name, updated_characters):
        for char in updated_characters:
            name = char.get("name")
            if name == character_name:
                print(f"{character_name} levelled up!")
                lvl = char.get("lvl")
                hp = char.get("hp")
                hp += floor(-3*math.log10(lvl)+104.195)
                eng = char.get("eng")
                eng += floor(-1*math.log10(lvl)+10.95)
                stg = char.get("stg")
                stg += floor(-3*math.log10(lvl)+8)
                ig = char.get("ig")
                ig += floor(-3*math.log10(lvl)+8)
                con = char.get("con")
                con += floor(-3*math.log10(lvl)+8)
                wis = char.get("wis")
                wis += floor(-3*math.log10(lvl)+8)
                pdef = char.get("pdef")
                pdef += floor(-3*math.log10(lvl)+8)
                tbar = char.get("tbar")
                tbar += floor(-3*math.log10(lvl)+8)
                agi = char.get("agi")
                agi += floor(-3*math.log10(lvl)+8)
                lvl += 1
                char.update({"lvl": lvl, "hp": hp, "eng": eng, "stg": stg, "ig": ig, "con": con, "wis": wis, "pdef": pdef, "tbar": tbar, "agi": agi})
        
        with open(self.filename, "r") as pl:
            characters = json.load(pl)
        selected_character = None
        if character_name:
            for char_data in characters:
                if char_data["name"].lower() == character_name.lower():
                    selected_character = char_data
                elif char_data["name"].lower() == character_name.lower():
                    selected_character = char_data
                elif char_data["name"].lower() == character_name.lower():
                    selected_character = char_data
                    break
            if not selected_character:
                print(f"Error: Character '{character_name}' not found in {json_file}.")
                return

        char_name = selected_character.get("name")
        if char_name == "Kris":
            character = PlayableCharacter.from_dict(selected_character)
        elif char_name == "Abigail":
            character = PlayableCharacter.from_dict(selected_character)
        else:
            character = PlayableCharacter.from_dict(selected_character)



kris = PlayableCharacter("Kris", 1, 0, 200, 80, 20, 15, 25, 15, 20, 20, 15)
abigail = PlayableCharacter("Abigail", 1, 0,150, 110, 12, 25, 15, 20, 15, 18, 17)
monte = PlayableCharacter("Monte", 1, 0, 180, 90, 15, 20, 15, 18, 20, 20, 20)
all_chars_start = [kris, abigail, monte]
cManager = CharacterManager()
cManager.create_chars()

active_list = ["kris", "abigail"]
cManager.active_party(active_list)
"""
cManager.gain_xp(300)

cManager.load_chars()
cManager.save_party()

"""

