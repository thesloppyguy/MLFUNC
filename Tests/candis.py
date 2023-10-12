class spell:
    def __init__(self, name=None, cost=None, dmg=None, type=None):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        self.name = ['mango']
        self.cost = ['ass', 'bass']
        self.dmg = [100, 200]
        self.type = ['tango', 'fango']

    def func_2(self):
        print(self.name)
        print(self.cost)
        print(self.dmg)
        print(self.type)
