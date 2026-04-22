# displays the menu and handles input from the user

import os
import subprocess

def display_menu():
    print("=== TrainSimPy Menu ===")
    print("1. Manually load data")
    print("2. Add...")
    print("3. Modify...")
    print("4. List...")
    print("5. Find an optimal route")
    print("6. Exit")

def get_user_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice in list(map(str, range(1, 7))):
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return get_user_choice()
        
def clear_screen():
    # fun fact, os.system is soft-deprecated (idk since when), but they got subprocess
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)