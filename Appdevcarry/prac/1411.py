while True:
    try:
        name = input('Enter name: ')
        weight = float(input('Enter weight (kg): '))
        height = float(input('Enter height(m): '))

        bmi = weight/height**2
        print(bmi)

        command = input('Store your bmi to file? (Y/N): ')
        if command.upper() == 'Y':
            bmi_File = open('bmi.txt', 'a')
            bmi_File.write(name+','+ str(bmi) +'\n')
            bmi_File.close()

        command = input('Do you want to continue? (Y/N): ')
        if command.upper() == 'N':
            break
    except ValueError:
        print('Invalid number entered')
    except ZeroDivisionError:
        print('Division by zero')
    except IOError:
        print('Error with file I/O')

command = input('Do you want view BMI record in file? (Y/N): ')
if command.upper() == 'Y':
    try:
        bmi_File = open('bmi.txt', 'r')
        contents = bmi_File.read()
        print(contents)
        #bmi_File.close()
    except IOError:
        print('Error with file')
    finally:
        print('End of the program')
        bmi_File.close()
################################3
class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = []

    def get_score(self):
#        return (str(self.math) + str(self.chinese) + str(self.english) + str(self.science))
        return (self.math + self.chinese + self.english + self.science) / 4

def main():
    students = load_result()
    for s in students:
        s.choices.append('School A')
        s.choices.append('School B')
        s.choices.append('School C')
        print('%s scored %.2f and the choices are %s, %s, %s' %(s.name, s.get_score(), s.choices[0], s.choices[1], s.choices[2]))


def load_result():
    students = []
    try:
        student_file = open('student.txt','r')
        for result in student_file:
            list = result.split(',')
            s1 = Student(list[0])
            s1.math = float(list[1])
            s1.chinese = float(list[2])
            s1.english = float(list[3])
            s1.science = float(list[4])
            students.append(s1)
    except IOError:
        print('Error with file')
    return students


# start the test program
main()
##############################################
class Phone:
    count = 0
    def __init__(self):
        self.__Id = None
        self.__make = None
        self.__model = None
        self.__price = 0
        self.__class__.count += 1
    def set_id(self, phone_id):
        self.__Id = phone_id
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
        else:
            print("price should consist of numbers")
    def get_id(self):
        return self.__Id
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def __str__(self):
        s = 'The phone make is {} {} priced at ${}. Current stock is {}'.format(self.__make, self.__model, self.__price, self.__class__.count)
        return s
input_phone_make = input("Enter make of phone: ")
input_phone_model = input("Enter model of phone: ")
input_phone_price = input("Enter price of phone: ")
ph = Phone()
ph.set_make(input_phone_make)
ph.set_model(input_phone_model)
ph.set_price(input_phone_price)
print(ph)
