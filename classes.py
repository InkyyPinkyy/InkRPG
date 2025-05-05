import random
import os
import json

class Player:
    def __init__(self, name,player_class):
        self.name = name
        self.player_class = player_class
        self.name_of_player_class = player_class['name_of_player_class']
        
        self.skillpoints = 0
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.ring = None
        self.necklace = None
        self.vitality = player_class['vitality'] + self.ring.ring_vitality if self.ring else player_class['vitality']
        self.base_hp = player_class['hp'] 
        self.max_hp = player_class['hp']
        self.max_max_hp = self.max_hp * self.vitality
        self.hp = self.max_max_hp
        self.strength = player_class['strength']
        self.attack_damage = player_class['attack_damage']

        #settings, Quests and more:
        self.autosave_on = False

    def player_attack(self, target, weapon):
        self.target = target
        final_damage_dealt = (self.attack_damage + weapon.weapon_damage) * self.strength
        target.hp -= final_damage_dealt
        print(f"{self.name} attacks {target.name} and deals {final_damage_dealt} damage!")
        print(f"{target.name} still has {target.hp} HP!")

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
            print(f"{self.gold} Gold")            
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

    def save_game(self):
        save_data = {
            'name': self.name,
            'player_class': self.player_class,
            'name_of_player_class': self.name_of_player_class,
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
                player_class = data['player_class']
                player = Player(data['name'],player_class)
                player.name_of_player_class = data['name_of_player_class']
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
        
CLASSES = {
    "Elf" : {"name_of_player_class": "Elf", "hp": 110, "vitality": 1, "attack_damage": 18, "strength": 1.3},
    "Demon" : {"name_of_player_class": "Demon", "hp": 125, "vitality": 1, "attack_damage": 25, "strength": 1.5},
    "Dwarf" : {"name_of_player_class": "Dwarf", "hp": 150, "vitality": 1.3, "attack_damage": 15, "strength": 1.3},
    "Orc" : {"name_of_player_class": "Orc", "hp": 120, "vitality": 1, "attack_damage": 23, "strength": 1.5},
    "Human" : {"name_of_player_class": "Human", "hp": 100, "vitality": 1.5, "attack_damage": 20, "strength": 1},
    "Inchling" : {"name_of_player_class": "Inchling", "hp": 80, "vitality": 1.5, "attack_damage": 15, "strength": 1.5}
}

class Enemy:
    def __init__(self, which_monster):
        self.name = which_monster[str('name')]
        self.hp = which_monster['hp']
        self.max_hp = self.hp
        self.attack_damage = which_monster['attack_damage']

    def enemy_attack(self, target, weapon):
        self.target = target
        final_damage_dealt = (self.attack_damage + weapon.weapon_damage) * (Player.level * 0.7)
        target.hp -= final_damage_dealt
        print(f"{self.name} attacks {target.name} and deals {final_damage_dealt} damage!")
        print(f"{target.name} still has {target.hp} HP!")
    

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack_damage})"

monsters = {
    "Dragon" : {"name": "Dragon","hp": 220,"attack_damage": 25},
    "Skeleton" : {"name": "Skeleton","hp": 70,"attack_damage": 18},
    "Orc" : {"name": "Orc","hp": 170,"attack_damage": 20},
    "Phantom" : {"name": "Phantom","hp": 130,"attack_damage": 19},
    "Ghost" : {"name": "Ghost","hp": 120,"attack_damage": 15},
    "Zombie" : {"name": "Zombie","hp": 135,"attack_damage": 20},
    "Sheep" : {"name": "Sheep","hp": 30,"attack_damage": 10},
    "Bandit" : {"name": "Bandit","hp": 140,"attack_damage": 19}
}

dungeon_monsters = {
    "Mimic" : {"name": "Mimic", "hp": 180, "attack_damage": 30},
}

