class Monster():
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence= defence
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__attack
    def get_defence(self):
        return self.__defence
    def set_name(self, name):
        self.__name = name
    def set_health(self, health):
        self.__health = health
    def set_attack(self, attack):
        self.__attack = attack
    def set_defence(self, defence):
        self.__defence = defence
    def display(self):
        print('%s is a Monster' % self.__name)
class FireMonster(Monster):
    def __init__(self):
        Monster.__init__(self, 'firebug', 10, 9, 4)
    def display(self):
        print('%s is a Fire type monster' % self.get_name())
class WaterMonster(Monster):
    def __init__(self):
        Monster.__init__(self, 'waterbird', 15, 6, 3)
    def display(self):
        print('%s is a Water type monster' % self.get_name())
class GrassMonster(Monster):
    def __init__(self):
        Monster.__init__(self, 'grasshopper', 20, 5, 3)
    def display(self):
        print('%s is a Grass type monster' % self.get_name())
def DisplayInfo(monster):
    if isinstance(monster, Monster):
        monster.display()
    else:
        print('Invalid monster')
monster = Monster('Giant', 17, 6, 7)
fire = FireMonster()
water = WaterMonster()
grass = GrassMonster()
monster.display()
fire.display()
water.display()
grass.display()
DisplayInfo('monster')
