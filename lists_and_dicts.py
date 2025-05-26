CLASSES = {
    "Elf" : {"name_of_player_class": "Elf", "hp": 110, "vitality": 1, "attack_damage": 18, "strength": 1.3},
    "Demon" : {"name_of_player_class": "Demon", "hp": 125, "vitality": 1, "attack_damage": 25, "strength": 1.5},
    "Dwarf" : {"name_of_player_class": "Dwarf", "hp": 150, "vitality": 1.3, "attack_damage": 15, "strength": 1.3},
    "Orc" : {"name_of_player_class": "Orc", "hp": 120, "vitality": 1, "attack_damage": 23, "strength": 1.5},
    "Human" : {"name_of_player_class": "Human", "hp": 100, "vitality": 1.5, "attack_damage": 20, "strength": 1},
    "Inchling" : {"name_of_player_class": "Inchling", "hp": 80, "vitality": 1.5, "attack_damage": 15, "strength": 1.5}
}

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

weapon_types = {
    
}



weapon_rarities = {
    "common": {"name": "Common", "symbol": "*", "chance": 0.5},
    "uncommon": {"name": "Uncommon", "symbol": "**", "chance": 0.3},
    "rare": {"name": "Rare", "symbol": "***", "chance": 0.15},
    "epic": {"name": "Epic", "symbol": "****", "chance": 0.1},
    "legendary": {"name": "Legendary", "symbol": "*****", "chance": 0.05},
    "godly": {"name": "Godly", "symbol": "⋈", "chance": 0.01}
}

weapon_elements = {

    "fire": {"rarities": {"*":"Fire", "**":"Flame", "***":"Inferno", "****":"Hellfire", "*****":"Phoenix Flame", "⋈":"Cinderheart"}, "possible_enchantments":"fire_enchantments", "good_against": [], "bad_against": []},
    "water": {"rarities": {"*":"Water", "**":"Tide", "***":"Flood", "****":"Maelstrom", "*****":"Leviathan's Wrath", "⋈":"Poseidon's Nemesis"}, "possible_enchantments":"water_enchantments", "good_against": [], "bad_against": []},
    "earth": {"rarities": {"*":"Earth", "**":"Stone", "***":"Quake", "****":"Terraforce", "*****":"Worldbreaker", "⋈":"Primordial Core"}, "possible_enchantments":"earth_enchantments", "good_against": [], "bad_against": []},
    "wind": {"rarities": {"*":"Wind", "**":"Gust", "***":"Storm", "****":"Tempest", "*****":"Skywrath", "⋈":"Breath of Aeons"}, "possible_enchantments":"wind_enchantments", "good_against": [], "bad_against": []},
    "ice": {"rarities": {"*":"Ice", "**":"Frost", "***":"Glacier", "****":"Frostbite", "*****":"Permafrost", "⋈":"Winter's Grave"}, "possible_enchantments":"ice_enchantments", "good_against": [], "bad_against": []},
    "spark": {"rarities": {"*":"Spark", "**":"Bolt", "***":"Thunder", "****":"Storm", "*****":"Stormcaller", "⋈":"Skyfire"}, "possible_enchantments":"spark_enchantments", "good_against": [], "bad_against": []},
    "blood": {"rarities": {"*":"Blood", "**":"Crimson", "***":"Bloodfang", "****":"red curse", "*****":"Crimson Requiem", "⋈":"Thirst of the forgotten"}, "possible_enchantments":"blood_enchantments", "good_against": [], "bad_against": []},
    "shadow": {"rarities": {"*":"Shadow", "**":"Void", "***":"Abyss", "****":"Endless Chaos", "*****":"The Nothingness", "⋈":"Khaos' Pain"}, "possible_enchantments":"shadow_enchantments", "good_against": [], "bad_against": []},
    "light": {"rarities": {"*":"Light", "**":"Radiant", "***":"Gleam", "****":"Lumina", "*****":"Celestia", "⋈":"Halo of Judgement"}, "possible_enchantments":"light_enchantments", "good_against": [], "bad_against": []},
    "toxin": {"rarities": {"*":"Toxin", "**":"Venom", "***":"Plague", "****":"Rotfang", "*****":"Pestilence", "⋈":"Serpent's Kiss"}, "possible_enchantments":"toxin_enchantments", "good_against": [], "bad_against": []},
    "iron": {"rarities": {"*":"Iron", "**":"Steel", "***":"Mithril", "****":"Adamant", "*****":"Godsteel", "⋈":"Starforged"}, "possible_enchantments":"iron_enchantments", "good_against": [], "bad_against": []},
    "magic": {"rarities": {"*":"Magic", "**":"Mana", "***":"Arcana", "****":"Spellfire", "*****":"Runeblade", "⋈":"Aetherial Wonder"}, "possible_enchantments":"iron_enchantments", "good_against": [], "bad_against": []},
}


all_items = {
    "Dagger": {"name": "Dagger", "type": "weapon", "item_info": "A small dagger that is easy to carry.", "weapon_type": "dagger", "weapon_damage": 4},
    "Chalice": {"name": "Chalice", "type": "item", "item_info": "A mysterious, golden Chalice that you found."},
    "Ring of the abyss": {"name": "Ring of the abyss", "type": "ring", "item_info": "This ring is emitting an aura that seems \nto draw in everything around it. \ncreepy...", "ring_type": "abyss", "ring_vitality": 1.2},
    "Ghoti": {"name": "Fish", "type": "weapon", "item_info": "reeks disgusting, but seems to never rot", "weapon_type": "fish", "weapon_damage": 15},
    "Greatsword": {"name": "Greatsword", "type": "weapon", "item_info": "A badass sword that makes you look really cool.", "weapon_type": "greatsword", "weapon_damage": 25},
    "Healing Potion": {"name": "Healing Potion", "type": "consumable", "item_info": "A potion that heals you for 50 HP.", "consumable_type": "health", "stats_player_gets": 50},
}

items_from_small_chests = {
    "Dagger": {"name": "Dagger", "type": "weapon", "item_info": "A small dagger that is easy to carry.", "weapon_type": "dagger", "weapon_damage": 4},
    "Chalice": {"name": "Chalice", "type": "item", "item_info": "A mysterious, golden Chalice that you found."},
    "Ring of the abyss": {"name": "Ring of the abyss", "type": "ring", "item_info": "This ring is emitting an aura that seems \nto draw in everything around it. \ncreepy...", "ring_type": "abyss", "ring_vitality": 1.2},
    "Ghoti": {"name": "Fish", "type": "weapon", "item_info": "reeks disgusting, but seems to never rot", "weapon_type": "fish", "weapon_damage": 15},
    "Greatsword": {"name": "Greatsword", "type": "weapon", "item_info": "A badass sword that makes you look really cool.", "weapon_type": "greatsword", "weapon_damage": 25},
    
}