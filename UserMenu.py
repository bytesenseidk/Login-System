import os
import time
import sqlite3


class UserMenu(object):
    def __init__(self, username=None):
        self.username = username
        self.options = {
            "0": self.exit,
            "1": self.print_data,
            "2": self.add_data,
            "3": self.delete_data
        }
    
    def structure_database(self):
        column_names = []
        os.system("cls")
        print("[ FIRST TIME DATABASE SETUP ]")
        try:
            columns = int(input("Amount of columns  >> "))
            for col in range(columns):
                col_name = input(f"Enter column {col} name  >> ")
                column_names.append(col_name)
        except:
            print("Enter valid data please..")
            time.sleep(1)
            self.structure_database()
        
        
        return column_names
                
        
    def personal_data(self):
        pass
        
    def exit(self):
        print("Exitting..")

    def print_data(self):
        self.structure_database()

    def add_data(self):
        print("Adding data")

    def delete_data(self):
        print("Deleting data")

    
    def menu(self):
        print("[ USER MENU ]\n"
              "[0] EXIT\n"
              "[1] PRINT DATA\n"
              "[2] ADD DATA\n"
              "[3] DELETE DATA\n")
        try:
            selection = input("  >> ")
            method = self.options[selection]
            method()
        except:
            self.menu()


if __name__ == "__main__":
    UserMenu().menu()