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

    # Ground weapons

    "dagger": {"type_name": "Dagger", 
               "strength_required": 0.5, 
               "base_chance_to_fail": 0.05, 
               "base_physical_damage_on_rarity": {"*":5, "**":10, "***":15, "****":20, "*****":25, "⋈":40}, 
               "base_durability_on_rarity": {"*":50, "**":75, "***":100, "****":125, "*****":150, "⋈":250}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },
    "sword": {"type_name": "Sword", 
               "strength_required": 0.8, 
               "base_chance_to_fail": 0.07, 
               "base_physical_damage_on_rarity": {"*":7, "**":14, "***":21, "****":28, "*****":35, "⋈":55}, 
               "base_durability_on_rarity": {"*":55, "**":80, "***":105, "****":130, "*****":155, "⋈":255}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },
    "greatsword": {"type_name": "Greatsword", 
                   "strength_required": 1.7, 
                   "base_chance_to_fail": 0.1, 
                   "base_physical_damage_on_rarity": {"*":10, "**":20, "***":30, "****":40, "*****":50, "⋈":80}, 
                   "base_durability_on_rarity": {"*":60, "**":90, "***":120, "****":150, "*****":180, "⋈":300}, 
                   "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
                   "preferred_mob_type": "ground", 
                   },
    "axe": {"type_name": "Axe", 
               "strength_required": 1.5, 
               "base_chance_to_fail": 0.08, 
               "base_physical_damage_on_rarity": {"*":8, "**":16, "***":24, "****":32, "*****":40, "⋈":65}, 
               "base_durability_on_rarity": {"*":60, "**":80, "***":105, "****":130, "*****":155, "⋈":255}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "ground", 
               },

    # Ranged weapons

    "bow": {"type_name": "Bow", 
            "strength_required": 1.0, 
            "base_chance_to_fail": 0.15,

            # Damage is low because that is just for the bow itself, the true damage comes from the arrows used later on. 
            "base_physical_damage_on_rarity": {"*":4, "**":8, "***":12, "****":16, "*****":20, "⋈":30}, 
            
            "base_durability_on_rarity": {"*":40, "**":60, "***":80, "****":100, "*****":120, "⋈":200}, 
            "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
            "preferred_mob_type": "air", 
            },
    "crossbow": {"type_name": "Crossbow", 
                 "strength_required": 1.2, 
                 "base_chance_to_fail": 0.12, 
                 
                 # Damage is low because that is just for the crossbow itself, the true damage comes from the arrows used later on. 
                 "base_physical_damage_on_rarity": {"*":6, "**":12, "***":18, "****":24, "*****":30, "⋈":45}, 
                 
                 "base_durability_on_rarity": {"*":50, "**":70, "***":90, "****":110, "*****":130, "⋈":220}, 
                 "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
                 "preferred_mob_type": "air", 
                 },
    "spear": {"type_name": "Spear",
               "strength_required": 1.2, 
               "base_chance_to_fail": 0.09, 
               "base_physical_damage_on_rarity": {"*":7, "**":14, "***":21, "****":28, "*****":35, "⋈":60}, 
               "base_durability_on_rarity": {"*":55, "**":75, "***":100, "****":125, "*****":150, "⋈":250}, 
               "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
               "preferred_mob_type": "air", 
               },

    # Magic weapons

    "staff": {"type_name": "Staff", 
              "strength_required": 0.7, 
              "base_chance_to_fail": 0.1, 
              "base_magical_damage_on_rarity": {"*":8, "**":16, "***":24, "****":32, "*****":40, "⋈":65}, 
              "base_durability_on_rarity": {"*":50, "**":60, "***":70, "****":90, "*****":110, "⋈":200}, 
              "gemstone_slots_on_rarity": {"*":0, "**":1, "***":1, "****":2, "*****":2, "⋈":3},
              "preferred_mob_type": "magic", 
              },

}



weapon_rarities = {
    "common": {"name": "Common", "symbol": "*", "chance": 0.5},
    "uncommon": {"name": "Uncommon", "symbol": "**", "chance": 0.3},
    "rare": {"name": "Rare", "symbol": "***", "chance": 0.15},
    "epic": {"name": "Epic", "symbol": "****", "chance": 0.1},
    "legendary": {"name": "Legendary", "symbol": "*****", "chance": 0.05},
    "godly": {"name": "Godly", "symbol": "⋈", "chance": 0.01}
}

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