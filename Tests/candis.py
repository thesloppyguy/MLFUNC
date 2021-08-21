class spell:
    def __init__(self, name=None, cost=None, dmg=None, type=None):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        mgdl = self.dmg - 5
        mgdh = self.dmg + 5
        return(self.dmg-5)
