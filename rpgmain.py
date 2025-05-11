import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import inventory.equip.unique.unique as uniquemodule
import inventory.equip.equip as equipmodule
import party.char as charmodule
from inventory.equip.weapons.weapon import Weapon
from inventory.equip.armor.armor import Armor
from inventory.equip.unique.unique import Unique
from enemies.enemy import Enemy, Enemy_chief, Beast
from party.char import PlayableCharacter
import json
import sys
from pathlib import Path
import pygame
from math import floor


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("RPRPG")
clock = pygame.time.Clock()
joysticks = {}
display_width, display_height = screen.get_size()
scale_factor = 0.95
surface_width = int(display_width * scale_factor)
surface_height = int(display_height * scale_factor)


surface = pygame.Surface((surface_width, surface_height))
surface.fill("Silver")

surface_x = (display_width - surface_width) // 2
surface_y = (display_height - surface_height) // 2

title_font = pygame.font.Font("fonts/D3 Digitalism Italic.ttf", size = int(280*display_height/display_width))
title = title_font.render("R.P.R.P.G.", True, (0,255,0))
title_bg_img = pygame.image.load("images/title_bg.png")
title_w = floor(surface_width * .98)
title_h = floor(surface_height * .98)
title_bg_img = pygame.transform.scale(title_bg_img, (title_w, title_h))
title_x = floor(surface_x*1.4)
title_y = floor(surface_y*1.4)
title_text_x = floor((display_width/4.5))
title_text_y = floor((display_height/3.5))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(surface,(surface_x,surface_y))
        screen.blit(title_bg_img, (title_x,title_y))
        screen.blit(title, (title_text_x, title_text_y))
        pygame.display.update()
        clock.tick(60)

        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            if event.button == 0:
                joystick = joysticks[event.instance_id]
                if joystick.rumble(0, 0.7, 500):
                    print(f"Rumble effect played on joystick {event.instance_id}")

        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_instance_id()} connencted")

        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]
            print(f"Joystick {event.instance_id} disconnected")
    joystick_count = pygame.joystick.get_count()

    for joystick in joysticks.values():
        jid = joystick.get_instance_id()

        text_print.tprint(screen, f"Joystick {jid}")
        text_print.indent()

            # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        text_print.tprint(screen, f"Joystick name: {name}")

        guid = joystick.get_guid()
        text_print.tprint(screen, f"GUID: {guid}")

        power_level = joystick.get_power_level()
        text_print.tprint(screen, f"Joystick's power level: {power_level}")

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
        axes = joystick.get_numaxes()
        text_print.tprint(screen, f"Number of axes: {axes}")
        text_print.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
        text_print.unindent()

        buttons = joystick.get_numbuttons()
        text_print.tprint(screen, f"Number of buttons: {buttons}")
        text_print.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            text_print.tprint(screen, f"Button {i:>2} value: {button}")
        text_print.unindent()

        hats = joystick.get_numhats()
        text_print.tprint(screen, f"Number of hats: {hats}")
        text_print.indent()

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
        text_print.unindent()

        text_print.unindent()

        # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



"""
def generate_encounter():
    import enemies.enemy as basics
    basics.eManager.randEnc()



armormodule.aManager.aEquip("Basic Buckler", "Kris")
weaponmodule.wManager.unlock_weapon("Fiery Scimitar")
weaponmodule.wManager.wEquip("Fiery Scimitar")
uniquemodule.uManager.uEquip("Compact Cell", "Kris")
equipmodule.eManager.kEquip()

#armormodule.aManager.aEquip("Basi Leather", "Abigail")


charmodule.cManager.load_chars()
charmodule.cManager.save_party()
"""

