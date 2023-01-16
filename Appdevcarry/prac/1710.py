class Customer:
    def __init__(self, name, email, number):
        self.__name = name
        self.__email = email
        self.__mobile_number = number
    def get_customer_info(self):
        return 'Name: ' + self.__name + ', Email: ' + self.__email + \
           ', Mobile Number: ' + self.__mobile_number
c1 = Customer("John", "john@nyp.edu.sg", "92345678")
print(c1.get_customer_info())
#####################################################
m1 = input("Enter the make of the phone: ")
m2 = input("Enter the model of the phone: ")
p1 = input("Enter the price of the phone: ")
class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price
    def get_phone_info(self):
        return 'The price for ' + self.__make + " "+ self.__model + ' is $' + self.__price
p = Phone(m1, m2, p1)
print(p.get_phone_info())
######################################################
class SalesPerson:
    def __init__(self, name, commission):
        self.__name = name
        self.__commission = commission

