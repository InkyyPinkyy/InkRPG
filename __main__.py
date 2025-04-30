from classes import *

def enemy_encounter(player, enemy):
    '''
    initialisiert einen Kampf zwischen dem Spieler 
    und einem Gegner. Am Anfang gibt es die Option,
    zu fliehen oder den Kampf zu starten.
    Beim fliehen wird der Kampf beendet, beim Kämpfen
    wird er richtig initialisiert. 
    Dabei werden der Schaden des Spielers und der
    des Gegners verschieden ausgerechnet.
    '''
    print(f"\nEin {enemy.name} greift an!")
    
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}: {player.hp}/{player.max_max_hp} HP")
        print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP")

        action = input("Angreifen (a) oder Fliehen (f)? ")
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
            print(f"Du fügst dem {enemy.name} {round(damage)} Schaden zu!")

            if enemy.hp > 0:
                damage = random.uniform(
                enemy.attack_damage * player.strength * 0.9,
                enemy.attack_damage * player.strength * 1.1
            )
                player.hp -= round(damage)
                print(f"Der {enemy.name} fügt dir {round(damage)} Schaden zu!")

        elif action.lower() == 'f':
            print("Du bist geflohen!")
            return

    if player.hp > 0:
        print(f"Du hast den {enemy.name} besiegt!")
        gold_earned = random.randint(10, 20)
        player.gold += gold_earned
        print(f"Du erhältst {gold_earned} Gold!")
        xp_earned = random.randint(enemy.max_hp // 10, enemy.max_hp // 3)
        player.xp += xp_earned
        print(f"Du erhältst {xp_earned} XP!")
        check_amount_player_xp(player)
        
    else:
        print("Du wurdest besiegt...")
        exit()

def check_amount_player_xp(player):
    while player.xp >= (player.level * 32):
        player.xp -= (player.level * 32)
        player.level += 1
        player.skillpoints += 1
        print(f"Du hast Level {player.level} erreicht und einen Skillpunkt bekommen!")

def show_player_stats(player):
        """Zeigt die Stats des Spielers an"""
        print(f"\n{player.name}'s Stats:")
        print(f"Rasse: {player.name_of_player_class}")
        print(f"{round(player.hp)}/{round(player.max_max_hp)} HP")
        print(f"Damage:", (player.attack_damage + player.weapon.weapon_damage) * player.strength)
        print(f"Deine Waffe: {player.weapon}")
        print(f"Deine Rüstung: {player.armor}")
        print(f"Dein Ring: {player.ring}")
        print(f"Deine Kette: {player.necklace}")
        print(f"Dein Level: {player.level}")
        print(f"{player.xp}/{player.level * 32} XP bis zum nächsten Level")
        print(f"{player.skillpoints} Skillpoints")
        print(f"Gold: {player.gold}")

def event_enemy_encounter(player):
    monster_data = get_random_monster(monsters)
    gegner = Enemy(monster_data)
    enemy_encounter(player, gegner)

def choose_equipment(player):
        player.show_inventory("weapons_armor_rings_necklaces")        
        print(f"Wähle einen Gegenstand zum Ausrüsten:")

        try:
            wahl = int(input(f"\nGib die Nummer des Gegenstandes ein, den du auwählen möchtest: ")) -1
            if 0 <= wahl < len(player.inventory):
                item = player.inventory[wahl]
                if item.type == "weapon":
                    player.weapon = item
                    print(f"{player.name} hat '{item.name}' als Waffe ausgerüstet!")
                elif item.type == "armor":
                    player.armor = item
                    print(f"{player.name} hat '{item.name}' als Rüstung ausgerüstet!")
                elif item.type == "ring":
                    player.ring = item
                    print(f"{player.name} hat '{item.name}' als Ring ausgerüstet!")
                elif item.type == "necklace":
                    player.necklace = item
                    print(f"{player.name} hat '{item.name}' als Kette ausgerüstet!")
                else:
                    print(f"Dieses Item kann nicht ausgerüstet werden!")
            else:
                print(f"ungültige Auswahl")
        except ValueError:
            print(f"Bitte gib eine gültige Zahl ein")
    
def consume_item(player):
    player.show_inventory("consumables")
    print(f"\nWas möchtest du konsumieren?")
    try:
        wahl = int(input(f"\nGib die Nummer des Gegenstandes ein, den du auwählen möchtest: "))
        item = player.show_inventory("consumables")[wahl]
        if 0 <= wahl < len(player.inventory):
            if item.consumable_type == "health":
                player.hp += item.stats_player_gets
                print(f"{player.name} hat {item.name} konsumiert und {item.stats_player_gets} HP erhalten!")
                player.inventory.remove(item)
            elif item.consumable_type == "strength":
                player.strength += item.stats_player_gets
                print(f"{player.name} hat {item.name} konsumiert und {item.stats_player_gets} Stärke erhalten!")
                player.inventory.remove(item)
            elif item.consumable_type == "increase_max_health":
                player.max_hp += item.stats_player_gets
                print(f"{player.name} hat {item.name} konsumiert und\nzusätzliche {item.stats_player_gets} maximale HP erhalten!")
                player.inventory.remove(item)
            elif item.consumable_type == "increase_attack_damage":
                player.attack_damage += item.stats_player_gets
                print(f"{player.name} hat {item.name} konsumiert und {item.stats_player_gets} zusätzlichen Angriffsschaden erhalten!")
                player.inventory.remove(item)
        else:
            return
        return
    except ValueError:
        print(f"Bitte gib eine gültige Zahl ein")

def do_inventory_shit(player):
    player.show_inventory("all")
    action = input("\nGegenstand ausrüsten (1), Gegenstand konsumieren (2) oder zurückkehren (3)? ")
    if action.lower() == '1':
        choose_equipment(player)
    elif action.lower() == '2':
        return
        #consume_item(player)
    elif action.lower() == '3':
        return

def do_random_event(events):
    random_event = random.choice(list(events))()
    return random_event
    
def welcome_player():
    print(f"\nWillkommen zu deinem neuen Abenteuer!")
    print(f"Du wachst an einem dir unbekannten Strand auf und erinnerst dich an nichts...\nNicht einmal dein eigener Name fällt dir ein...")
    print(f"In deinen Taschen findest du ein Messer, es ist nicht viel,\naber du solltest dich im Notfall verteidigen können.")
    name = input("Also, wie möchtest du in deinem neuen Leben heißen?\nNeuer Name: ")
    return name

def choose_class():
    print(f"\nWähle eine Klasse:")
    for i, c in enumerate(CLASSES.keys(), 1):
        print(f"{i}. {c}")
    choice = int(input(f"Deine Wahl: "))
    class_name = list(CLASSES.keys())[choice - 1]
    return class_name

def main():
    if input(f"Neues Spiel (n) oder Laden (l)?\n").lower() == 'l':
        name = input("Gib deinen Spielernamen ein: ")
        player = Player.load_game(f"{name}_save.json")
        if not player:
            return
    else:
        name = welcome_player()
        class_name = choose_class()
        player = Player(name, CLASSES[class_name])

        Messer = weapon("Messer", "weapon","Ein kleines Messer, dass du in deiner Tasche gefunden hast", "messer", 5)
        Drachenschwert = weapon("Drachenschwert", "weapon", "Random-ass Schwert zu test-zwecken", "Schwert", 6969)
        RandomAssRing = ring("Ring der Rache oder so", "ring", "Random ass test-ring", "rache", 69)
        Heiltrank = consumable("Heiltrank", "consumable", "Eine kleine Glasröhre mit einer rötlich schimmernden Flüssigkeit","health",100)
        player.weapon = Messer
        player.inventory.append(Messer)
        player.inventory.append(Drachenschwert)
        player.inventory.append(RandomAssRing)
        player.inventory.append(Heiltrank)
        player.hp = player.max_max_hp

    while True:
        print(f"\nWas möchtest du tun?")
        print(f"1. Erkunden")
        print(f"2. Inventar ansehen")
        print(f"3. Spiel speichern")
        print(f"4. Beenden")
        print(f"5. Deine Stats ansehen")
        choice = input("Deine Wahl: ")

        if choice == '1':
            event_enemy_encounter(player)
        elif choice == '2':
            do_inventory_shit(player)
        elif choice == '3':
            player.save_game()
            print("Spiel gespeichert!")
        elif choice == '4':
            print("Spiel beendet!")
            break
        elif choice == '5':
            show_player_stats(player)

main()
