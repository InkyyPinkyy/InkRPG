import random

from classes import *
from lists_and_dicts import *

dungeon_sizes = {
    "small": [ # 15 rooms
        ["A1", "A2", "A3"],
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        ["D1", "D2", "D3"],
        ["E1", "E2", "E3"]
        ],

    "medium": [ # 28 rooms
        ["A1", "A2", "A3", "A4"],
        ["B1", "B2", "B3", "B4"],
        ["C1", "C2", "C3", "C4"],
        ["D1", "D2", "D3", "D4"],
        ["E1", "E2", "E3", "E4"],
        ["F1", "F2", "F3", "F4"],
        ["G1", "G2", "G3", "G4"]
        ],

    "large": [ # 45 rooms
        ["A1", "A2", "A3", "A4", "A5"],
        ["B1", "B2", "B3", "B4", "B5"],
        ["C1", "C2", "C3", "C4", "C5"],
        ["D1", "D2", "D3", "D4", "D5"],
        ["E1", "E2", "E3", "E4", "E5"],
        ["F1", "F2", "F3", "F4", "F5"],
        ["G1", "G2", "G3", "G4", "G5"],
        ["H1", "H2", "H3", "H4", "H5"],
        ["I1", "I2", "I3", "I4", "I5"]
        ],
}

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