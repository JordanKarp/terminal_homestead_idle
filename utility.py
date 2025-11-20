import os


def get_number_in_range(prompt, max_val, min_val=1):
    """
    Prompts the user for a number and ensures it falls within a specified range.

    Args:
        prompt (str): The message to display to the user.
        min_val (int/float): The minimum allowed value (inclusive).
        max_val (int/float): The maximum allowed value (inclusive).

    Returns:
        int/float: The valid number entered by the user.
    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)  # Use float to allow for decimal numbers
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Error: Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def question(question, dict_of_answers):
    print(question)
    index_dict = {}
    for idx, option in enumerate(dict_of_answers):
        index_dict[idx] = option
        print(f"{idx+1}. {option}")
    index_dict[idx + 1] = "Quit"
    print(f"{idx+2}. Quit")

    choice = get_number_in_range("> ", len(index_dict))
    choice -= 1
    if index_dict[choice] == "Quit":
        print("quit")
        return False
    func = dict_of_answers[index_dict[choice]]
    try:
        func()
        return True
    except Exception:
        print("no function")
        return False


# Online Python - IDE, Editor, Compiler, Interpreter
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (posix)
    else:
        _ = os.system('clear')