
import random

from classes import *
from lists_and_dicts import *
from dungeon import *



def event_enemy_encounter(player):
    monster_data = Enemy.get_random_monster("normal")
    enemy = Enemy(monster_data)
    player.enemy_encounter(enemy)

events = {
    1: "event_enemy_encounter",
    2: "event_wandering_trader_encounter",
    3: "event_player_finds_village",
    4: "event_player_finds_dungeon",
    5: "event_player_finds_random_house",
    6: "event_npc_encounter",
    7: "event_player_finds_ruins",
    8: "event_payer_finds_ancient_ruins",
    9: "event_player_finds_camp",
    10: "event_player_finds_hostile_camp",
    11: "event_player_random_thoughts",
    12: "event_bird_shits_on_player",
    13: "event_random_animal",
    14: "event_player_finds_farmhouse",
    15: "event_player_finds_abandoned_farmhouse",
    16: "event_player_finds_herb",
    17: "event_player_finds_city",
    18: "event_player_finds_npc_getting_attacked",
}

def do_random_event():
    random_event = random.choice(list(events.values()))
    return random_event
