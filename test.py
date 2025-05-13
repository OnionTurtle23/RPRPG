import math
from math import floor
import techs.tech as tmobile

"""two ways to calc xp req modifier"""
"""
x = floor(19 / 10)
print(x)
y = (20 // 10)
print(y)
xp21 = (((y+75) * (21**2))//10)
print(xp21)
xp22 = (((y+75) * (22**2))//10)
print(xp22)
print(xp21 + xp22)


z = (9 - 10) // 2
print(z)

def test():
    x_modifier = 68
    current_lvl = 1
    for current_lvl in range(1,100):
        lvmod = ((current_lvl - 2) // 10) * 10 + 2
        lvdiff = abs(current_lvl - lvmod)
        #print(f" lv mod: {lvmod}, lv diff: {lvdiff}")
        x_modifier = ((current_lvl // 10) + 68)
        current = 0
        #print(f"current lvl: {current_lvl}, xmod: {x_modifier}")
        xp_needed_to_lvl = (((x_modifier * (current_lvl + 1)** 2) // 10))
        #print(f"xp needed for calc: {xp_needed_to_lvl}")
        current += xp_needed_to_lvl
        #print(f"current + next = {current + xp_needed_to_lvl}")
        next = current + (current + xp_needed_to_lvl)
        #print(f"xp needed total for lvl {current_lvl}: {next}")
        #print(next+next)

        x = floor((100*(current_lvl**2)) - 100*current_lvl + (current_lvl * x_modifier * (current_lvl -1)))
        print(f" to get to level {current_lvl +1}: {x} XP required")
def stat_adj():
    sample_stat = [200, 95, 15, 18, 20, 12, 22]
    slist = []
    lv = 1
    for stat in sample_stat:
        stat = (stat**2 - (lv*stat) + stat)
        slist.append(stat)
    print(slist)


def ck():
    n = 110
    for i in range(1,100):
        n += floor(-1*math.log10(i)+10.95)
        print (f"lvl {i}: {n}")

ck()
"""

