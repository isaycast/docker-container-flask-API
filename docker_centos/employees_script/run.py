import os
from app import script_csv

if __name__ == "__main__":

    flag = True
    while flag:
        try:        
            script_csv.createTables()
            script_csv.populate_table()
            flag=False
        except :
            print("db not redy yet")
