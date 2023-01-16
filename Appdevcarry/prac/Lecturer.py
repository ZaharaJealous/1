from Student import *
from Person import *
class Lecturer(Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_Id = staff_id
        self.__total_TeachingHour = 0
    def get_staff_Id(self):
        return self.__staff_Id
    def get_total_TeachingHour(self):
        return self.__total_TeachingHour
    def set_staff_Id(self, staffId):
        self.__staff_Id = staffId
    def set_total_TeachingHour(self,totalTeachingHour):
        self.__total_TeachingHour = totalTeachingHour
    def computeSalary(self):
        return self.__total_TeachingHour*90
    def __str__(self):
        s = '%s, Staff Id: %s earns $%.2f' %(self.get_name(), self.get_staff_Id(), self.computeSalary())
        return s
lname = input("Enter Lecturer Name: ")
lnric = input("Enter Lecturer NRIC: ")
sId = input("Enter Staff ID: ")
hours = float(input("Enter Teaching Hours: "))
l1 = Lecturer(lname, lnric, sId)
l1.set_total_TeachingHour(hours)

sname = input("Enter Student Name: ")
snric = input("Enter Student NRIC: ")
admno = input("Enter Student admin number: ")
testmark = float(input("Enter test mark: "))
exammark = float(input("Enter exam mark: "))
s1 = Student(sname, snric, admno)
s1.set_test_Mark(testmark)
s1.set_exam_Mark(exammark)

print(l1)
print(s1)
