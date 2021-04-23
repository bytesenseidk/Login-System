class SignUp(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.user_id = self.account_count()
    
    def account_count(self):
        with open("users.txt", "r") as file:
            text = file.readlines()
            try:
                for index, line in enumerate(text):
                    count = index
                return count + 1
            except:
                return 0

    def save(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.username},{self.password},{self.user_id}\n")
    
    
    @staticmethod
    def valid_username(username):
        valid = True
        with open("users.txt", "r") as file:
            text = file.readlines()
            for line in text:
                for user in line.split("\n"):
                    if username == user.split(",")[0]:
                        valid = False
        return valid


# def sign_up():
#     print("[ SIGN UP ]")
#     while True:
#         username = input("ENTER USERNAME  >> ")
#         if valid_username(username):
#             break
#         else:
#             print("Username Taken, try again..")
#             continue
#     password = getpass.getpass("ENTER PASSWORD  >> ")
#     account_count()
#     with open("users.txt", "a") as file:
#         user_id = account_count()
#         user = {
#             "username": username,
#             "password": password,
#             "user_id": user_id
#         }
#         file.write(f"{user['username']},{user['password']},{user['user_id']}\n")
#     os.system("cls")
#     print("account added")
#     time.sleep(1)



