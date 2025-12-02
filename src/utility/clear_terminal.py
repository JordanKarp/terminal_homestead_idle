import os

def clear_terminal():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For Mac and Linux (posix)
    else:
        _ = os.system("clear")
