import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import json
import os

class Tech:
    def __init__(self,tname, tpwr, txp, tlv, txpcap, tmstr, tpaired, tavail, ttype):
        self.tname = tname
        self.tpwr = tpwr
        self.txp = txp
        self.tlv = tlv
        self.txpcap = txpcap
        self.tmstr = tmstr
        self.tpaired = tpaired
        self.tavail = tavail
        self.ttype = ttype

    def to_dict(self):
        return {
                "tname": self.tname,
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
                data["tname"],
                data["tpwr"],
                data["txp"],
                data["tlv"],
                data["txpcap"],
                data["tmstr"],
                data["tpaired"],
                data["tavail"],
                data["ttype"]
                )

    class BaneBoonTpwr:
        def __init__(self, p1, p1t, p2, p2t, p3, p3t):
            self.p1 = p1
            self.p1t = p1t
            self.p2 = p2
            self.p2t = p2t
            self.p3 = p3
            self.p3t = p3t

        def bb_to_dict(self):
            return {
                    "p1": self.p1,
                    "p1t": self.p1t,
                    "p2": self.p2,
                    "p2t": self.p2t,
                    "p3": self.p3,
                    "p3t": self.p3t
                    }

        @classmethod
        def bb_from_dict(cls, data):
            return cls(
                    data["p1"],
                    data["p1t"],
                    data["p2"],
                    data["p2t"],
                    data["p3"],
                    data["p3t"]
                    )

    class AutoTpwr:
        def __init__(self, status):
            self.status = status

        def a_to_dict(self):
            return {
                    "status": self.status
                    }
        @classmethod
        def a_from_dict(cls, data):
            return cls(
            data["status"]
            )

