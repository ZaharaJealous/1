class Course:
    count = 0
    def __init__(self, name, intake):
        self.__name = name
        self.__intake = intake
        self.__class__.count += 1
    def get_intake(self):
        return self.__intake
    def get_name(self):
        return self.__name
    def set_intake(self, intake):
        self.__intake = intake
    def set_name(self,name):
        self.__name = name
    def get_course_info(self):
        return 'Name: {}, intake: {}'.format(self.__name, self.__intake)
c = Course('Diploma in IT',80)
intake = int(input('Enter new intake: '))
c.set_intake(intake)
print(c.get_course_info())
print(Course.count, 'Course(s) created')
###################teachers above^^^#######################
class Course:
    count = 0
    def __init__(self, name, intake):
        self.__name = name
        self.__intake = intake
        self.__class__.count += 1
    def set_name(self, name):
        self.__name = name
    def set_intake(self, intake):
        self.__intake = intake
        intake = 80
    def get_name(self):
        return self.__name
    def get_intake(self):
        return self.__intake
    def get_course_info(self):
        s = 'Name: {}, intake: {}\n{} Course(s) created'.format(self.__name,self.__intake, self.__class__.count)
        return s
intake = int(input("Enter new intake: "))
c = Course('Diploma in IT', intake)
c.set_name('Diploma in IT')
c.set_intake(intake)
print(c.get_course_info())
