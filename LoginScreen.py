import os
import sys
import time
import getpass

def exit():
    sys.exit()


def login():
    while True:
        os.system("cls")
        print("[ LOGIN ]")
        username = input("ENTER USERNAME  >> ")
        password = getpass.getpass("ENTER PASSWORD  >> ")
        if valid_user(username, password):
            print("Login Successful!")
            time.sleep(1)
            break
        else:
            print("Login Unsuccessful, try again..")
            time.sleep(1)
            continue

def valid_user(username=None, password=None):
    valid = False
    with open("users.txt", "r") as file:
        text = file.readlines()
        for line in text:
            for user in line.split("\n"):
                if username == user.split(",")[0] and password == user.split(",")[1]:
                    valid = True
    return valid


def sign_up():
    print("[ SIGN UP ]")
    while True:
        username = input("ENTER USERNAME  >> ")
        if valid_username(username):
            break
        else:
            print("Username Taken, try again..")
            continue
    password = getpass.getpass("ENTER PASSWORD  >> ")
    account_count()
    with open("users.txt", "a") as file:
        user_id = account_count()
        user = {
            "username": username,
            "password": password,
            "user_id": user_id
        }
        file.write(f"{user['username']},{user['password']},{user['user_id']}\n")
    os.system("cls")
    print("account added")
    time.sleep(1)

def account_count():
    with open("users.txt", "r") as file:
        text = file.readlines()
        try:
            for index, line in enumerate(text):
                count = index
            return count + 1
        except:
            return 0

def valid_username(username=None):
    valid = True
    with open("users.txt", "r") as file:
        text = file.readlines()
        for line in text:
            for user in line.split("\n"):
                if username == user.split(",")[0]:
                    valid = False
    return valid


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

