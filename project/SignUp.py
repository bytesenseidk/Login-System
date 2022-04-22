import os

class SignUp(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.user_id = self.account_count()
    
    def account_count(self):
        if not os.path.exists("Database//users.txt"):
            open("Database//users.txt", "a").close()

        with open("Database//users.txt", "r") as file:
            text = file.readlines()
            try:
                for index, line in enumerate(text):
                    count = index
                return count + 1
            except:
                return 0

    def save(self):
        with open("Database//users.txt", "a") as file:
            file.write(f"{self.username},{self.password},{self.user_id}\n")
    
    
    @staticmethod
    def valid_username(username):
        valid = True
        if os.path.exists("Database//users.txt"):
            with open("Database//users.txt", "r") as file:
                text = file.readlines()
                for line in text:
                    for user in line.split("\n"):
                        if username == user.split(",")[0]:
                            valid = False
        return valid
