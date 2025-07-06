import random
from functools import reduce

from lists_and_dicts import *
from classes import *

# print(f"{weapon_elements["fire"]["symbol"]}")
# 
# element = weapon_elements["fire"]
# print(element)
# print(element["rarities"]["*"]) 


# def get_random_weapon():
    # luck = 100
    # if luck > 0:
        # random_value = random.random() + luck * 0.001 # Generates a float between 0 and 1
    # else:
        # random_value = random.random()
# 
    # if random_value < weapon_rarities["common"]["chance"]:
        # weapon = weapon_rarities["common"]
        # return weapon
        # 
    # elif random_value < weapon_rarities["uncommon"]["chance"] + weapon_rarities["common"]["chance"]:
        # weapon = weapon_rarities["uncommon"]
        # return weapon
        # 
    # elif random_value < weapon_rarities["rare"]["chance"] + weapon_rarities["uncommon"]["chance"] + weapon_rarities["common"]["chance"]:
    #    
        # weapon = weapon_rarities["rare"]
        # return weapon
        # 
    # elif random_value < weapon_rarities["epic"]["chance"] + weapon_rarities["rare"]["chance"] + weapon_rarities["uncommon"]["chance"] + weapon_rarities["common"]["chance"]:
        # 
        # weapon = weapon_rarities["epic"]
        # return weapon
        # 
    # elif random_value < weapon_rarities["legendary"]["chance"] + weapon_rarities["epic"]["chance"] + weapon_rarities["rare"]["chance"] + weapon_rarities["uncommon"]["chance"] + weapon_rarities["common"]["chance"]:
        #  
        # weapon = weapon_rarities["legendary"]
        # return weapon
        # 
    # else:
        ##This covers the case for "godly"
    #    
        # weapon = weapon_rarities["godly"]
        # return weapon
        
# common = 0
# uncommon = 0
# rare = 0
# epic = 0
# legendary = 0
# godly = 0
# weapons = []

# for i in range(1, 1001):
#     weapon = Weapon.get_random_weapon("random", "random", "random")
#     weapons.append(weapon)

# for weapon in weapons:
#     if weapon.weapon_rarity["name"] == "Common":
#         common += 1
#     if weapon.weapon_rarity["name"] == "Uncommon":
#         uncommon += 1
#     if weapon.weapon_rarity["name"] == "Rare":
#         rare += 1
#     if weapon.weapon_rarity["name"] == "Epic":
#         epic += 1
#     if weapon.weapon_rarity["name"] == "Legendary":
#         legendary += 1

# print(f"Common: {common/10}%\nUncommon: {uncommon/10}%\nRare: {rare/10}%\nEpic: {epic/10}%\nLegendary: {legendary/10}%\n")
#print(weapon)