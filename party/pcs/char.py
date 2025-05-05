import pygame
import math
import sys
sys.path.insert(0, '/Users/mz/Developer/git/new/RPRPG/inventory/equip/weapons/')
import weapon

class PlayableCharacter:

    # Character creation

    def __init__(self, name, sprite):

        self.name = name
        self.sprite = sprite
    # Stats: hit points, energy is MP,
    # stg (strength) is physical attack, 
    # ig (intelligence) tech attack strength
    # con (Constitution) adds to HP
    # wis (wisdom) addds to eng
    #pdef (physical defense) mitigates physical damage
    #tbar (tech barrier) mitigates tech damage
    #agi (Agility) increses ATB and dodge

    def stats(self, hp, eng, stg, ig, con, wis, pdef, tbar, agi):

        self.hp = hp
        self.eng = energy
        self.stg = strength
        self.ig = intel
        self.con = const
        self.wis = wisdom
        self.pdef = physDef
        self.tbar = techBar
        self.agi = agility

    #Equipment inherits from the item class, modifies stats and adds abilties

    #def equipped():

print(basic_sword)
