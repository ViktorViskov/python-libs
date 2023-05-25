from multi_file.modul1 import Mod1
from multi_file.modul2 import Mod2
from multi_file.modul3 import Mod3


class Container:
    def __init__(self):
        self.mod1 = Mod1("Modul 1", self)
        self.mod2 = Mod2("Modul 2", self)
        self.mod3 = Mod3("Modul 3", self)