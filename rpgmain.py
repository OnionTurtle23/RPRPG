import inventory.equip.weapons.weapon as weaponmodule
import inventory.equip.armor.armor as armormodule
import inventory.equip.unique.unique as uniquemodule
import inventory.equip.equip as equipmodule
import party.char as charmodule
import techs.tech as tmobile
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


def add_outline_to_image(image: pygame.Surface, thickness: int, color: tuple, color_key: tuple = (255, 0, 255)) -> pygame.Surface:
    mask = pygame.mask.from_surface(image)
    mask_surf = mask.to_surface(setcolor=color)
    mask_surf.set_colorkey((0, 0, 0))

    new_img = pygame.Surface((image.get_width() + 2, image.get_height() + 2))
    new_img.fill(color_key)
    new_img.set_colorkey(color_key)

    for i in -thickness, thickness:
        new_img.blit(mask_surf, (i + thickness, thickness))
        new_img.blit(mask_surf, (thickness, i + thickness))
    new_img.blit(image, (thickness, thickness))

    return new_img
"""
text_surf = myfont.render("test", False, (255, 255, 255)).convert()
text_with_outline = add_outline_to_image(text_surf, 2, (0, 0, 0))
"""

screen_x, screen_y = screen.get_size()
scale_factor = 0.95
surface_width = int(screen_x * scale_factor)
surface_height = int(screen_y * scale_factor)


surface = pygame.Surface((surface_width, surface_height))
surface.fill("Silver")

surface_x = (screen_x - surface_width) // 2
surface_y = (screen_y - surface_height) // 2

title_font = pygame.font.Font("fonts/D3 Digitalism Italic.ttf", size = int(280*screen_y/screen_x))
title = title_font.render("R.P.R.P.G.", True, (0,255,0))
title_bg_img = pygame.image.load("images/title_bg.png")
title_w = floor(surface_width * .98)
title_h = floor(surface_height * .98)
title_bg_img = pygame.transform.scale(title_bg_img, (title_w, title_h))
title_x = floor(surface_x*1.4)
title_y = floor(surface_y*1.4)
title_text_x = floor((screen_x/4.5))
title_text_y = floor((screen_y/3.5))

press_x_font = pygame.font.Font("fonts/big_dots.ttf", size = int(160*screen_y/screen_x))
press_x_raw = press_x_font.render("Press    to start", False, (255,255,255)).convert()
press_x = add_outline_to_image(press_x_raw, 2, (0, 0, 0))
x_pressx = floor(screen_x*.27)
y_pressx = floor(screen_y*.81)
x_img = pygame.image.load("images/ps_x.png").convert()
x_img = pygame.transform.scale(x_img, (140,140)).convert_alpha()
x_ximg = floor(screen_x*.44)
y_ximg = floor(screen_y*.79)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        screen.blit(surface,(surface_x,surface_y))
        screen.blit(title_bg_img, (title_x,title_y))
        screen.blit(title, (title_text_x, title_text_y))
        screen.blit(press_x, (x_pressx,y_pressx))
        screen.blit(x_img, (x_ximg, y_ximg))
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

        print(f"Joystick {jid}")
        name = joystick.get_name()
        print(f"Joystick name: {name}")

        guid = joystick.get_guid()
        print(f"GUID: {guid}")

        power_level = joystick.get_power_level()
        print(f"Joystick's power level: {power_level}")

        axes = joystick.get_numaxes()
        print(f"Number of axes: {axes}")

        for i in range(axes):
            axis = joystick.get_axis(i)
            print(f"Axis {i} value: {axis:>6.3f}")

        buttons = joystick.get_numbuttons()
        print(f"Number of buttons: {buttons}")

        for i in range(buttons):
            button = joystick.get_button(i)
            print(f"Button {i:>2} value: {button}")

        hats = joystick.get_numhats()
        print(f"Number of hats: {hats}")

        for i in range(hats):
            hat = joystick.get_hat(i)
            print(f"Hat {i} value: {str(hat)}")
    pygame.display.flip()

    if joystick.get_button(0):
        pygame.quit()
        sys.exit()



"""
def generate_encounter():
    import enemies.enemy as basics
    basics.eManager.randEnc()



armormodule.aManager.aEquip("Basic Buckler", "Kris")
weaponmodule.wManager.unlock_weapon("Fiery Scimitar")
weaponmodule.wManager.wEquip("Fiery Scimitar")
uniquemodule.uManager.uEquip("Compact Cell", "Kris")
equipmodule.eManager.kEquip()

#armormodule.aManager.aEquip("Basic Leather", "Abigail")


charmodule.cManager.load_chars()
charmodule.cManager.save_party()
"""

