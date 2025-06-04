import random
import os
import json

#from events import *
from dungeon import *
from lists_and_dicts import *

class pcolors: # print-colors
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    BACKGROUND_CYAN = '\033[46m'
    BACKGROUND_PURPLE = '\033[45m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_RED = '\033[41m'
    
    DARK_CYAN = '\033[36m'
    DARK_PURPLE = '\033[35m'
    DARK_BLUE = '\033[34m'
    DARK_YELLOW = '\033[33m'
    DARK_GREEN = '\033[32m'
    DARK_RED = '\033[31m'

    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player:
    def __init__(self, name,player_species):
        self.name = name
        self.player_species = player_species
        self.name_of_player_species = player_species['name_of_player_species']
        
        self.skillpoints = 0
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.ring = None
        self.necklace = None
        self.vitality = player_species['vitality'] + self.ring.ring_vitality if self.ring else player_species['vitality']
        self.base_hp = player_species['hp'] 
        self.max_hp = player_species['hp']
        self.max_max_hp = self.max_hp * self.vitality
        self.hp = self.max_max_hp
        self.strength = player_species['strength']
        self.attack_damage = player_species['attack_damage']

        #settings, Quests and more:
        self.autosave_on = False

    def show_player_stats(self):
        """shows the player's stats"""
        print(f"\n{self.name}'s stats:")
        print(f"Class: {self.name_of_player_species}")
        print(f"{round(self.hp)}/{round(self.max_max_hp)} HP")
        print(f"Damage: {round((self.attack_damage + self.weapon.weapon_damage) * self.strength)}")
        print(f"Your weapon: {self.weapon}")
        print(f"Your armor: {self.armor}")
        print(f"Your ring: {self.ring}")
        print(f"Your necklace: {self.necklace}")
        print(f"Your level: {self.level}")
        print(f"{self.xp}/{self.level * 32} XP until the next level")
        print(f"{self.skillpoints} skillpoints")

    def check_amount_self_xp(self):
        while self.xp >= (self.level * 32):
            self.xp -= (self.level * 32)
            self.level += 1
            self.skillpoints += 1
            self.max_max_hp += 5
            self.hp = self.max_max_hp        
            print(f"You reached level {self.level} and got a skillpoint!")
            print(f"Your max HP increased by 5!")
            print(f"Your hp had been restored!")

    def go_to_settings(self):
        """shows the settings menu"""
        print(f"\nSettings:")
        print(f"1. Change autosave on/off")
        print(f"2. exit settings")
    
        choice = input("Choice: ")
    
        if choice == '1':
            self.autosave_on = not self.autosave_on
            print(f"Autosave is now {'on' if self.autosave_on else 'off'}")
        elif choice == '2':
            return
        else:
            print(f"Invalid choice!")
            return

    def player_attack(self, target):
        try: damage = random.uniform(
            ((self.attack_damage + self.weapon.weapon_damage) * self.strength) * 0.9,
            ((self.attack_damage + self.weapon.weapon_damage) * self.strength) * 1.1
            )
        except: damage = random.uniform(
            ((self.attack_damage) * self.strength) * 0.9,
            ((self.attack_damage) * self.strength) * 1.1
            )
        target.hp -= round(damage)
        # (f"{damage:.2f
        print(f"You are dealing {round(damage)} damage to the {target.name}!")
        if target.hp > 0:
            damage = random.uniform(
            target.attack_damage * self.strength * 0.5,
            target.attack_damage * self.strength * 0.7
        )
            self.hp -= round(damage)
            print(f"The target is dealing {round(damage)} damage to you!")

    def enemy_encounter(self, enemy):
        """
        initialises a battle with the player and an enemy.
        There is an option to flee, where the fight gets
        cancelled. The damage of the enemy scales with
        the players strength.
        """
        print(f"\nA {enemy.name} is attacking you!")

        while self.hp > 0 and enemy.hp > 0:
            print(f"\n{self.name}: {self.hp}/{self.max_max_hp} HP")
            print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP")

            action = input("Attack (a) or flee (f)? ")
            if action.lower() == 'a':
                self.player_attack(enemy)

            elif action.lower() == 'f':
                print("You fled!")
                return

        if self.hp > 0:
            print(f"You won gainst the {enemy.name}!")
            gold_earned = random.randint(10, 20)
            self.gold += gold_earned
            print(f"You got {gold_earned} gold!")
            xp_earned = random.randint(enemy.max_hp // 10, enemy.max_hp // 3)
            self.xp += xp_earned
            print(f"You  got {xp_earned} XP!")
            self.check_amount_self_xp()

        else:
            print("You lost...")
            exit()

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}!")

    def show_inventory(self, which_items_to_show = None):
        """
        legal values for which_items_to_show:\n
        - "everything": all items in the inventory\n
        - "weapons": only weapons in the inventory\n
        - "armor": all the armor in the inventory\n
        - "rings": all the rings in the inventory\n
        - "necklaces": all the necklaces in the inventory\n
        - "consumables": all the consumable items in the inventory\n
        - "weapons_armor_rings_necklaces": all the equippable items in the inventory\n
        """
        if which_items_to_show == "everything":
            print(f"\nYour inventory:")
            print(f"{pcolors.YELLOW}{self.gold}{pcolors.END} Gold")            
            for idx, item in enumerate(self.inventory, start = 1):
                print(f"{idx}. {item}")
        elif which_items_to_show == "weapons":
            weapons_inventory = [item for item in self.inventory if isinstance(item, weapon)]
            print(f"\nYour weapons:")
            for idx, item in enumerate(weapons_inventory, start = 1):
                print(f"{idx}. {item}")
        elif which_items_to_show == "armor":    
            print(f"\nYour armor-sets:")
            for idx, item in enumerate(self.inventory, start = 1):
                if isinstance(item, armor):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "rings":
            print(f"\nYour rings:")
            for idx, item in enumerate(self.inventory, start = 1):
                if isinstance(item, ring):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "necklaces":
            necklaces_inventory = [item for item in self.inventory if isinstance(item, necklace)]
            print(f"\nYour necklaces:")
            for idx, item in enumerate(necklaces_inventory, start = 1):
                if isinstance(item, necklace):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "consumables":
            consumables_inventory = [item for item in self.inventory if isinstance(item, consumable)]
            print(f"\nYour consumable items:")
            for idx, item in enumerate(consumables_inventory, start = 1):
                print(f"{idx}. {item}")
                return consumables_inventory
        elif which_items_to_show == "weapons_armor_rings_necklaces":
            equippable_inventory = [item for item in self.inventory if isinstance(item, weapon) or isinstance(item, armor) or isinstance(item, ring) or isinstance(item, necklace)]
            print(f"\nEquippable items:")
            for idx, item in enumerate(equippable_inventory, start = 1):
                print(f"{idx}. {item}")
        else:
            print("Your inventory is empty!")

    def choose_equipment(self):
        self.show_inventory("weapons_armor_rings_necklaces")        
        print(f"Choose an item to equip")

        try:
            wahl = int(input(f"\nProvide the number of the item you want to equip: ")) -1
            if 0 <= wahl < len(self.inventory):
                item = self.inventory[wahl]
                if item.type == "weapon":
                    self.weapon = item
                    print(f"{self.name} equipped '{item.name}' as their weapon!")
                elif item.type == "armor":
                    self.armor = item
                    print(f"{self.name} equipped '{item.name}' as their armor!")
                elif item.type == "ring":
                    self.ring = item
                    print(f"{self.name} equipped '{item.name}' as their ring!")
                elif item.type == "necklace":
                    self.necklace = item
                    print(f"{self.name} equipped '{item.name}' as their necklace!")
                else:
                    print(f"This item can't be equipped!")
            else:
                print(f"invalid selection")
        except ValueError:
            print(f"Please provide a valid number")

    def consume_item(self):
        consumable_items = self.show_inventory("consumables")
        wahl = input(f"\nProvide the number of the item you want to consume or exit (e) ")
        if wahl.lower() == 'e':
            return
        try: 
            wahl -= 1       
            item = consumable_items[wahl]
            if 0 <= wahl < len(self.inventory):
                if item.consumable_type == "health":
                    if self.hp == self.max_max_hp:
                        print(f"{self.name} is already at max HP!")
                        return
                    elif self.hp + item.stats_self_gets > self.max_max_hp:
                        item.stats_self_gets = self.max_max_hp - self.hp
                        self.hp += item.stats_self_gets
                    else:
                        self.hp += item.stats_self_gets
                    print(f"{self.name} consumed {item.name} and got {item.stats_self_gets} HP!")
                    self.inventory.remove(item)
                elif item.consumable_type == "strength":
                    self.strength += item.stats_self_gets
                    print(f"{self.name} consumed {item.name} and got {item.stats_self_gets} strength!")
                    self.inventory.remove(item)
                elif item.consumable_type == "increase_max_health":
                    self.max_hp += item.stats_self_gets
                    print(f"{self.name} consumed {item.name} and got additional {item.stats_self_gets} max HP!")
                    self.inventory.remove(item)
                elif item.consumable_type == "increase_attack_damage":
                    self.attack_damage += item.stats_self_gets
                    print(f"{self.name} consumed {item.name} and got additional {item.stats_self_gets} strength!")
                    self.inventory.remove(item)
            else:
                return
        except ValueError:
            print(f"Please provide a valid number")
            return

    def do_inventory_shit(self):
        self.show_inventory("everything")
        action = input("\nEquip item (1), consume item (2) or return (3)? ")
        if action.lower() == '1':
            self.choose_equipment()
        elif action.lower() == '2':
            self.consume_item()
        elif action.lower() == '3':
            return

    def save_game(self):
        save_data = {
            'name': self.name,
            'player_species': self.player_species,
            'name_of_player_species': self.name_of_player_species,
            'hp': self.hp, 
            'max_hp': self.max_hp, 
            'vitality': self.vitality, 
            'strength': self.strength, 
            'attack_damage': self.attack_damage,
            'skillpoints': self.skillpoints, 
            'level': self.level, 
            'xp': self.xp, 
            'gold': self.gold, 
            'inventory': [
            {'type': type(item).__name__, **vars(item)} for item in self.inventory  # Save all items in the inventory converted to dicts
            ], 
            'weapon': vars(self.weapon) if self.weapon else None,  # object to dict
            'armor': vars(self.armor) if self.armor else None,
            'ring': vars(self.ring) if self.ring else None,
            'necklace': vars(self.necklace) if self.necklace else None
        }
        with open(f"{self.name}_save.json", "w") as file:
            json.dump(save_data, file)
        
        settings_data = {
            'autosave_on' : self.autosave_on,
        }
        with open(f"{self.name}_settings.json", "w") as file:
            json.dump(settings_data, file)

    @staticmethod
    def load_game(player_file_name, settings_file_name):
        if os.path.exists(player_file_name) and os.path.exists(settings_file_name):
            with open(player_file_name, "r") as file:
                data = json.load(file)
                player_species = data['player_species']
                player = Player(data['name'],player_species)
                player.name_of_player_species = data['name_of_player_species']
                player.hp = data['hp']
                player.max_hp = data['max_hp']
                player.vitality = data['vitality']
                player.strength = data['strength']
                player.attack_damage = data['attack_damage']
                player.level = data['level']
                player.xp = data['xp']
                player.gold = data['gold']

                player.inventory = []
                for item_data in data['inventory']:
                    item_type = item_data['type']
                    
                    if item_type == 'weapon':
                        item = weapon(**item_data)
                    elif item_type == 'armor':
                        item = armor(**item_data)
                    elif item_type == 'ring':
                        item = ring(**item_data)
                    elif item_type == 'necklace':
                        item = necklace(**item_data)
                    elif item_type == 'consumable':
                        item = consumable(**item_data)
                    else:
                        item = item(**item_data)
                    player.inventory.append(item)
                
                player.weapon = weapon(**data['weapon']) if data['weapon'] else None  # dict to object
                player.armor = armor(**data['armor']) if data['armor'] else None
                player.ring = ring(**data['ring']) if data['ring'] else None
                player.necklace = necklace(**data['necklace']) if data['necklace'] else None
                print(f"Game-file of {player.name} was succesfully loaded!")
                return player
            with open(settings_file_name, "r") as file:
                data = json.load(file)
                self.autosave_on = data['autosave_on']
                print(f"Settings-file of {player.name} was succesfully loaded!")
        else:
            # mention of the not existing file is in main() function
            return None

class NPC:
    def __init__(self, which_npc):
        self.name = which_npc[str('name')]
        self.species_name = which_npc['species_name']
        # same as player-races
        self.profession = which_npc['profession']

        self.profession_specialization = which_npc['profession_specialization']
        self.hp = which_npc['hp']
        self.max_hp = self.hp

        self.inventory = []

class Merchant(NPC):
    def __init__(self, which_merchant):
        super().__init__(which_merchant)
        self.gold = which_merchant['gold']
        self.items_for_sale = which_merchant['items_for_sale']
        self.items_to_buy = which_merchant['items_to_buy']

    def show_items_for_sale(self):
        print(f"\n{self.name}'s items for sale:")
        for idx, item in enumerate(self.items_for_sale, start = 1):
            print(f"{idx}. {item}")
    
    def show_items_to_buy(self):
        print(f"\n{self.name}'s items to buy:")
        for idx, item in enumerate(self.items_to_buy, start = 1):
            print(f"{idx}. {item}")

class Enemy:
    def __init__(self, which_monster):
        self.name = which_monster[str('name')]
        self.hp = which_monster['hp']
        self.max_hp = self.hp
        self.attack_damage = which_monster['attack_damage']

    def get_random_monster(which_monster):
        """
        valid values for which_monster:\n
        - "normal": monsters for enemy_encounter()\n
        - "dungeon": dungeon monsters\n
        """
        if which_monster == "normal":
            monster = random.choice(list(monsters.values()))
        elif which_monster == "dungeon":
            monster = random.choice(list(dungeon_monsters.values()))
        return monster

    def enemy_attack(self, target, weapon):
        self.target = target
        final_damage_dealt = (self.attack_damage + weapon.weapon_damage) * (Player.level * 0.7)
        target.hp -= final_damage_dealt
        print(f"{self.name} attacks {target.name} and deals {final_damage_dealt} damage!")
        print(f"{target.name} still has {target.hp} HP!")
    

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack_damage})"

