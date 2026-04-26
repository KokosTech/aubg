# displays the menu and handles input from the user


from utils.handlers import Handlers
from utils.ui import clear_screen, display_menu


def run_menu():
    handlers = Handlers()

    while True:
        clear_screen()
        display_menu()
        choice = input("Choice: ").strip()

        clear_screen()
        if choice == "1":
            handlers.handle_load()
        elif choice == "2":
            handlers.handle_add()
        elif choice == "3":
            handlers.handle_modify()
        elif choice == "4":
            handlers.handle_list()
        elif choice == "5":
            handlers.handle_search()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")
