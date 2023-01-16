class Player():
    def __init__(self, tname, pname, position):
        self.__tname = tname
        self.__pname = pname
        self.__position = 'center' or 'forward' or 'guard'
    def get_tname(self):
        return self.__tname
    def get_pname(self):
        return self.__pname
    def get_position(self):
        return self.__position
    def set_tname(self, tname):
        self.__tname = tname
    def set_pname(self, pname):
        self.__pname = pname
    def set_position(self, position):
        self.__position = position
class BasketballPlayer(Player):
    def __init__(self, tname, pname, positions):
        super().__init__(tname, pname,positions)
        self.__tname = tname
        self.__pname = pname
        self.__positions = positions
    def __str__(self):
        s = '{} playing as a {}'.format(self.get_pname(),self.get_position())
        return s
tname = input("Enter the basketball team name: ")
pname = input("Enter player name: ")
position = input("Which position is he/she playing? ")
bbp1 = BasketballPlayer(tname, pname, position)
bbp1.set_tname(tname)
bbp1.set_pname(pname)
bbp1.set_position(position)
print(bbp1)
