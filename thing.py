import json
import os
import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import inventory.equip.unique.unique as uniquemodule
import inventory.equip.equip as equipmodule

kFile = "inventory/equip/kEquip.json"

def pull():
    keq = []
    with open (kFile,"r") as kdata:
        keq = json.load(kdata)
        kw = keq[0][0].get("slots")
        kwl = keq[0][0].get("slot_link")
        ka = keq[1][0]
        #print(kw.get("slots"), kw.get("slot_link"))
        print(kw)
        print(ka)

pull()
