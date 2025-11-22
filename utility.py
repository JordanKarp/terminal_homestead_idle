import os


def get_number_in_range(prompt, max_val, min_val=1):
    """
    Prompt the user for a number within a range.

    Args:
        prompt (str): Message to show to the user.
        min_val (int/float): Minimum allowed value (inclusive).
        max_val (int/float): Maximum allowed value (inclusive).

    Returns:
        float: A valid number entered by the user.
    """
    while True:
        try:
            number = float(input(prompt))
            if min_val <= number <= max_val:
                return number
            print(f"Error: Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def question(prompt, options: dict):
    """
    Asks a multiple-choice question where each option maps to a function.

    Args:
        prompt (str): The question to display.
        options (dict[str, callable]): Keys are labels, values are functions.

    Returns:
        bool: True if an option function executed successfully, False if quit or error.
    """

    print(prompt)

    # Build the numbered menu
    labeled_options = list(options.keys())
    for i, label in enumerate(labeled_options, start=1):
        print(f"{i}. {label}")
    quit_index = len(labeled_options) + 1
    print(f"{quit_index}. Quit")

    # Get user choice
    choice = int(get_number_in_range("> ", quit_index))

    # Quit
    if choice == quit_index:
        print("Quitting...")
        return False

    # Run selected function
    selected_label = labeled_options[choice - 1]
    return options.get(selected_label)

    # func = options.get(selected_label)

    # try:
    #     func()
    #     return True
    # except Exception as e:
    #     print(f"Error calling function '{selected_label}': {e}")
    #     return False


# Online Python - IDE, Editor, Compiler, Interpreter
def clear_terminal():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For Mac and Linux (posix)
    else:
        _ = os.system("clear")
