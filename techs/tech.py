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
        self.ktech = "techs/ktech.json"
        self.atech = "techs/atech.json"
        self.mtech = "techs/mtech.json"

    class Equipped:
        def __init__(self, gear_slots, linked_slots):
            self.gear_slots = gear_slots
            self.linked_slots = linked_slots

        def to_dict(self):
            return {
                "gear_slots": self.gear_slots,
                "linked_slots": self.linked_slots
                }
        @classmethod
        def from_dict(cls, data):
            return cls(
                data["gear_slots"],
                data["linked_slots"]
                )

            
    class AssignedSlots:
        def __init__(self, t1 = None, t2 = None, t3 = None, t4 = None, t5 = None, t6 = None, t7 = None, t8 = None):
            self.t1 = t1
            self.t2 = t2
            self.t3 = t3
            self.t4 = t4
            self.t5 = t5
            self.t6 = t6
            self.t7 = t7
            self.t8 = t8

        def to_dict(self):
            return {
                "t1": self.t1,
                "t2": self.t2,
                "t3": self.t3,
                "t4": self.t4,
                "t5": self.t5,
                "t6": self.t6,
                "t7": self.t7,
                "t8": self.t8
                }

        @classmethod
        def from_dict(cls, data):
            return cls(
                data.get("t1"),
                data.get("t2"),
                data.get("t3"),
                data.get("t4"),
                data.get("t5"),
                data.get("t6"),
                data.get("t7"),
                data.get("t8")
                )

        def remove_from_slot(self, slot):
            if hasattr(self, slot):
                setattr(self, slot, None)

    class LinkedSlots:
        def __init__(self, lt1a = None, lt1b = None, lt2a = None, lt2b = None, lt3a = None, lt3b = None, lt4a = None, lt4b = None):
            self.lt1a = lt1a
            self.lt1b = lt1b
            self.lt2a = lt2a
            self.lt2b = lt2b
            self.lt3a = lt3a
            self.lt3b = lt3b
            self.lt4a = lt4a
            self.lt4b = lt4b
            
        def to_dict(self):
            return {
                "lt1a": self.lt1a,
                "lt1b": self.lt1b,
                "lt2a": self.lt2a,
                "lt2b": self.lt2b,
                "lt3a": self.lt3a,
                "lt3b": self.lt3b,
                "lt4a": self.lt4a,
                "lt4b": self.lt4b
                }

        @classmethod
        def from_dict(cls, data):
            return cls(
                data["lt1a"],
                data["lt1b"],
                data["lt2a"],
                data["lt2b"],
                data["lt3a"],
                data["lt3b"],
                data["lt4a"],
                data["lt4b"]
                )

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
        if not os.path.exists(self.ktech or self.atech or self.mtech):
            with open (self.ktech, "w") as k, open(self.atech, "w") as a, open(self.mtech, "w") as m:
                json.dump([],k)
                json.dump([],a)
                json.dump([],m)

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
            with open ("techs/unlocked.json", "a") as unlock_file:
                json.dump([tech.to_dict() for tech in updated_list], unlock_file, indent =4)
            with open("inventory/current.json", "r") as cfile:
                cdata = json.load(cfile)
                try:
                    qty = cdata[3].get(updated_list[0].tname) + 1
                except:
                    qty = 1
                cdata[3].update({updated_list[0].tname: qty})
                with open("inventory/current.json", "w") as cfile:
                    json.dump(cdata, cfile, indent = 2)


    def get_slots(self):
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
        #print(self.kw,self.kwl,self.ka,self.kal,self.aw,self.awl,self.aa,self.aal,self.mw,self.mwl,self.ma,self.mal)
    def assign_tech_to_slot(self, selected, slot):
        inv = "inventory/current.json"
        with open(inv,"r") as inv:
            data = json.load(inv)
            if [selected == i for i in data[3]]:
                self.slot_dict.update({slot:selected})
    def assign_linked(self):
        x = 1
        y = 1
        z = 2
        n = 0
        lst = self.slot_dict.values()
        for i in lst:
            if str(i) == "None":
                pass
            else:
                n += 1
        print('\n',self.slot_dict)
        print(self.ldict)
        for i in range(1, int(n)):
            try:
                self.ldict.update({f"lt{x}a":self.slot_dict.get(f"t{y}")})
                self.ldict.update({f"lt{x}b":self.slot_dict.get(f"t{z}")})
            except:
                pass
            x += 1
            y += 2
            z += 2
        print(self.ldict)

    def create_slots_from_weapon(self):
        slots = TechManager.AssignedSlots()
        self.slot_dict = {}
        self.ldict = {}
        TechManager.get_slots(self)
        if self.char == "Kris":
            snum = self.kw+1
            lnum = self.kwl*2
        elif self.char == "Abigail":
            snum = self.aw+1
            lnum = self.awl*2
        else:
            snum = self.mw+1
            lnum = self.mwl*2

        for i in range(1, snum):
            self.slot_dict[f"t{i}"] = None
        print(self.slot_dict)
        for i in range(1, lnum+1):
             if i % 2 == 0:
                l = "b"
             else:
                l = "a"
             if i <= 2:
                self.ldict[f"lt1{l}"]= None
             if i > 2 and i < 5:
                self.ldict[f"lt2{l}"]= None
             if i > 4 and i < 7:
                self.ldict[f"lt3{l}"]= None
             if i >= 7:
                self.ldict[f"lt4{l}"]= None
        print(self.ldict)


    def equip_techs(self, char, w_or_a):
        self.kTech = "techs/kTech.json"
        self.aTech = "techs/aTech.json"
        self.mTech = "techs/mTech.json"
        self.char = char
        if not os.path.exists(self.kTech and self.aTech and self.mTech):
            with open(self.kTech, "w") as ktek, open(self.aTech, "w") as atek, open(self.mTech, "w") as mtek:
                json.dump([], ktek)
                json.dump([], atek)
                json.dump([], mtek)
        self.kw_slots = {}
        self.ka_slots = {}
        self.aw_slots = {}
        self.aa_slots = {}
        self.mw_slots = {}
        self.ma_slots = {}
        if self.char == "Kris":
            with open(self.kTech, "r") as ktek:
                ksdata = json.load(ktek)
                if w_or_a == "w":
                    TechManager.create_slots_from_weapon(self)
                    TechManager.assign_tech_to_slot(self, "Flame-Thrower", "t1")
                    TechManager.assign_tech_to_slot(self, "Water Condenser", "t2")
                    TechManager.assign_tech_to_slot(self, "Flame-Thrower", "t3")
                    TechManager.assign_linked(self)
                    print("\n\n", self.slot_dict)
                    check = [i for i in self.slot_dict.values()]
                    print(check)
                    new_item = TechManager.Equipped(self.slot_dict, self.ldict)
                    print('\n', new_item.to_dict())
                    #if len(duo) != self.kwl and rw_slots > 0 and link =="y":
                     #   self.kw_slots.update({tech_to_slot: slot_num})
                    #else:
                     #   print("Slots Full")

                elif w_or_a == "a":
                    try: 
                        self.ka_slots = ksdata[1]
                        ra_slots = self.ka - (len(ksdata[1]))

                        if ra_slots > 0:
                            self.ka_slots.update({tech_to_slot: slot_num})
                        else:
                            print("Slots Full")
                    except:
                        self.ka_slots.update({tech_to_slot: slot_num})
                
                with open(self.kTech, "w") as ktek:
                    json.dump(new_item.to_dict(), ktek)
        """
Equipped = {"gear_slots" : {"exist": Weapon.slots, "assigned" : {in_slot_int: jutsu, in_slot_int: link}, "remain": self.sdict.get("exist") - len(self.sdict.get("assigned")}, "linked":{jutsu0:justu1}}

        if to_whom == "Kris":
            with open(self.kTech, "r") as ktek:
                kcurrent = json.load(ktek)
      """          


    def slot_combo():
        pass



"""
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
"""

            

tManager.create_slots_from_weapon("Kris")

#assign_tech_to_slot("Flame-Thrower", 1)

tManager.get_slots()
"""
tManager.equip_techs("Kris", "w")
"""
tManager.assign_tech_to_slot(("Flame-Thrower", "Water Condenser"))

tManager.make_available("Water Condenser")


tManager.create_techs(init_tech_list)
tManager.load_techs()
tManager.ck()

tManager.make_available("Flame-Thrower")


tname, tpwr, txp, tlv, txpcap, tmsr, tpaired, tavail
t = Tech()
"""
