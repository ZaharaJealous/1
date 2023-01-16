class Player:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def __str__(self):
        return '{}'.format(self.get_name())
class BasketballPlayer(Player):
    positions = ['Center', 'Guard', 'Forward']
    def __init__(self, name):
        Player.__init__(self,name)
        self.__position = ''
    def get_position(self):
        return self.__position
    def set_position(self,position):
        if position in self.__class__.positions:
            self.__position = position
        else:
            print('Invalid position entered')
    def __str__(self):
        return '{} is a player in {} position'.format(self.get_name(), self.get_position())

basketball_team = []
team_name = input('Enter the basketball team name: ')
for i in range(5):
    name = input('Enter player name: ')
    plr = BasketballPlayer(name)
    pos = input('Enter your position: ')
    plr.set_position(pos)
    basketball_team.append(plr)
print('Team ', team_name, 'have the following players: ')
for plr in basketball_team:
    print(plr)
