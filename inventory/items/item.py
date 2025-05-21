import inventory.equip.weapons.weapon
import inventory.equip.armor.armor
import inventory.equip.unique.unique
import inventory.equip.equip
#import techs.tech
import json
import os

class Item:
    def __init__(self, iname, itype, qty = int):
        self.iname = iname
        self.itype = itype

    def to_dict(self):
        return {
                "iname": self.iname,
                "itype": self.itype,
                "qty": self.qty
                }

    @classmethod
    def from_dict(cls, data):
        return cls(
                data["iname"],
                data["itype"],
                data["qty"]
                )

class ItemManager:
    def __init__(self):
        self.ref_file = "inventory/items/ref.json"
        self.current = "inventory/current.json"
        self.wqty = {}
        self.aqty = {}
        self.uqty = {}
        self.tqty = {}

    def initial_inventory(self):
        with open ("inventory/equip/weapons/weaponlist.json", "r") as wlist:
            wdata = json.load(wlist)
            for w in wdata:
                wname = w.get("wname")
                avail = w.get("is_avail")
                if avail == True:
                    self.wqty.update({wname : 1})
            print(self.wqty)

        with open ("inventory/equip/armor/armorlist.json", "r") as alist:
            adata = json.load(alist)
            for a in adata:
                aname = a.get("aname")
                avail = a.get("is_avail")
                if avail == True:
                    self.aqty.update({aname : 1})
            print(self.aqty)

        with open ("inventory/equip/unique/uniquelist.json", "r") as ufile:
            udata = json.load(ufile)
            for u in udata:
                uname = u.get("uname")
                avail = u.get("is_avail")
                if avail == True:
                    self.uqty.update({uname: 1})
            print(self.uqty)

        with open ("techs/unlocked.json", "r") as tfile:
            tdata = json.load(tfile)
            for t in tdata:
                tname = t.get("tname")
                self.tqty.update({tname: 1})
            print(self.tqty)

        if not os.path.exists(self.current):
            with open (self.current, "w") as current:
                json.dump([self.wqty, self.aqty, self.uqty, self.tqty], current, indent = 4)
                print("Initial Inventory Created!")
        if not os.path.exists(self.ref_file):
            with open (self.ref_file, "w") as ref:
                json.dump([], ref)
                print("ref_file created")

    def inv_update(self):
        with open("inventory/equip/weapons/weaponlist.json", "r") as wfile, open("inventory/equip/armor/armorlist.json", "r") as afile, open("inventory/equip/unique/uniquelist.json", "r") as ufile, open("techs/unlocked.json", "r") as tfile, open("inventory/items/ref.json", "r") as ref, open("inventory/current.json", "r") as current:
            wdata = json.load(wfile)
            adata = json.load(afile)
            udata = json.load(ufile)
            tdata = json.load(tfile)
            rdata = json.load(ref)
            cdata = json.load(current)
            wlist = (w.get("wname") for w in wdata if w.get("is_avail")==True)
            alist = (a.get("aname") for a in adata if a.get("is_avail")==True)
            ulist = (u.get("uname") for u in udata if u.get("is_avail")==True)
            tlist = (t.get("tname") for t in tdata if t.get("is_avail")==True)
            print(cdata)

            """
            for w in wdata:
                wname = w.get("wname")
                avail = w.get("is_avail")
                if avail == True:
                    self.wqty.update({wname : 1})
            print(self.wqty)

"""



iManager = ItemManager()
iManager.initial_inventory()

