from classes import *

def enemy_encounter(player, enemy):
    """
    initialises a battle with the player and an enemy.
    There is an option to flee, where the fight gets
    cancelled. The damage of the enemy scales with
    the players strength.
    """
    print(f"\nA {enemy.name} is attacking you!")
    
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}: {player.hp}/{player.max_max_hp} HP")
        print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP")

        action = input("Attack (a) or flee (f)? ")
        if action.lower() == 'a':
            try: damage = random.uniform(
                ((player.attack_damage + player.weapon.weapon_damage) * player.strength) * 0.9,
                ((player.attack_damage + player.weapon.weapon_damage) * player.strength) * 1.1
            )
            except: damage = random.uniform(
                ((player.attack_damage) * player.strength) * 0.9,
                ((player.attack_damage) * player.strength) * 1.1
            )
            enemy.hp -= round(damage)
            # (f"{damage:.2f})

            print(f"You are dealing {round(damage)} damage to the {enemy.name}!")

            if enemy.hp > 0:
                damage = random.uniform(
                enemy.attack_damage * player.strength * 0.5,
                enemy.attack_damage * player.strength * 0.7
            )
                player.hp -= round(damage)
                print(f"The enemy is dealing {round(damage)} damage to you!")

        elif action.lower() == 'f':
            print("You fled!")
            return

    if player.hp > 0:
        print(f"You won gainst the {enemy.name}!")
        gold_earned = random.randint(10, 20)
        player.gold += gold_earned
        print(f"You got {gold_earned} gold!")
        xp_earned = random.randint(enemy.max_hp // 10, enemy.max_hp // 3)
        player.xp += xp_earned
        print(f"You  got {xp_earned} XP!")
        check_amount_player_xp(player)
        
    else:
        print("You lost...")
        exit()

def check_amount_player_xp(player):
    while player.xp >= (player.level * 32):
        player.xp -= (player.level * 32)
        player.level += 1
        player.skillpoints += 1
        player.hp = player.max_max_hp
        print(f"You reached level {player.level} and got a skillpoint!")
        print(f"Also, your health got regenerated!")

def show_player_stats(player):
        """shows the player's stats"""
        print(f"\n{player.name}'s stats:")
        print(f"Class: {player.name_of_player_class}")
        print(f"{round(player.hp)}/{round(player.max_max_hp)} HP")
        print(f"Damage: {round((player.attack_damage + player.weapon.weapon_damage) * player.strength)}")
        print(f"Your weapon: {player.weapon}")
        print(f"Your armor: {player.armor}")
        print(f"Your ring: {player.ring}")
        print(f"Your necklace: {player.necklace}")
        print(f"Your level: {player.level}")
        print(f"{player.xp}/{player.level * 32} XP until the next level")
        print(f"{player.skillpoints} skillpoints")

def event_enemy_encounter(player):
    monster_data = get_random_monster("normal")
    enemy = Enemy(monster_data)
    enemy_encounter(player, enemy)

def choose_equipment(player):
        player.show_inventory("weapons_armor_rings_necklaces")        
        print(f"Choose an item to equip")

        try:
            wahl = int(input(f"\nProvide the number of the item you want to equip: ")) -1
            if 0 <= wahl < len(player.inventory):
                item = player.inventory[wahl]
                if item.type == "weapon":
                    player.weapon = item
                    print(f"{player.name} equipped '{item.name}' as their weapon!")
                elif item.type == "armor":
                    player.armor = item
                    print(f"{player.name} equipped '{item.name}' as their armor!")
                elif item.type == "ring":
                    player.ring = item
                    print(f"{player.name} equipped '{item.name}' as their ring!")
                elif item.type == "necklace":
                    player.necklace = item
                    print(f"{player.name} equipped '{item.name}' as their necklace!")
                else:
                    print(f"This item can't be equipped!")
            else:
                print(f"invalid selection")
        except ValueError:
            print(f"Please provide a valid number")
    
def consume_item(player):
    consumable_items = player.show_inventory("consumables")
    wahl = int(input(f"\nProvide the number of the item you want to consume: ")) -1
    #player.show_inventory("consumables")
    #print(f"\nWhat item do you want to consume?")
    try:        
        item = consumable_items[wahl]
        if 0 <= wahl < len(player.inventory):
            if item.consumable_type == "health":
                player.hp += item.stats_player_gets
                print(f"{player.name} consumed {item.name} and got {item.stats_player_gets} HP!")
                player.inventory.remove(item)
            elif item.consumable_type == "strength":
                player.strength += item.stats_player_gets
                print(f"{player.name} consumed {item.name} and got {item.stats_player_gets} strength!")
                player.inventory.remove(item)
            elif item.consumable_type == "increase_max_health":
                player.max_hp += item.stats_player_gets
                print(f"{player.name} consumed {item.name} and got additional {item.stats_player_gets} max HP!")
                player.inventory.remove(item)
            elif item.consumable_type == "increase_attack_damage":
                player.attack_damage += item.stats_player_gets
                print(f"{player.name} consumed {item.name} and got additional {item.stats_player_gets} strength!")
                player.inventory.remove(item)
        else:
            return
    except ValueError:
        print(f"Please provide a valid number")

def do_inventory_shit(player):
    player.show_inventory("everything")
    action = input("\nEquip item (1), consume item (2) or return (3)? ")
    if action.lower() == '1':
        choose_equipment(player)
    elif action.lower() == '2':
        consume_item(player)
    elif action.lower() == '3':
        return

def do_random_event(events):
    random_event = random.choice(list(events))()
    return random_event
    
def welcome_player():
    print(f"\nWelcome to your new adventure!")
    print(f"You wake up under a tree and don't remember anything...\nYou can't even recall your own name...")
    print(f"You find a knife in your pocket. It's not much, but you \nshould be able to protect yourself when in danger.")
    name = input("So, what should be your new name in this new life of yours?\nNew name: ")
    return name

def choose_class():
    print(f"\nChoose a class:")
    for i, c in enumerate(CLASSES.keys(), 1):
        print(f"{i}. {c}")
    choice = int(input(f"Your choice: "))
    class_name = list(CLASSES.keys())[choice - 1]
    return class_name

def main():
    if input(f"new game (n) or load an existing game (l)?\n").lower() == 'l':
        name = input("Gib deinen Spielernamen ein: ")
        player = Player.load_game(f"{name}_save.json")
        if not player:
            print(f"invalid name, save-file does not exist.\nPlease try again or start a new game.")
            return
        print(f"Welcome back, {player.name}!")
    else:
        name = welcome_player()
        class_name = choose_class()
        player = Player(name, CLASSES[class_name])

        Knife = weapon("Knife", "weapon","A small knife that you found in your pocket", "knife", 5)
        player.weapon = Knife
        player.inventory.append(Knife)
        player.hp = player.max_max_hp

    while True:
        print(f"\nWhat do you want to do?")
        print(f"1. Explore")
        print(f"2. Inventory")
        print(f"3. Save the game")
        print(f"4. Look at your stats")
        print(f"5. Quit")
        choice = input("Choice: ")

        if choice == '1':
            event_enemy_encounter(player)
        elif choice == '2':
            do_inventory_shit(player)
        elif choice == '3':
            player.save_game()
            print("Game saved!")
        elif choice == '4':
            show_player_stats(player)
        elif choice == '5':
            print("Closed game!")
            break

main()
