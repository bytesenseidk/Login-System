import os
import sys
import time
import getpass
from Login import Login
from SignUp import SignUp



def login():
    while True:
        os.system("cls")
        print("[ LOGIN ]")
        username = input("ENTER USERNAME  >> ")
        password = getpass.getpass("ENTER PASSWORD  >> ")
        if Login.valid_user(username, password):
            print("Login Successful!")
            time.sleep(1)
            break
        else:
            print("Login Unsuccessful, try again..")
            time.sleep(1)
            continue


def sign_up():
    print("[ SIGN UP ]")
    while True:
        username = input("ENTER USERNAME  >> ")
        if SignUp.valid_username(username):
            break
        else:
            print("Username Taken, try again..")
            continue
    password = getpass.getpass("ENTER PASSWORD  >> ")
    SignUp.save(username, password)
    

os.system("cls")
functions = {
    "1": login,
    "2": sign_up
}

while True:
    os.system("cls")
    print("[ LOGIN SYSTEM ]\n"
        "[0] Exit\n"
        "[1] LOGIN\n"
        "[2] SIGN UP\n")

    choice = input("  >> ")
    if choice == "0":
        break
    try:
        os.system("cls")
        function = functions[choice]
        function()
    except:
        os.system("cls")
        print("Enter valid option please...")
        time.sleep(1)
        continue
