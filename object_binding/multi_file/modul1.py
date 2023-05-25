class Mod1:
    def __init__ (self, string, root):
        from multi_file.container import Container


        self.string = string
        self.root: Container = root

    def print_string(self):
        print(self.string)