import pandas as pd
import numpy as np
from Soldier import Player
import os
from GridMatrix import GridMatrix
# module for dataBase

#initialize variables for db
# every db has its fields (categories)
#field (4): game_state_id(int), player (object) , parallel_grass_grid(object), trap_grid(object)
# records (רשומות)(0-9): 0,1,2,3,4,5,6,7,8,9

DB_FILE_PATH='db_file.csv'
file_exists = os.path.exists(DB_FILE_PATH)

def create_file():
   if file_exists is False:
        # assign data of Lists.
        initial_data=['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty']
        data = {
            'game_state_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            'player': initial_data,
            'parallel_grass_grid': initial_data,
            'trap_grid':initial_data
        }
        db = pd.DataFrame(data)
        db.to_csv(DB_FILE_PATH,index=False)
   return pd.read_csv(DB_FILE_PATH)


def update_index(key, player, parallel_grass_grid, trap_grid):
    #update a specific row in dataBase
    db = create_file()
    row_index = key
    db.at[row_index,'player'] = player
    db.at[row_index,"parallel_grass_grid"] = parallel_grass_grid
    db.at[row_index,"trap_grid"] = trap_grid
    db.to_csv(DB_FILE_PATH, index=False)

def read_to_display(key_num):
    # function gets the key number that was pressed and read the state
    # from the csv file (name of file saved as const in thos module)
    # function return 3 variables of object type
    db = create_file()
    list_of_returned_objects = []
    columns_list = ['player','parallel_grass_grid', 'trap_grid']

    record_of_state= db.loc[db['game_state_id'] == key_num]

    for index, row in record_of_state.iterrows():
        for column in columns_list:
            list_of_returned_objects.append(row[column])
    return list_of_returned_objects

import ctypes


def memoryad_to_object(hex_ad):
    return ctypes.cast(hex_ad, ctypes.py_object).value

a=5
#print("id of a:",id(a))
#print(memoryad_to_object(id(a)))
#print("id saved in db- player at state 5 :", read_to_display(5)[0])
#print(memoryad_to_object(read_to_display(5)[0]).get_i_leftcorner())






