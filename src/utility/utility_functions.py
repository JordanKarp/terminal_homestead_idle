from src.utility.color_text import color_text
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def get_number_in_list(prompt, approved_list):
    while True:
        try:
            number = int(input(prompt))
            if number in approved_list:
                return number
            print(f"Error: Enter a valid choice.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def ask_question(prompt, text_options_list, approved_options=None, quit=True):
    print(color_text(prompt, style="underline"))
    if not approved_options:
        approved_options = list(range(1, len(text_options_list) + 1))
    for i, label in enumerate(text_options_list, start=1):
        if i in approved_options:
            print(f"{i}. {label}")
        else:
            print(color_text(f"{i}. {label}", "red"))

    if quit:
        quit_index = len(text_options_list) + 1
        print(f"{quit_index}. Back")
        approved_options.append(quit_index)

    choice = int(get_number_in_list("> ", approved_options))

    # Quit
    if quit and choice == quit_index:
        return False

    return text_options_list[choice - 1]


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

    selected_label = labeled_options[choice - 1]
    return options.get(selected_label)
