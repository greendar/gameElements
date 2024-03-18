class Ship:
    def __str__(self):
        # change this to reflect full dataset
        return f"{self.name} hits on a {self.hit}"



# check all below for accuracy. done from memory
    
class Cruiser(Ship):
    def __init__(self, upgraded = False):
        self.name = "Cruiser"
        self.hit = 7
        self.capacity = 0
        self.antiFighterBarrage = False
        self.afb = 0
        self.upgraded = upgraded
        self.sustainDamage = False
        self.bombardment = False

        if self.upgraded:
            # do the upgrade stuff here
            pass

class Destroyer(Ship):
    def __init__(self, upgraded = False):
        self.name = "Destroyer"
        self.hit = 7
        self.capacity = 0
        self.antiFighterBarrage = False
        self.afb = 0
        self.upgraded = upgraded
        self.sustainDamage = False
        self.bombardment = False

        if self.upgraded:
            # do the upgrade stuff here
            pass

class Carrier(Ship):
    def __init__(self, upgraded = False):
        self.name = "Carrier"
        self.hit = 7
        self.capacity = 0
        self.antiFighterBarrage = False
        self.afb = 0
        self.upgraded = upgraded
        self.sustainDamage = False
        self.bombardment = False

        if self.upgraded:
            # do the upgrade stuff here
            pass

class Dreadnought(Ship):
    def __init__(self, upgraded = False):
        self.name = "Dreadnought"
        self.hit = 7
        self.capacity = 0
        self.antiFighterBarrage = False
        self.afb = 0
        self.upgraded = upgraded
        self.sustainDamage = False
        self.bombardment = False

        if self.upgraded:
            # do the upgrade stuff here
            pass

class Fighter(Ship):
    def __init__(self, upgraded = False):
        self.name = "Fighter"
        self.hit = 7
        self.capacity = 0
        self.antiFighterBarrage = False
        self.afb = 0
        self.upgraded = upgraded
        self.sustainDamage = False
        self.bombardment = False

        if self.upgraded:
            # do the upgrade stuff here
            pass






a = Cruiser()

print(a.antiFighterBarrage)
