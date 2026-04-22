# displays the menu and handles input from the user

import os
import subprocess

from utils.config import DEFAULT_CARRIAGE_CAPACITY, TRAINS_FILE


def display_menu():
    print("Welcome to TrainSimPy!")
    print(f"Trains file: {TRAINS_FILE}")
    print(f"Default carriage capacity: {DEFAULT_CARRIAGE_CAPACITY}")
    print("1. Load data")
    print("2. Display stations")
    print("3. Display railways")
    print("4. Display trains")
    print("5. Exit")
    
def get_user_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return get_user_choice()
        
def clear_screen():
    # fun fact, os.system is soft-deprecated (idk since when), but they got subprocess
    subprocess.call("cls" if os.name == "nt" else "clear", shell=True)