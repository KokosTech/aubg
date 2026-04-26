"""

# Project: COS 3040 Python Project

"""

from utils.menu import display_menu, get_user_choice, clear_screen


def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "5":
            clear_screen()
            print("Exiting TrainSimPy. Goodbye!")
            break

if __name__ == "__main__":
    main()