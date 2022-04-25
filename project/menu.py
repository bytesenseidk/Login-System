import sys
from consolemenu import *
from consolemenu.items import *
from main import login, sign_up

# Create the menu
menu = ConsoleMenu("Login System")

login_option = FunctionItem("Login", login)
signup_option = FunctionItem("Sign Up", sign_up)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)


menu.append_item(login_option)
menu.append_item(signup_option)

menu.append_item(submenu_item)

menu.show()