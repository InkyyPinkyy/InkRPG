from lists_and_dicts import *
from classes import *
from events import *

class Game:
    
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
            player = Player.load_game(f"{name}_save.json", f"{name}_settings.json")
            if not player:
                print(f"invalid name, save-file, settings-file or both of them does/do not exist.\nPlease try again or start a new game.")
                return
            print(f"Welcome back, {player.name}!")
        else:
            name = Game.welcome_player()
            class_name = Game.choose_class()
            player = Player(name, CLASSES[class_name])

            Knife = weapon("Knife", "weapon","A small knife that you found in your pocket", "knife", 5)
            HealingPotion = consumable("Healing Potion", "consumable", "A tube out of glass with a red liquid inside", "health", 100)
            player.weapon = Knife
            player.inventory.append(Knife)
            player.inventory.append(HealingPotion)
            player.hp = player.max_max_hp

        while True:

            print(f"\nWhat do you want to do?")
            print(f"1. Explore")
            print(f"2. Inventory")
            print(f"3. Save the game")
            print(f"4. Look at your stats")
            print(f"5. Settings")
            print(f"6. Quit")
            choice = input("Choice: ")

            if choice == '1':
                if player.autosave_on ==True:
                    player.save_game()
                    print(f"Autosaved game!")
                Game.event_enemy_encounter(player)           
            elif choice == '2':
                player.do_inventory_shit()
            elif choice == '3':
                player.save_game()
                print("Game saved!")
            elif choice == '4':
                player.show_player_stats()
            elif choice == '5':
                player.go_to_settings()
            elif choice == '6':
                print("Closed game!")
                break

Game.main()