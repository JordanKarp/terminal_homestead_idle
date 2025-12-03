class Menu:
    def __init__(self, all_options, show_all=True):
        self.all_options = all_options
        self.show_all = show_all

    def display(self):
        if sh