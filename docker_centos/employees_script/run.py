import os
from app import script_csv

if __name__ == "__main__":
    print(os.getcwd())
    script_csv.createTables()
    script_csv.populate_table()
