import pygame
import pygame_menu as pm
import techs.tech as tekmod
import json

pygame.init()

w,h = 450, 350
screen = pygame.display.set_mode((w,h))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

def tMenu():
    w,h = 450, 350
    screen2 = pygame.display.set_mode((w,h))
    m2 = pm.Menu("techs", width = w, height = h, theme=pm.themes.THEME_GREEN)
    def clicked():
        print("Hi")
    x = 1
    """
    if menu == "Weapons":
        x = 0
    elif menu == "Armor":
        x = 1
    else:
        x = 2
        """
    with open("inventory/current.json", "r") as current:
        inv = json.load(current)
        for i in inv[0]:
            button= m2.add.button(title = i, button_id = i)
            print(button.init.getattr(title))
            x += 1
            
    m2.add.button(title="Exit", action = pm.events.BACK, font_color=WHITE, background_color=RED)
    m2.mainloop(screen2)

def event():
    tekmod.tManager.create_slots_from_weapon("Kris", "w")

def testmenu():

    testM = pm.Menu(title = "testing", width = w, height = h, theme=pm.themes.THEME_GREEN)
    testM.add.button(title="Weapons", action= tMenu, font_color = WHITE, background_color = GREEN)
    testM.add.button(title="Armor", action= tMenu, font_color = WHITE, background_color = GREEN)
    testM.add.button(title="Unique", action= tMenu, font_color = WHITE, background_color = GREEN)

    testM.add.button(title="Exit", action=pm.events.EXIT,
                        font_color=WHITE, background_color=RED)
 

    testM.mainloop(screen)

if __name__ == "__main__":
    testmenu()
