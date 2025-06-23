SPECIES = {
    "Elf" : {"name_of_player_species": "Elf", "hp": 110, "vitality": 1, "attack_damage": 18, "strength": 1.3},
    "Demon" : {"name_of_player_species": "Demon", "hp": 125, "vitality": 1, "attack_damage": 25, "strength": 1.5},
    "Dwarf" : {"name_of_player_species": "Dwarf", "hp": 150, "vitality": 1.3, "attack_damage": 15, "strength": 1.3},
    "Orc" : {"name_of_player_species": "Orc", "hp": 120, "vitality": 1, "attack_damage": 23, "strength": 1.5},
    "Human" : {"name_of_player_species": "Human", "hp": 100, "vitality": 1.5, "attack_damage": 20, "strength": 1},
    "Inchling" : {"name_of_player_species": "Inchling", "hp": 80, "vitality": 1.5, "attack_damage": 15, "strength": 1.5}
}

monster_species = {

    # Ground-type
    "Goblin" : {
        "general_spawn_chance": 0.1,
        "mob_type": "ground",
        "subclasses": {
            "normal_goblin": {"name": "Goblin", "base_damage": 7, "base_hp": 50, "highest_armor_tier": 2, "highest_weapon_rarity": "**", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "hobgoblin": {"name": "Hobgoblin", "base_damage": 20, "base_hp": 80, "highest_armor_tier": 4, "highest_weapon_rarity": "****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "goblin_brute": {"name": "Goblin Brute", "base_damage": 30, "base_hp": 100, "highest_armor_tier": 5, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.15, "rank": 3, "can_be_found_where": []},
            "goblin_king": {"name": "Goblin King", "base_damage": 50, "base_hp": 300, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 4, "can_be_found_where": []},
            },
        },
    "Orc": {
        "general_spawn_chance": 0.1, #TODO: When doing the calculation for the enemy damage, it will look at the rank. For explanation: Since Monsters a re getting stronger with the player, I want lower-rank mobs to get stronger slower so the player gtes something for his work; maybe one-shot possible
        "mob_type": "ground",
        "subclasses": {
            "normal_orc": {"name": "Orc", "base_damage": 16, "base_hp": 80, "highest_armor_tier": 2, "highest_weapon_rarity": "**", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "brave_orc_youngling": {"name": "Orc Youngling", "base_damage": 25, "base_hp": 95, "highest_armor_tier": 3, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "head_of_orc_tribe": {"name": "Head of Orc tribe", "base_damage": 80, "base_hp": 350, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.1, "rank": 3, "can_be_found_where": []},
            },
        },
    "Sheep" : {
        "general_spawn_chance": 0.1,
        "mob_type": "ground",
        "subclasses": {
            "baby_sheep": {"name": "Baby Sheep", "base_damage": 3, "base_hp": 20, "highest_armor_tier": None, "highest_weapon_rarity": None, "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 1, "can_be_found_where": []},
            "normal_sheep": {"name": "Sheep", "base_damage": 5, "base_hp": 30, "highest_armor_tier": None, "highest_weapon_rarity": None, "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 2, "can_be_found_where": []},
            "big_chongus_sheep": {"name": "Big Sheep", "base_damage": 10, "base_hp": 50, "highest_armor_tier": None, "highest_weapon_rarity": None, "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.14, "rank": 3, "can_be_found_where": []},
            "angry_magical_sheep": {"name": "Angry Magical Sheep", "base_damage": 6, "base_hp": 300, "highest_armor_tier": None, "highest_weapon_rarity": None, "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 4, "can_be_found_where": []},
            "unicorn_sheep": {"name": "Unicorn Sheep", "base_damage": 7, "base_hp": 150, "highest_armor_tier": None, "highest_weapon_rarity": None, "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.01, "rank": 5, "can_be_found_where": []},
            },
        },
    "Bandit": {
        "general_spawn_chance": 0.1,
        "mob_type": "ground",
        "subclasses": {
            "bandit": {"name": "Bandit", "base_damage": 10, "base_hp": 60, "highest_armor_tier": 2, "highest_weapon_rarity": "**", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "bandit_leader": {"name": "Bandit Leader", "base_damage": 30, "base_hp": 100, "highest_armor_tier": 4, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "bandit_warlord": {"name": "Bandit Warlord", "base_damage": 50, "base_hp": 200, "highest_armor_tier": 5, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.15, "rank": 3, "can_be_found_where": []},
            "bandit_king": {"name": "Bandit King", "base_damage": 80, "base_hp": 400, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 4, "can_be_found_where": []},
            },
        },
    "Mimic": {
        "general_spawn_chance": 0.1,
        "mob_type": "ground",
        "subclasses": {
            "tiny_mimic": {"name": "Tiny Mimic", "base_damage": 5, "base_hp": 30, "highest_armor_tier": 1, "highest_weapon_rarity": "*", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.2, "rank": 1, "can_be_found_where": []},
            "normal_mimc": {"name": "Mimic", "base_damage": 15, "base_hp": 80, "highest_armor_tier": 3, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 2, "can_be_found_where": []},
            "legendary_mimic": {"name": "Legendary Mimic", "base_damage": 40, "base_hp": 200, "highest_armor_tier": 5, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.25, "rank": 3, "can_be_found_where": []},
            "ancient_mimic": {"name": "Ancient Mimic", "base_damage": 70, "base_hp": 500, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 4, "can_be_found_where": []},
            
            },
        },
    # multiple mob types
    "Zombie" : {
        "general_spawn_chance": 0.1,
        "mob_type": ["ground", "magic"],
        "subclasses": {
            "baby_zombie": {"name": "Baby Zombie", "base_damage": 5, "base_hp": 40, "highest_armor_tier": 1, "highest_weapon_rarity": "*", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "zombie": {"name": "Zombie", "base_damage": 9, "base_hp": 85, "highest_armor_tier": 3, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "zombie_soldier": {"name": "Zombie Soldier", "base_damage": 30, "base_hp": 110, "highest_armor_tier": 5, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.15, "rank": 3, "can_be_found_where": []},
            "queen_of_the_undead": {"name": "Queen of the undead", "base_damage": 60, "base_hp": 350, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 3, "can_be_found_where": []},
            },
        },
    "Skeleton": {
        "general_spawn_chance": 0.1,
        "mob_type": ["ground", "magic"],
        "subclasses": {
            "normal_skeleton": {"name": "Skeleton", "base_damage": 8, "base_hp": 60, "highest_armor_tier": 3, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "skeleton_guard": {"name": "Skeleton Guard", "base_damage": 25, "base_hp": 90, "highest_armor_tier": 5, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "queen_of_the_undead": {"name": "Queen of the undead", "base_damage": 60, "base_hp": 350, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.2, "rank": 3, "can_be_found_where": []},
            },
        },
    "Dragon": {
        "general_spawn_chance": 0.1,
        "mob_type": ["air", "ground", "magic"],
        "subclasses": {
            "baby_dragon": {"name": "Baby Dragon", "base_damage": 15, "base_hp": 100, "highest_armor_tier": 2, "highest_weapon_rarity": "**", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "young_dragon": {"name": "Young Dragon", "base_damage": 30, "base_hp": 200, "highest_armor_tier": 4, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            "adult_dragon": {"name": "Adult Dragon", "base_damage": 60, "base_hp": 400, "highest_armor_tier": 6, "highest_weapon_rarity": "*****", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.15, "rank": 3, "can_be_found_where": []},
            "ancient_dragon": {"name": "Ancient Dragon", "base_damage": 100, "base_hp": 800, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.05, "rank": 4, "can_be_found_where": []},
            },
        },

    # magic-type
    "Phantom": {
        "general_spawn_chance": 0.1,
        "mob_type": "magic",
        "subclasses": {
            "phantom": {"name": "Phantom", "base_damage": 10, "base_hp": 70, "highest_armor_tier": 3, "highest_weapon_rarity": "***", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.5, "rank": 1, "can_be_found_where": []},
            "phantom_warrior": {"name": "Phantom Warrior", "base_damage": 25, "base_hp": 120, "highest_armor_tier": 6, "highest_weapon_rarity": "⋈", "material_drop_chances": {}, "weapon_and_armor_drop_chances": {}, "spawn_chance": 0.3, "rank": 2, "can_be_found_where": []},
            },
        },
    }

monsters = {
    #"Dragon" : {"name": "Dragon","hp": 220,"attack_damage": 25},
    #"Skeleton" : {"name": "Skeleton","hp": 70,"attack_damage": 18},
    #"Orc" : {"name": "Orc","hp": 170,"attack_damage": 20},
    +"Phantom" : {"name": "Phantom","hp": 130,"attack_damage": 19},
    "Ghost" : {"name": "Ghost","hp": 120,"attack_damage": 15},
    #"Zombie" : {"name": "Zombie","hp": 135,"attack_damage": 20},
    #"Sheep" : {"name": "Sheep","hp": 30,"attack_damage": 10},
    #"Bandit" : {"name": "Bandit","hp": 140,"attack_damage": 19}
}

dungeon_monsters = {
    "Mimic" : {"name": "Mimic", "hp": 180, "attack_damage": 30},
}

weapon_types = {

    # Ground weapons

    "dagger": {"type_name": "Dagger", 
               "strength_required": 0.5, 
               "base_chance_to_fail": 0.05, 
               "base_damage_on_rarity": {"*":5, "**":10, "***":15, "****":20, "*****":25, "⋈":40}, 
               "base_durability_on_rarity": {"*":50, "**":75, "***":100, "****":125, "*****":150, "⋈":250}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },
    "sword": {"type_name": "Sword", 
               "strength_required": 0.8, 
               "base_chance_to_fail": 0.07, 
               "base_damage_on_rarity": {"*":7, "**":14, "***":21, "****":28, "*****":35, "⋈":55}, 
               "base_durability_on_rarity": {"*":55, "**":80, "***":105, "****":130, "*****":155, "⋈":255}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },
    "greatsword": {"type_name": "Greatsword", 
                   "strength_required": 1.7, 
                   "base_chance_to_fail": 0.1, 
                   "base_damage_on_rarity": {"*":10, "**":20, "***":30, "****":40, "*****":50, "⋈":80}, 
                   "base_durability_on_rarity": {"*":60, "**":90, "***":120, "****":150, "*****":180, "⋈":300}, 
                   "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
                   "preferred_mob_type": "ground", 
                   },
    "axe": {"type_name": "Axe", 
               "strength_required": 1.5, 
               "base_chance_to_fail": 0.08, 
               "base_damage_on_rarity": {"*":8, "**":16, "***":24, "****":32, "*****":40, "⋈":65}, 
               "base_durability_on_rarity": {"*":60, "**":80, "***":105, "****":130, "*****":155, "⋈":255}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },

    # Ranged weapons

    "bow": {"type_name": "Bow", 
            "strength_required": 1.0, 
            "base_chance_to_fail": 0.15,

            # Damage is low because that is just for the bow itself, the true damage comes from the arrows used later on. 
            "base_damage_on_rarity": {"*":4, "**":8, "***":12, "****":16, "*****":20, "⋈":30}, 
            
            "base_durability_on_rarity": {"*":40, "**":60, "***":80, "****":100, "*****":120, "⋈":200}, 
            "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
            "preferred_mob_type": "air", 
            },
    "crossbow": {"type_name": "Crossbow", 
                 "strength_required": 1.2, 
                 "base_chance_to_fail": 0.12, 
                 
                 # Damage is low because that is just for the crossbow itself, the true damage comes from the arrows used later on. 
                 "base_damage_on_rarity": {"*":6, "**":12, "***":18, "****":24, "*****":30, "⋈":45}, 
                 
                 "base_durability_on_rarity": {"*":50, "**":70, "***":90, "****":110, "*****":130, "⋈":220}, 
                 "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
                 "preferred_mob_type": "air", 
                 },
    "spear": {"type_name": "Spear",
               "strength_required": 1.2, 
               "base_chance_to_fail": 0.09, 
               "base_damage_on_rarity": {"*":7, "**":14, "***":21, "****":28, "*****":35, "⋈":60}, 
               "base_durability_on_rarity": {"*":55, "**":75, "***":100, "****":125, "*****":150, "⋈":250}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "air", 
               },

    # Magic weapons

    "staff": {"type_name": "Staff", 
              "strength_required": 0.7, 
              "base_chance_to_fail": 0.1, 
              "base_damage_on_rarity": {"*":8, "**":16, "***":24, "****":32, "*****":40, "⋈":65}, 
              "base_durability_on_rarity": {"*":50, "**":60, "***":70, "****":90, "*****":110, "⋈":200}, 
              "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
              "preferred_mob_type": "magic", 
              },
    
    # hydrophile

    "trident": {"type_name": "Trident",
               "strength_required": 1.2, 
               "base_chance_to_fail": 0.1, 
               "base_damage_on_rarity": {"*":9, "**":18, "***":27, "****":36, "*****":45, "⋈":75}, 
               "base_durability_on_rarity": {"*":55, "**":75, "***":100, "****":125, "*****":150, "⋈":250}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "hydrophile",     
                },

    # special weapons

    "fish": {"type_name": "Fish",
               "strength_required": 0.4, 
               "base_chance_to_fail": 0.01, 
               "base_damage_on_rarity": {"*":2, "**":4, "***":6, "****":8, "*****":10, "⋈":20}, 
               "base_durability_on_rarity": {"*":20, "**":45, "***":60, "****":85, "*****":100, "⋈":150}, 
               "gemstone_slots_on_rarity": {"*":1, "**":2, "***":2, "****":3, "*****":4, "⋈":5},
               "preferred_mob_type": "ground", 
               },

}

weapon_rarities = {
    "common": {"name": "Common", "symbol": "*", "chance": 0.44, "pcolors_string": ''},
    "uncommon": {"name": "Uncommon", "symbol": "**", "chance": 0.26, "pcolors_string": '\033[92m'},
    "rare": {"name": "Rare", "symbol": "***", "chance": 0.16, "pcolors_string": '\033[94m'},
    "epic": {"name": "Epic", "symbol": "****", "chance": 0.11, "pcolors_string": '\033[95m'},
    "legendary": {"name": "Legendary", "symbol": "*****", "chance": 0.03, "pcolors_string": '\033[93m'},
    "godly": {"name": "Godly", "symbol": "⋈", "pcolors_string": '\033[91m'}
}

#   ^—-^    
# (_='.')  


# ≈≋ 
# ≡
# ⊛
# ⊰⊰
# ⋇
# ⊹
# ⋯⋱⋮⋰
# ⁕
# · ‥ ⁖ ⁘ ⁙  
# ⁜※◬
# ◜◝◟◞
# ⊙⨀⊚◎◉◯
# ◸◹◺◿◤◥◣◢
# ⨌
# ⨫⨬
# ⨳
# ⩬
# ⫞⫟⫠
# ‹«›»
# ←↖↑↗→↘↓↙
# 🌑🌒🌓🌔🌕🌖🌗🌘
# ⭐🌊🌠🌟⭐
# 1️2️⃣3️⃣4️⃣5️
# 🔈🔉🔊
# 
weapon_elements = {

    "fire": {"symbol": "🔥" ,"rarities": {"*":"Fire", "**":"Flame", "***":"Inferno", "****":"Hellfire", "*****":"Phoenix Flame", "⋈":"Cinderheart"}, "possible_enchantments":"fire_enchantments", "good_against": [], "bad_against": []},
    "water": {"symbol": "💧", "rarities": {"*":"Water", "**":"Tide", "***":"Flood", "****":"Maelstrom", "*****":"Leviathan's Wrath", "⋈":"Poseidon's Nemesis"}, "possible_enchantments":"water_enchantments", "good_against": [], "bad_against": []},
    "earth": {"symbol": "🌍", "rarities": {"*":"Earth", "**":"Stone", "***":"Quake", "****":"Terraforce", "*****":"Worldbreaker", "⋈":"Primordial Core"}, "possible_enchantments":"earth_enchantments", "good_against": [], "bad_against": []},
    "wind": {"symbol":"💨", "rarities": {"*":"Wind", "**":"Gust", "***":"Storm", "****":"Tempest", "*****":"Skywrath", "⋈":"Breath of Aeons"}, "possible_enchantments":"wind_enchantments", "good_against": [], "bad_against": []},
    "ice": {"symbol": "❄", "rarities": {"*":"Ice", "**":"Frost", "***":"Glacier", "****":"Frostbite", "*****":"Permafrost", "⋈":"Winter's Grave"}, "possible_enchantments":"ice_enchantments", "good_against": [], "bad_against": []},
    "spark": {"symbol": "⚡", "rarities": {"*":"Spark", "**":"Bolt", "***":"Thunder", "****":"Storm", "*****":"Stormcaller", "⋈":"Skyfire"}, "possible_enchantments":"spark_enchantments", "good_against": [], "bad_against": []},
    "blood": {"symbol": "🩸", "rarities": {"*":"Blood", "**":"Crimson", "***":"Bloodfang", "****":"red curse", "*****":"Crimson Requiem", "⋈":"Thirst of the forgotten"}, "possible_enchantments":"blood_enchantments", "good_against": [], "bad_against": []},
    "shadow": {"symbol": "👥", "rarities": {"*":"Shadow", "**":"Void", "***":"Abyss", "****":"Endless Chaos", "*****":"The Nothingness", "⋈":"Khaos' Pain"}, "possible_enchantments":"shadow_enchantments", "good_against": [], "bad_against": []},
    "light": {"symbol": "🔆", "rarities": {"*":"Light", "**":"Radiant", "***":"Gleam", "****":"Lumina", "*****":"Celestia", "⋈":"Halo of Judgement"}, "possible_enchantments":"light_enchantments", "good_against": [], "bad_against": []},
    "toxin": {"symbol": "☣", "rarities": {"*":"Toxin", "**":"Venom", "***":"Plague", "****":"Rotfang", "*****":"Pestilence", "⋈":"Serpent's Kiss"}, "possible_enchantments":"toxin_enchantments", "good_against": [], "bad_against": []},
    "iron": {"symbol": "🔩", "rarities": {"*":"Iron", "**":"Steel", "***":"Mithril", "****":"Adamant", "*****":"Godsteel", "⋈":"Starforged"}, "possible_enchantments":"iron_enchantments", "good_against": [], "bad_against": []},
    "magic": {"symbol": "🔮", "rarities": {"*":"Magic", "**":"Mana", "***":"Arcana", "****":"Spellfire", "*****":"Runeblade", "⋈":"Aetherial Wonder"}, "possible_enchantments":"iron_enchantments", "good_against": [], "bad_against": []},
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