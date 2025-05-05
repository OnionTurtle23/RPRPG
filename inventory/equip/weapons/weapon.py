import json

class Weapon:

    def __init__(self, wname, wtype, slots, slotLink, damage, isUnique, isAvail):
        self.wname = wname
        self.wtype = wtype
        self.slots = slots
        self.slotLink = slotLink
        self.damage = damage
        self.isUnique = isUnique
        self.isAvail = isAvail

    
    def weaponListed(name):
        print (name.wname)
        print ("Type: ",name.wtype)
        print ("Slots: ",name.slots)
        print ("Linked: ",name.slotLink)
        print ("Damage: ",name.damage)
        print ("Who Uses: ", name.isUnique)
        print ("Unlocked: ", name.isAvail)


    
    def weaponSaved(name):
        toSave = {
            "Name" : name.wname,
            "Type: " : name.wtype,
            "Slots: " : name.slots,
            "Linked: " : name.slotLink,
            "Damage: " : name.damage,
            "Who Uses: " : name.isUnique,
            "Unlocked: " : name.isAvail
           }
        return toSave




file = open("weaponlist.json","w")
file.write("[")
#weapons = json.load("weaponlist.json")
wtype = {
    "Normal" : "None",
    "Superheated" : "Fire",
    "Precipitative" : "Water",
    "Discharging" : "Electric",
    "Frostbitten" : "Ice",
    "Jet Turbined" : "Wind",
    "Seismic" : "Rock",
    "Ancient" : "Holy"
    }


    
basic_sword = Weapon("Basic Sword", "Normal", 3, 1, 20, "Kris", bool)
basic_staff = Weapon("Basic Staff", "Normal", 4, 2, 10, "Abigail", bool)
basic_pistol = Weapon("Basic Pistol", "Normal", 2, 1, 25, "Monte", bool)
fiery_scimitar = Weapon("Fiery Scimitar", "Superheated", 4, 2, 35, "Kris", bool)
rain_stick = Weapon("Rain Stick", "Precipitative", 5, 2, 25, "Abigail", bool)
electro_rifle = Weapon("Electro Rifle", "Discharging", 3, 1, 40, "Monte", bool)
masamune = Weapon("Masamune", "Frostbitten", 5, 2, 60, "Kris", bool)
hurricane_staff = Weapon("Huricane Staff", "Jet Turbined", 7, 3, 45, "Abigail", bool)
heavy_shotgun = Weapon("Heavy Shotgun", "Seismic", 5, 2, 70, "Monte", bool)
archangel_blade = Weapon("Archangel Blade", "Ancient", 8, 4, 100, "Kris", bool)
staff_of_the_prophets = Weapon("Staff of the Prophets", "Ancient", 8, 4, 100, "Abigail", bool)
judgement_day = Weapon("Judgement Day", "Ancient", 8, 4, 100, "Monte", bool)
charList = ["Kris", "Abigail", "Monte"]
weaponList = [basic_sword, basic_staff, basic_pistol, fiery_scimitar, rain_stick, electro_rifle, masamune, hurricane_staff, heavy_shotgun, archangel_blade, staff_of_the_prophets, judgement_day]
weaponInv = []

def weapInv():
    
    if len(weaponInv) == 0:
        print("Your inventory is sadly empty. . . go get stuff!")
    else:
        for i in weaponInv:
            print ("You currently have %s in inventory" % (i.wname))
 

def wunlock(weaponList):
    file.write("[")
    for i in weaponList:
        i.isAvail = True
        print("You have added the %s to your inventory" % (i.wname))
        save = Weapon.weaponSaved(i)
        json.dump(save, file, indent = 4)
        file.write(",")
    file.write("]")

wunlock(weaponList)
#for i in weaponInv:
 #   save = Weapons.weaponSaved(i)
  #  print(save)
#json.dump(Weapons.weaponSaved(i), file, indent = 4)
file.write("\n]")
file = open("weaponlist.json", "r")
check = json.load(file)
fileList = {}
for i in check:
    fileList.update({i: check[i]})

for i in fileList:
    print(i, fileList[i])

#def weapEquip():


