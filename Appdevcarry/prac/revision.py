class Shape:
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return 0
class Square(Shape):
    def __init__(self, side, length):
        super().__init__(side)
        self.length = length
    def calculate_perimeter(self):
        return self.side * self.length
    def __str__(self):
        s = 'Square with {} side and length of {} has a perimeter of {}'.format(self.side,self.length, self.calculate_perimeter())
        return s
sq = Square(4,10)
print(sq)
##################teachers^^#######################
class Shape:
    def __init__(self, side):
        self.__side = side
    def set_side(self,side):
        self.__side = side
    def get_side(self):
        return self.__side
    def calculate_perimeter(self):
        p = self.__side + self.__side
        return p
class Square(Shape):
    def __init__(self,side, length):
        super().__init__(side)
        self.__side = side
        self.__length = length
    def set_length(self,length):
        self.__length = length
    def get_length(self):
        return self.__length
    def calculate_perimeter(self):
        p = self.__side * self.__length
        return p
    def __str__(self):
        st = 'Square with {} side and length of {} has a perimeter of {}'.format(self.__side, self.__length,self.calculate_perimeter())
        return st
s = Square(4,10)
print(s)
