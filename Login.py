from Encryption import Encrypt

class Login(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def valid_user(self):
        valid = False
        user_file = Encrypt("users.txt").decryption()
        with open(user_file, "r") as file:
            text = file.readlines()
            for line in text:
                for user in line.split("\n"):
                    if self.username == user.split(",")[0] and self.password == user.split(",")[1]:
                        valid = True
        user_file = Encrypt("users.txt").encrypt()
        return valid    
        