events = [
    "event_enemy_encounter",
    "event_wandering_trader_encounter",
    "event_player_finds_village",
    "event_player_finds_dungeon",
    "event_player_finds_random_house",
    "event_npc_encounter"
    "event_player_finds_ruins",
    "event_payer_finds_ancient_ruins",
    "event_player_finds_camp",
    "event_player_finds_hostile_camp",
    "event_player_random_thoughts",
    "event_bird_shits_on_player",
    "event_random_animal",
    "event_player_finds_farmhouse",
    "event_player_finds_abandoned_farmhouse",
    "event_player_finds_herb",
    "event_player_finds_city",
    "event_player_finds_npc_getting_attacked",


]

all_items = {
    "Dagger": {"name": "Dagger", "type": "weapon", "item_info": "A small dagger that is easy to carry.", "weapon_type": "daggger", "weapon_damage": 4},
    "Chalice": {"name": "Chalice", "type": "item", "item_info": "A mysterious, golden Chalice that you found."},
    "Ring of the abyss": {"name": "Ring of the abyss", "type": "ring", "item_info": "This ring is emitting an aura that seems \nto draw in everything around it. \ncreepy...", "ring_type": "abyss", "ring_vitality": 1.2},
    "Ghoti": {"name": "Fish", "type": "weapon", "item_info": "reeks disgusting, but seems to never rot", "weapon_type": "fish", "weapon_damage": 15},
    "GroßschwertGreatsword": {"name": "Greatsword", "type": "weapon", "item_info": "A badass sword that makes you look really cool.", "weapon_type": "greatsword", "weapon_damage": 25},

}

items_from_small_chests = {
    "Dagger": {"name": "Dagger", "type": "weapon", "item_info": "A small dagger that is easy to carry.", "weapon_type": "daggger", "weapon_damage": 4},
    "Chalice": {"name": "Chalice", "type": "item", "item_info": "A mysterious, golden Chalice that you found."},
    "Ring of the abyss": {"name": "Ring of the abyss", "type": "ring", "item_info": "This ring is emitting an aura that seems \nto draw in everything around it. \ncreepy...", "ring_type": "abyss", "ring_vitality": 1.2},
    "Ghoti": {"name": "Fish", "type": "weapon", "item_info": "reeks disgusting, but seems to never rot", "weapon_type": "fish", "weapon_damage": 15},
    "GroßschwertGreatsword": {"name": "Greatsword", "type": "weapon", "item_info": "A badass sword that makes you look really cool.", "weapon_type": "greatsword", "weapon_damage": 25},
    
}

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

class item:
    def __init__(self, name, type, item_info):
        self.name = name
        self.type = type
        self.item_info = str(item_info)

    def __str__(self):
        return f"{self.name} ({self.type}): \n{self.item_info}"
    
class weapon(item):
    def __init__(self, name, type, item_info, weapon_type, weapon_damage):
        super().__init__(name, type, item_info)
        self.weapon_type = weapon_type
        self.weapon_damage = weapon_damage

    def __str__(self):
        return f"{self.name} ({self.type}): {self.weapon_damage} Damage\n{self.item_info}"

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
        return f"{self.name} ({self.type}): {self.ring_vitality} Vitality\n{self.item_info}"

class necklace(item):
    def __init__(self, name, type, item_info, necklace_type, necklace_strength):
        super().__init__(name, type, item_info)
        self.armor_type = necklace_type
        self.armor_vitality = necklace_strength

    def __str__(self):
        return f"{self.name} ({self.type}): {self.necklace_type}: {self.necklace_strength}\n{self.item_info}"

class consumable(item):
    def __init__(self, name, type, item_info, consumable_type, stats_player_gets):
        super().__init__(name, type, item_info)
        self.consumable_type = consumable_type
        self.stats_player_gets = int(stats_player_gets)

    def __str__(self):
        return f"{self.name} ({self.type}): {self.stats_player_gets} HP\n{self.item_info}"