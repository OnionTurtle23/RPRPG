import inventory.equip.equip as equipmodule
import inventory.equip.weapons.weapon as weaponmodule
import party.char as charmodule
import enemies.enemy as enemymodule
import pygame as pg
import math
import json

class Battle:
    def __init__(self):
        self.chars = "party/active_party.json"
        self.k_gear = "inventory/equip/kEquip.json"
        self.a_gear = "inventory/equip/aEquip.json"
        self.m_gear = "inventory/equip/mEquip.json"
        self.encounter = "enemies/encounter.json"
        self.char_dict = []
        self.gear_dict = []
        self.enemy_dict = []
        self.char_info()
        self.gear_info()
        self.enemy_info()
        self.char_mods()

    def char_info(self):
        self.char_dict = []
        from party.char import PlayableCharacter, CharacterManager
        with open (self.chars, "r") as char_file:
            char_data = json.load(char_file)
            for char in char_data:
                self.char_dict.append(char)


    def gear_info(self):
        self.gear_dict = []
        from inventory.equip.weapons.weapon import Weapon, WeaponManager
        from inventory.equip.armor.armor import Armor, ArmorManager
        from inventory.equip.unique.unique import Unique, UniqueManager
        with open (self.k_gear, "r") as k_file:
            k_equip = json.load(k_file)
            for equipped in k_equip:
                self.gear_dict.append(equipped)
        with open (self.a_gear, "r") as a_file:
            a_equip = json.load(a_file)
            for equipped in a_equip:
                self.gear_dict.append(equipped)
        with open (self.m_gear, "r") as m_file:
            m_equip = json.load(m_file)
            for equipped in m_equip:
                self.gear_dict.append(equipped)


    def enemy_info(self):
        self.enemy_dict = []
        from enemies.enemy import Enemy, Enemy_chief, Beast, EnemyManager
        with open (self.encounter, "r") as encounter_file:
            enemies = json.load(encounter_file)
            for enemy in enemies:
                self.enemy_dict.append(enemy)

    def char_mods(self):
        kw = self.gear_dict[0][0]
        ka = self.gear_dict[0][1]
        ku = self.gear_dict[0][2]
        aw = self.gear_dict[1][0]
        aa = self.gear_dict[1][1]
        au = self.gear_dict[1][2]
        mw = self.gear_dict[2][0]
        ma = self.gear_dict[2][1]
        mu = self.gear_dict[2][2]


battle = Battle()
