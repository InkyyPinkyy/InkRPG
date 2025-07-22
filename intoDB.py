import sqlite3
from lists_and_dicts import *

conn = sqlite3.connect('static.db')  # ':memory:' for testing

c = conn.cursor()

def subclasses_to_sql(subclasses):
    with conn:    
        for subclass in subclasses:
            for i in subclass[2].values():
                c.execute(
                    """"INSERT INTO mob_subcls VALUES
                    (:MobName, :SubClsName, :Rank, :SpawnChance, :BaseHP, :BaseDMG, :MobType)
                    """, {'MobName': subclass['name'], 
                          'SubClsName': i['name'], 
                          'Rank': i['rank'], 
                          'SpawnChance': i['spawn_chance'], 
                          'BaseHP': i['base_hp'], 
                          'BaseDMG': i['base_damage'], 
                          'MobType': subclass['mob_type']})
            
subclasses_to_sql(monster_species)