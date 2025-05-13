import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import json

class Tech:
    def __init__(self):
        self.techfile = "tech/techs.json"
        self.kTech = "tech/kTech.json"
        self.aTech = "tech/aTech.json"
        self.mTech = "tech/mTech.json"
        self.kFile = "inventory/kFile.json"
        self.aFIle = "inventory/aFile.json"
        self.mFile = "inventory/mFile.json"
        self.kw_slots = []
        self.ka_slots = []
        self.aw_slots = []
        self.aa_slots = []
        self.mw_slots = []
        self.ma_slots = []
        self.to_dict()
        self.create_techs()
        self.load_techs()
        self.save_techs()
        self.get_slots()
        self.slot_combos()

    def to_dict(self):
        return {
                "name": self.tname,
                "tpwr": self.tpwr,
                "txp": self.txp,
                "tlv": self.tlv,
                "txpcap": self.txpcap,
                "tmstr": self.tmstr,
                "tpaired": self.tpaired,
                "tavail": self.tavail
                }

    def create_techs(self,tech_list):
        with open self.techfile, "w") as master_list:
            for tech in tech_list:
                json.dump(tech.to_dict(), master_list, indent = 4)

    @classmethod
    def from_dict(cls, data):
        return cls(
                data["name"],
                data["tpwr"],
                data["txp"],
                data["tlv"],
                data["txpcap"],
                data["tmstr"],
                data["tpaired"],
                data["tavail"]
                )

"""
tech_list = [to do]
t = Tech()
"""
