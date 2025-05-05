import pygame
import json
import random


class PlayableCharacter:

    # Character creation

    def __init__(self, name, sprite, hp, eng, stg, ig, con, wis, pdef, tbar, agi):

        self.name = name
        self.sprite = sprite
        self.hp = hp
        self.eng = eng
        self.stg = stg
        self.ig = ig
        self.con = con
        self.wis = wis
        self.pdef = pdef
        self.tbar = tbar
        self.agi = agi

    #Equipment inherits from the item class, modifies stats and adds abilties
kSprite = pygame.image.load("kris.png")
kris = PlayableCharacter("Kris", kSprite, 100, 20, 10, 8, 9, 7, 8, 8, 8)

class Equipment:

    def __init__(self, Weapon, Armor, Unique):
        pass


class Enemy:

    def __init__(self, name, hp, eng, atk, tech, isAlive):
        self.name = name
        self.hp = hp
        self.eng = eng
        self.atk = atk
        self.tech = tech
        self.isAlive = isAlive


goblin = Enemy("Goblin", 50, 10, 5, "None", bool)
gob_chief = Enemy("Goblin Chief", 80, 20, 10, "Fire", bool)
enemyList = [goblin, gob_chief]

def randEnc():
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    a = random.choice(enemyList)
    a = a.name
    b = random.choice(enemyList)
    b = b.name
    if a == b:
        z = x + y
        print ("You encounter %s %ss" % (z, a))
    elif x == 0:
        if y > 1:
            print("You encounter %s %ss" % (y, a))
        else:
            print("You encounter %s %s" % (y, a))
    elif y == 0:
        if x > 1:
            print("You encounter %s %ss" % (x, a))
        else:
            print("You encounter %s %s" % (x, a))
    else:
        if x > 1 and y > 1:
            print ("you encounter %s %ss, and %s %ss" % (x, a, y, b))
        elif x > 1 and y == 1:
            print ("You encounter %s %ss, and %s %s" % (x, a, y, b))
        elif x ==1 and y > 1:
            print ("You encounter %s %s, and %s %ss" % (x, a, y, b))
        else:
            print ("You encounter %s %s, and %s %s" % (x, a, y, b))



randEnc()
randEnc()
randEnc()
randEnc()
randEnc()




#weaponInv = []






#def weapInv():
    
    #if len(weaponInv) == 0:
        #print("Your inventory is sadly empty. . . go get stuff!")
    #else:
        #for i in weaponInv:
            #print ("You currently have %s in inventory" % (i.wname))
 

#def wunlock(weaponList):
    #file.write("[")
    #for i in weaponList:
        #i.isAvail = True
        #print("You have added the %s to your inventory" % (i.wname))
        #save = Weapon.weaponSaved(i)
        #json.dump(save, file, indent = 4)
        #file.write(",")
    #file.write("]")

#wunlock(weaponList)
#for i in weaponInv:
 #   save = Weapons.weaponSaved(i)
  #  print(save)
#json.dump(Weapons.weaponSaved(i), file, indent = 4)
#file.write("\n]")
#file = open("weaponlist.json", "r")
#check = json.load(file)
#fileList = {}
#for i in check:
    #fileList.update({i: check[i]})

#for i in fileList:
    #print(i, fileList[i])

#def weapEquip():