class TechManager:
    def __init__(self):
        self.techfile = "techs/techs.json"

    def create_techs(self, init_tech_list):
        self.techs = []
        for tech in init_tech_list:
            self.techs.append(tech)
        if not os.path.exists(self.techfile):
            try:
                with open (self.techfile, "w") as master_list:
                    json.dump(self.techs, master_list, indent = 4)
                    #json.dump([tech.to_dict() for tech in self.techs], master_list, indent = 4)
                    #print(f"{tech.tname} successfully added to master list!")
            except json.JSONDecodeError:
                print("Error Invalid JSON file format.")

    def load_techs(self):
        self.techs = []
        with open (self.techfile, "r") as file:
            self.tdata = json.load(file)
            for tech in self.tdata:
                self.techs.append(Tech.from_dict(tech))
            for tech in self.tdata:
                print (tech.get("tpwr"))
            print("loaded!")
            #tpwrs["tpwr"] = self.tdata.get("tpwr")
        #print(tpwrs)

    def ck(self):
        self.pwer_list = []
        for tech in self.tdata:
            self.pwer_list.append(tech.get("tpwr"))

    def make_available(self, tname):
        with open(self.techfile, "r") as file:
            data = json.load(file)
            for tech in data:
                if tname == tech.get("tname") and tech.get("tavail") == False:
                    tech.update({"tavail": True})
                    unlocked = tech
        print(unlocked)
        print(tname + " Avaialable")
        if not os.path.exists("techs/unlocked.json"):
            with open("techs/unlocked.json", "w") as unlock_file:
                json.dump([unlocked], unlock_file, indent = 4)
        if os.path.exists("techs/unlocked.json"):
            with open("techs/unlocked.json", "r") as unlock_file:
                udata = json.load(unlock_file)
                unlocked = Tech.from_dict(unlocked)
                for i in udata:
                    updated_list = []
                    updated_list.append(Tech.from_dict(i))
                updated_list.append(unlocked)
            with open ("techs/unlocked.json", "w") as unlock_file:
                json.dump([tech.to_dict() for tech in updated_list], unlock_file, indent =4)

    def get_slots(self):
        self.kTech = "techs/kTech.json"
        self.aTech = "techs/aTech.json"
        self.mTech = "techs/mTech.json"
        self.kFile = "inventory/equip/kEquip.json"
        self.aFile = "inventory/equip/aEquip.json"
        self.mFile = "inventory/equip/mEquip.json"
        with open (self.kFile, "r") as kfile:
            kdata = json.load(kfile)
            self.kw = kdata[0][0].get("slots")
            self.kwl = kdata[0][0].get("slot_link")
            self.ka = kdata[1][0].get("slots")
            self.kal = kdata[1][0].get("slot_link")
        with open (self.aFile, "r") as afile:
            adata = json.load(afile)
            self.aw = adata[0][0].get("slots")
            self.awl = adata[0][0].get("slot_link")
            self.aa = adata[1][0].get("slots")
            self.aal = adata[1][0].get("slot_link")
        with open (self.mFile, "r") as mfile:
            mdata = json.load(mfile)
            self.mw = mdata[0][0].get("slots")
            self.mwl = mdata[0][0].get("slot_link")
            self.ma = mdata[1][0].get("slots")
            self.mal = mdata[1][0].get("slot_link")
        print(self.kw,self.kwl,self.ka,self.kal,self.aw,self.awl,self.aa,self.aal,self.mw,self.mwl,self.ma,self.mal)


    def equip_techs(self):
        self.kw_slots = []
        self.ka_slots = []
        self.aw_slots = []
        self.aa_slots = []
        self.mw_slots = []
        self.ma_slots = []
        self.bane_list = []
        self.boon_list = []
        self.auto_list = []
        for tech in self.tdata:
            if tech.get("ttype") == "Bane":
                self.bane_list.append(tech)
            elif tech.get("ttype") == "Boon":
                self.boon_list.append(tech)
            else:
                self.auto_list.append(tech)
        print(self.bane_list)
        #for tech in self.bane_list:
            #bane_pwr = [Tech.BaneBoonTpwr.bb_from_dict(tech) for tech in self.bane_list]

    def slot_combo():
        pass

    """

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

flamethrowing_chip = Tech("Flame-Thrower", Tech.BaneBoonTpwr("Throw Flames: ", (40, 10), "Throw Flamier: ", (80, 14), "Throw Flamiest: ", (120, 18)).bb_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

atmospheric_condenser = Tech("Water Condenser", Tech.BaneBoonTpwr("Make It Rain: ", (40, 10), "Make It Rainier: ", (80, 14), "Make it Rainiest: ", (120, 18)).bb_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

hi_volt_discharger = Tech("Hi-Volt Discharger", Tech.BaneBoonTpwr("Lightning Strike: ", (40, 10), "Lightning Strikier: ", (80, 14), "Lightning Strikiest: ", (120, 18)).bb_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

freon_former = Tech("Freon Former", Tech.BaneBoonTpwr("Form Freon: ", (40, 10), "Form Freonier: ", (80, 14), "Formiest Freon: ", (120, 18)).bb_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

jet_turbine_chip = Tech("Jet Turbine", Tech.BaneBoonTpwr("Wind Blast: ", (50, 12), "Windier Blast: ", (100, 16), "Windiest Blast: ", (150, 20)).bb_to_dict(), 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

seismic_disruptor = Tech("Seismic Disruptor", Tech.BaneBoonTpwr("Disrupt Earth: ", (50, 12), "Disruptier Earth: ", (100, 16), "Disruptiest Earth: ", (150, 20)).bb_to_dict(), 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

light_of_ages = Tech("Light of the Ages", Tech.BaneBoonTpwr("Celestial Beam: ", (60, 14), "Holy Ray: ", (120, 18), "Light of Heaven: ", (180, 22)).bb_to_dict(), 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Bane").to_dict()

restore = Tech("Restore", Tech.BaneBoonTpwr("Restore Health: ", (40, 6), "Restore More: ", (80, 8), "Restore Most: ", (120, 10)).bb_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon").to_dict()

regen = Tech("Regenerate", Tech.BaneBoonTpwr("Regenerate Health: ", (10, 10), "Regenrate Health/Energy: ", (20, 20), "Regenerate Party: ", (20, 40)).bb_to_dict(), 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon").to_dict()

panacea = Tech("Cure Ailment", Tech.BaneBoonTpwr("Cure Minor Ail: ", (0, 8), "Cure Major Ail: ", (0, 12), "Panacea: ", (0, 20)).bb_to_dict(), 0, 1, 6000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon").to_dict()

overclock = Tech("Overclock", Tech.BaneBoonTpwr("Speed-Up: ", (1, 10), "Speed-Up All: ", (2, 15), "Super-Speed All: ", (3, 20)).bb_to_dict(), 0, 1, 7000, False, {False: "None", True: TechManager.slot_combo()}, False, "Boon").to_dict()

auto_cover = Tech("Cover Allies", Tech.AutoTpwr(False).a_to_dict(), 0, 1, 5000, False, {}, False, "Auto").to_dict()

auto_auto = Tech("Automate", Tech.AutoTpwr(False).a_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Auto").to_dict()

auto_link = Tech("Link", Tech.AutoTpwr(False).a_to_dict(), 0, 1, 5000, False, {False: "None", True: TechManager.slot_combo()}, False, "Auto").to_dict()

init_tech_list = [flamethrowing_chip, atmospheric_condenser, hi_volt_discharger, freon_former, jet_turbine_chip, seismic_disruptor, light_of_ages, restore, regen, panacea, overclock, auto_cover, auto_auto, auto_link]

tManager = TechManager()
tManager.create_techs(init_tech_list)
tManager.load_techs()
tManager.ck()
tManager.get_slots()
tManager.equip_techs()


"""
tManager.make_available("Flame-Thrower")
tManager.make_available("Water Condenser")

tname, tpwr, txp, tlv, txpcap, tmsr, tpaired, tavail
t = Tech()
"""
