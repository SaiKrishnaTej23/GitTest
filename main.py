class Main:
    param = 'hello'

    def __init__(self):
        print('hi')
        self.param = 'This is new param'
        self.print_string()

    def print_string(self):
        print(self.param)
        self.hi_there()

    def hi_there(self):
        print('hi there'+ self.param)


mains = Main()
maas = Main()