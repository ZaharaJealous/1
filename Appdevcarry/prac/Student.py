import Person
class Student(Person.Person):
    def __init__(self, name, nric, admin_no):
        Person.Person.__init__(self, name, nric)
        self.__test_Mark = 0
        self.__exam_Mark = 0
        self.__admin_No = admin_no
    def get_admin_No(self):
        return self.__admin_No
    def get_exam_Mark(self):
        return self.__exam_Mark
    def get_test_Mark(self):
        return self.__test_Mark
    def set_admin_No(self, adminNo):
        self.__admin_No = adminNo
    def set_exam_Mark(self, examMark):
        self.__exam_Mark = examMark
    def set_test_Mark(self, testMark):
        self.__test_Mark = testMark
    def computeFinalMark(self):
        return (self.__test_Mark + self.__exam_Mark) / 2
    def __str__(self):
        s = "{}, Admin no: {} final mark is {:.2f}".format(self.get_name(), self.get_admin_No(), self.computeFinalMark())
        return s
