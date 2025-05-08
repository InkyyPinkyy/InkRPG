import random

from classes import *
from lists_and_dicts import *

class Dungeon:
    def __init__(self, name, dungeon_size):
        self.name = name
        self.dungeon_size = "" # "small", "medium" or "large"

        # The number of rooms in the Dungeon is randomly selected between 50% and 100% of the total number of rooms in the dungeon size
        self.num_rooms = random.randint(int((len(dungeon_sizes[dungeon_size]) * len(dungeon_sizes[dungeon_size][0])) * 0.5), int(len(dungeon_sizes[dungeon_size]) * len(dungeon_sizes[dungeon_size][0])))

class DungeonRoom:
    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type # "enemy", "treasure", "trap", "empty"
        self.room_description = "" # description of the room
        self.room_items = [] # items in the room
        self.room_monsters = [] # monsters in the room