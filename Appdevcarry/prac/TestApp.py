from Person import *
from Student import *
from Lecturer import *

name = input("Enter Lecturer Name: ")
nric = input('Enter Lecturer NRIC: ')
staffid = input('Enter Staff Id: ')
hour = float(input('Enter Total Teaching Hour: '))
lecturer1 = Lecturer(name, nric, staffid)
lecturer1.set_total_TeachingHour(hour)


name = input("Enter Student Name: ")
nric = input('Enter Student NRIC: ')
adminNo = input('Enter Student Admin No: ')
test = float(input('Enter Test mark: '))
exam = float(input('Enter Exam mark: '))

student1 = Student(name, nric, adminNo)
student1.set_test_Mark(test)
student1.set_exam_Mark(exam)

print(lecturer1)
print(student1)
