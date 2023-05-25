class Container:
    def __init__(self):
        self.mod1 = Mod1("Modul 1", self)
        self.mod2 = Mod2("Modul 2", self)
        self.mod3 = Mod3("Modul 3", self)

class Mod1:
    def __init__ (self, string, root):
        self.string = string
        self.root: Container = root

    def print_string(self):
        print(self.string)

class Mod2:
    def __init__ (self, string, root):
        self.string = string
        self.root: Container = root

    def print_string(self):
        print(self.string)

class Mod3:
    def __init__ (self, string, root):
        self.string = string
        self.root: Container = root

    def print_string(self):
        print(self.string)