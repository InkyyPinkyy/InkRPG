from __main__ import *
from classes import *

    # "dungeon_enemy_room",
    # "dungeon_npc_room",
    # "dungeon_black_market_room",
    # "dungeon_pile_of_bones_room",
    # "dungeon_mini_boss_room",
    # "dungeon_boss_room",
    # "dungeon_key_room",
    # "dungeon_library_room",
    # "dungeon_altar_room",
    # "dungeon_church_room",
    # "dungeon_prison_room",
    # "dungeon_spider_room",

import random
import json

# --- Dungeon-Setup ---
def generate_dungeon(num_rooms):
    """Generiert einen Dungeon mit num_rooms Räumen und zufälligen Verbindungen."""
    dungeon = {}
    for i in range(num_rooms):
        # Zufällige Verbindungen zu anderen Räumen
        connections = random.sample(range(num_rooms), random.randint(1, 3))
        connections = [c for c in connections if c != i]  # Keine Verbindung zu sich selbst
        dungeon[i] = {"connections": connections, "visited": False}
    return dungeon

# --- Raum-Mechaniken ---
def dungeon_entrance_room():
    print("Du betrittst einen dunklen Gang, an dessen Wänden Spinnenweben hängen\nund auf dem Weg liegen ein paar Knochen. Ob sie menschlich sind,\nweißt du nicht")

def dungeon_chest_room(player):
    print("Der vor dir liegende Raum beinhaltet nichts außer einer großen\nKiste aus Holz.")
    if str(input(f"Möchtest du die Kiste öffnen? Ja (y) oder Nein (n)?")).lower("y"):
        print("Knarzend öffnet sich die Kiste, als du ihren schweren Deckel anhebst.\nEs sieht so aus, als hättest du einen Schatz gefunden!")
        chest_item = get_random_item(items)
        print(f"In der Kiste findest du: {chest_item}!")
        player.inventory.append(chest_item)
    else:
        pass

def dungeon_mimic_room(player):
    print("Der vor dir liegende Raum beinhaltet nichts außer einer großen\nKiste aus Holz.")
    if str(input(f"Möchtest du die Kiste öffnen? Ja (y) oder Nein (n)?")).lower("y"):
        mimic = Enemy("Mimic", 180, 30)
        print(f"Oh nein! Die Kiste entpuppt sich als Monster,\ndass nur darauf gewartet hat, dich zu zerfleischen!\nDu musst dich verteidigen!")
        enemy_encounter(player, mimic)
        
    else:
        pass

def dungeon_trap_room(player):
    print("Ein Schatz liegt hier! Du bist reich!")

def dungeon_enemy_room(player):
    pass

def dungeon_npc_room(player):
    pass

def dungeon_black_market_room(player):
    pass

def dungeon_pile_of_bones_room(player):
    pass

def dungeon_mini_boss_room(player):
    pass

def dungeon_boss_room(player):
    pass

def dungeon_key_room(player):
    pass

def dungeon_library_room(player):
    pass

def dungeon_altar_room(player):
    pass

def dungeon_church_room(player):
    pass

def dungeon_prison_room(player):
    pass

def dungeon_spider_room(player):
    pass

def dungeon_bonfire_room(player):
    pass



# Mapping von Raumfunktionen
room_functions = {
    0: dungeon_entrance_room,
    1: dungeon_chest_room,
    2: dungeon_mimic_room,
    3: dungeon_trap_room,
    4: dungeon_enemy_room,
    5: dungeon_npc_room,
    6: dungeon_black_market_room,
    7: dungeon_pile_of_bones_room,
    8: dungeon_mini_boss_room,
    9: dungeon_boss_room,
    10: dungeon_key_room,
    11: dungeon_library_room,
    12: dungeon_altar_room,
    13: dungeon_church_room,
    14: dungeon_prison_room,
    15: dungeon_spider_room,
}

# --- Spielstand speichern/laden ---
def save_game(dungeon, current_room):
    """Speichert den Spielstand in einer Datei."""
    with open("savegame.json", "w") as file:
        json.dump({"dungeon": dungeon, "current_room": current_room}, file)
    print("Spielstand gespeichert.")

def load_game():
    """Lädt den Spielstand aus einer Datei."""
    with open("savegame.json", "r") as file:
        data = json.load(file)
    print("Spielstand geladen.")
    return data["dungeon"], data["current_room"]

# --- Spiel-Logik ---
def play_dungeon(dungeon, start_room=0):
    current_room = start_room
    while True:
        # Raum betreten
        if not dungeon[current_room]["visited"]:
            print(f"Du betrittst Raum {current_room}.")
            dungeon[current_room]["visited"] = True
            # Führe raumspezifische Funktion aus
            if current_room in room_functions:
                room_functions[current_room]()
        else:
            print(f"Du bist wieder in Raum {current_room}.")

        # Verfügbare Verbindungen anzeigen
        connections = dungeon[current_room]["connections"]
        print(f"Du kannst in die folgenden Richtungen weitergehen:\n{connections}")

        # Spieler nach der nächsten Richtung fragen
        next_room = None
        while next_room not in connections:
            try:
                next_room = int(input("Hier möchte ich hin: "))
            except ValueError:
                print("Bitte gib eine gültige Raum-Nummer ein.")
        
        current_room = next_room

        # Spiel speichern oder beenden
        action = input("Möchtest du speichern (s), beenden (b) oder weitermachen (w)? ").lower()
        if action == "s":
            save_game(dungeon, current_room)
        elif action == "b":
            print("Spiel beendet.")
            break

# --- Hauptprogramm ---
if __name__ == "__main__":
    try:
        # Spielstand laden oder neuen Dungeon erstellen
        choice = input("Neues Spiel (n) oder Spiel laden (l)? ").lower()
        if choice == "l":
            dungeon, start_room = load_game()
        else:
            num_rooms = int(input("Wie viele Räume soll der Dungeon haben? "))
            dungeon = generate_dungeon(num_rooms)
            start_room = 0

        # Spiel starten
        play_dungeon(dungeon, start_room)
    except FileNotFoundError:
        print("Kein gespeicherter Spielstand gefunden. Starte ein neues Spiel.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
