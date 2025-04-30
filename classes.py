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
        self.ring = ring("Platzhalter-Ring", "ring", "Random ass test-ring", "rache", 0  )
        self.necklace = None
        self.vitality = player_class['vitality'] + self.ring.ring_vitality
        self.base_hp = player_class['hp'] 
        self.max_hp = player_class['hp']
        self.max_max_hp = self.max_hp * self.vitality
        self.hp = self.max_max_hp
        self.strength = player_class['strength']
        self.attack_damage = player_class['attack_damage']

    def player_attack(self, target, weapon):
        self.target = target
        final_damage_dealt = (self.attack_damage + weapon.weapon_damage) * self.strength
        target.hp -= final_damage_dealt
        print(f"{self.name} attackiert {target.name} und verursacht {final_damage_dealt} Schaden")
        print(f"{target.name} hat noch {target.hp} Leben!")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} hat {item} aufgenommen!")

    def show_inventory(self, which_items_to_show = None):
        """
        legal values for which_items_to_show:\n
        all, weapons, armor, rings, necklaces, consumables, \nweapons_armor_rings_necklaces
        """
        if which_items_to_show == "all":
            print(f"\nAlle Items im Inventar:")
            for idx, item in enumerate(self.inventory, start = 1):
                print(f"{idx}. {item}")
        elif which_items_to_show == "weapons":
            weapons_inventory = [item for item in self.inventory if isinstance(item, weapon)]
            print(f"\nWaffen im Inventar:")
            for idx, item in enumerate(weapons_inventory, start = 1):
                print(f"{idx}. {item}")
        elif which_items_to_show == "armor":    
            print(f"\nRüstungen im Inventar:")
            for idx, item in enumerate(self.inventory, start = 1):
                if isinstance(item, armor):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "rings":
            print(f"\nRinge im Inventar:")
            for idx, item in enumerate(self.inventory, start = 1):
                if isinstance(item, ring):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "necklaces":
            necklaces_inventory = [item for item in self.inventory if isinstance(item, necklace)]
            print(f"\nHalsketten im Inventar:")
            for idx, item in enumerate(necklaces_inventory, start = 1):
                if isinstance(item, necklace):
                    print(f"{idx}. {item}")
        elif which_items_to_show == "consumables":
            consumables_inventory = [item for item in self.inventory if isinstance(item, consumable)]
            print(f"\nVerbrauchbare Items im Inventar:")
            for idx, item in enumerate(consumables_inventory, start = 1):
                print(f"{idx}. {item}")
                return consumables_inventory
        elif which_items_to_show == "weapons_armor_rings_necklaces":
            equippable_inventory = [item for item in self.inventory if isinstance(item, weapon) or isinstance(item, armor) or isinstance(item, ring) or isinstance(item, necklace)]
            print(f"\nAusrüstungsgegenstände im Inventar:")
            for idx, item in enumerate(equippable_inventory, start = 1):
                print(f"{idx}. {item}")


        else:
            print("Dein Inventar ist leer")

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
            {'type': type(item).__name__, **vars(item)} for item in self.inventory  # Speichere Typ und Attribute
            ], 
            'weapon': vars(self.weapon) if self.weapon else None,  # Objekt in ein Dictionary umwandeln
            'armor': vars(self.armor) if self.armor else None,
            'ring': vars(self.ring) if self.ring else None,
            'necklace': vars(self.necklace) if self.necklace else None
        }
        with open(f"{self.name}_save.json", "w") as file:
            json.dump(save_data, file)

    @staticmethod
    def load_game(file_name):
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
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
                    item_type = item_data['type']  # Extrahiere den Typ des Items
                    
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
                        item = item(**item_data)  # Generische Basisklasse
                    player.inventory.append(item)
                
                player.weapon = weapon(**data['weapon']) if data['weapon'] else None  # Objekt aus Dictionary erstellen
                player.armor = armor(**data['armor']) if data['armor'] else None
                player.ring = ring(**data['ring']) if data['ring'] else None
                player.necklace = necklace(**data['necklace']) if data['necklace'] else None
                print(f"Spielstand von {player.name} wurde erfolgreich geladen!")
                return player
        else:
            print("Speicherstand nicht gefunden!")
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
        print(f"{self.name} attackiert {target.name} und verursacht {final_damage_dealt} Schaden")
        print(f"{target.name} hat noch {target.hp} Leben!")
    

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

items = {
    "Dolch": {"name": "Dolch", "type": "weapon", "item_info": "Ein kleiner Dolch, der gut in deine Tasche passt.", "weapon_type": "dolch", "weapon_damage": 4},
    "Kelch": {"name": "Kelch", "type": "item", "item_info": "Ein mysteriöser, goldener Kelch, den du gefunden hast."},
    "Ring des Abyss": {"name": "Ring des Abyss", "type": "ring", "item_info": "Dieser Ring strahlt eine Atmosphäre aus,\ndie alles um sich herum aufzusaugen scheint.. \ngruselig...", "ring_type": "abyss", "ring_vitality": 1.2},
}

items_from_chests = {
    "Dolch": {"name": "Dolch", "type": "weapon", "item_info": "Ein kleiner Dolch, der gut in deine Tasche passt.", "weapon_type": "dolch", "weapon_damage": 4},
    "Goldkelch": {"name": "Kelch", "type": "item", "item_info": "Ein mysteriöser, goldener Kelch, den du gefunden hast."},
    "Ring des Abyss": {"name": "Ring des Abyss", "type": "ring", "item_info": "Dieser Ring strahlt eine Atmosphäre aus,\ndie alles um sich herum aufzusaugen scheint.. \ngruselig...", "ring_type": "abyss", "ring_vitality": 1.2},
    "Scholle": {"name": "Scholle", "type": "weapon", "item_info": "Riecht ranzig, scheint aber niemals vergammeln zu können.", "weapon_type": "fisch", "weapon_damage": 15},
    "Großschwert": {"name": "Großschwert", "type": "weapon", "item_info": "Ein badass großes Schwert, dass dich befähigt,\ndeinen Feinden so richtig in den Hintern zu treten.", "weapon_type": "großschwert", "weapon_damage": 25},
    
}

def get_random_monster(monsters):
    which_monster = random.choice(list(monsters.values()))
    return which_monster

def get_random_item(items):
    which_item = random.choice(list(items.values()))
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