class item:
    def __init__(self, name, type, item_info):
        self.name = name
        self.type = type
        self.item_info = str(item_info)

    def __str__(self):
        return f"{self.name} ({self.type}): \n  {self.item_info}"
    
    def get_random_item(which_items):
        """
        valid values for which_items:\n
        - "from_big_pool": all items in the game\n
        - "small_chest": items from small chests\n
        """
        if which_items == "from_big_pool":
            which_item = random.choice(list(all_items.values()))
        if which_items == "small_chest":
            which_item = random.choice(list(items_from_small_chests.values()))
        return which_item
    
    
    
class weapon(item):
    """legal values for weapon_type:\n
            - "dagger"\n
            - "sword"\n
            - "greatsword"\n
            - "fish"\n
            - "axe"\n
            - "spear"\n
            - "bow"\n
            - "crossbow"\n
            - "trident"\n
            - "staff"\n

        legal values for weapon_rarity:\n
            - "common"
            - "uncommon"
            - "rare"
            - "epic"
            - "legendary"
            - "godly"

        legal values for weapon_element:\n
            - "fire"
            - "water"
            - "earth"
            - "wind"
            - "ice"
            - "spark"
            - "blood"
            - "shadow"
            - "light"
            - "toxin"
            - "iron"
            - "magic"
    """
    def __init__(self, name, type, item_info, weapon_type, weapon_rarity, weapon_element, weapon_damage, enchantments = None):
        super().__init__(name, type, item_info)
        self.weapon_type = weapon_type

        self.weapon_type_name = weapon_type.capitalize()
        self.strength_required = 0
        self.base_chance_to_fail = 0
        self.base_damage_on_rarity = {}
        self.base_durability_on_rarity = {}
        self.gemstone_slots_on_rarity = {}
        self.preferred_mob_type = None # ranged, ground, hydrophile or magical
        
        self.weapon_rarity = {}
        self.weapon_element = {}
        self.weapon_damage = weapon_damage
        self.enchantments = [] 
        self.IsEnabled = True

    def __str__(self):
        return f"{self.name} ({self.weapon_type}): {self.weapon_damage} Damage\n    {self.item_info}"

class armor(item):
    def __init__(self, name, type, item_info, armor_type, armor_vitality):
        super().__init__(name, type, item_info)
        self.armor_type = armor_type
        self.armor_vitality = armor_vitality

class ring(item):
    def __init__(self, name, type, item_info, ring_type, ring_vitality):
        super().__init__(name, type, item_info)
        self.ring_type = ring_type
        self.ring_vitality = ring_vitality

    def __str__(self):
        return f"{self.name} ({self.type}): {self.ring_vitality} Vitality\n    {self.item_info}"

class necklace(item):
    def __init__(self, name, type, item_info, necklace_type, necklace_strength):
        super().__init__(name, type, item_info)
        self.armor_type = necklace_type
        self.armor_vitality = necklace_strength

    def __str__(self):
        return f"{self.name} ({self.type}): {self.necklace_type}: {self.necklace_strength}\n    {self.item_info}"

class consumable(item):
    def __init__(self, name, type, item_info, consumable_type, stats_player_gets):
        super().__init__(name, type, item_info)
        self.consumable_type = consumable_type
        self.stats_player_gets = int(stats_player_gets)

    def __str__(self):
        return f"{self.name} ({self.type}): {self.stats_player_gets} HP\n   {self.item_info}"