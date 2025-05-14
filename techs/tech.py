import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import json
import os

class Tech:
    def __init__(self,tname, tpwr, txp, tlv, txpcap, tmstr, tpaired, tavail, ttype):
        self.tname = tname
        self.tpwr = {}
        self.txp = txp
        self.tlv = tlv
        self.txpcap = txpcap
        self.tmstr = tmstr
        self.tpaired = tpaired
        self.tavail = tavail
        self.ttype = ttype

    def to_dict(self):
        return {
                "name": self.tname,
                "tpwr": self.tpwr,
                "txp": self.txp,
                "tlv": self.tlv,
                "txpcap": self.txpcap,
                "tmstr": self.tmstr,
                "tpaired": self.tpaired,
                "tavail": self.tavail,
                "ttype": self.ttype
                }

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
                data["tavail"],
                data["ttype"]
                )

class TechManager:
    def __init__(self):
        self.techfile = "techs/techs.json"
        self.kTech = "techs/kTech.json"
        self.aTech = "techs/aTech.json"
        self.mTech = "techs/mTech.json"
        self.kFile = "inventory/kFile.json"
        self.aFIle = "inventory/aFile.json"
        self.mFile = "inventory/mFile.json"
        self.kw_slots = []
        self.ka_slots = []
        self.aw_slots = []
        self.aa_slots = []
        self.mw_slots = []
        self.ma_slots = []

    def create_techs(self, init_tech_list):
        if not os.path.exists(self.techfile):
            try:
                with open (self.techfile, "w") as master_list:
                    for tech in init_tech_list:
                        json.dump([tech.to_dict()], master_list, indent = 4)
                        print(f"{tech.tname} successfully added to master list!")
            except json.JSONDecodeError:
                print("Error Invalid JSON file format.")

    def slot_combo():
        pass

    """
        self.load_techs()
        self.load_tpwr()
        self.save_tpwr()
        self.save_techs()
        self.get_slots()
        self.set_slots()
        self.save_slots()
        self.slot_combos()

    @classmethod
    def slot_combos():
        pass
    """

flamethrowing_chip = Tech("Flame-Thrower", {"Throw Flames: ": (40, 10), "Throw Flamier: ": (80, 14), "Throw Flamiest: ": (120, 18)}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

atmospheric_condenser = Tech("Water Condenser", {"Make It Rain: ": (40, 10), "Make It Rainier: ": (80, 14), "Make it Rainiest: ": (120, 18)}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

hi_volt_discharger = Tech("Hi-Volt Discharger", {"Lightning Strike: ": (40, 10), "Lightning Strikier: ": (80, 14), "Lightning Strikiest: ": (120, 18)}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

freon_former = Tech("Freon Former", {"Form Freon: ": (40, 10), "Form Freonier: ": (80, 14), "Formiest Freon: ": (120, 18)}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

jet_turbine_chip = Tech("Jet Turbine", {"Wind Blast: ": (50, 12), "Windier Blast: ": (100, 16), "Windiest Blast: ": (150, 20)}, 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

seismic_disruptor = Tech("Seismic Disruptor", {"Disrupt Earth: ": (50, 12), "Disruptier Earth: ": (100, 16), "Disruptiest Earth: ": (150, 20)}, 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

light_of_ages = Tech("Light of the Ages", {"Celestial Beam: ": (60, 14), "Holy Ray: ": (120, 18), "Light of Heaven: ": (180, 22)}, 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane")

restore = Tech("Restore", {"Restore Health: ": (40, 6), "Restore More: ": (80, 8), "Restore Most: ": (120, 10)}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon")

regen = Tech("Regenerate", {"Regenerate Health: ": (10, 10), "Regenrate Health/Energy: ": (20, 20), "Regenerate Party: ": (20, 40)}, 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon")

panacea = Tech("Cure Ailment", {"Cure Minor Ail: ": (0, 8), "Cure Major Ail: ": (0, 12), "Panacea: ": (0, 20)}, 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon")

overclock = Tech("Overclock", {"Speed-Up: ": (1, 10), "Speed-Up All: ": (2, 15), "Super-Speed All: ": (3, 20)}, 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon")

auto_cover = Tech("Cover Allies", {}, 0, 1, 5000, False, {}, False, "Auto")

auto_auto = Tech("Automate", {}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Auto")

auto_link = Tech("Link", {}, 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Auto")

init_tech_list = [flamethrowing_chip, atmospheric_condenser, hi_volt_discharger, freon_former, jet_turbine_chip, seismic_disruptor, light_of_ages, restore, regen, panacea, overclock, auto_cover, auto_auto, auto_link]

tManager = TechManager()
tManager.create_techs(init_tech_list)
"""
tname, tpwr, txp, tlv, txpcap, tmsr, tpaired, tavail
t = Tech()
"""
