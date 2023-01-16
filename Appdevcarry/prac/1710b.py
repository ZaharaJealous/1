class Customer:
    def set_name(self,name):
        self.name = name
    def set_email(self,email):
        self.email = email
    def get_customer_info(self):
        print(self.name, self.email)
def display_customer_info(customer):
    print(customer.get_customer_info())
c1 = Customer()
c1.set_name("rg")
c1.set_email("rg@fege")
display_customer_info(c1)
###################
class Customer:
    def __init__(self, name, email):
        self.__name = name
    def __str__(self):
        s = "Name: {}, ".format(self.__name,)
        return s
ca1 = Customer("fefe")
print(ca1)
###################
class Counter:
    cn1 = 0
    def __init__(self):
        self.cn2 = 0
    def increase_cn2(self):
        self.cn2 += 1
    def increase_cn1(self):
        self.__class__.cn1 += 1
a1 = Counter()
a1.increase_cn1()
a1.increase_cn2()
a2 = Counter()
a2.increase_cn1()
a2.increase_cn2()
a3 = Counter()
a3.increase_cn1()
a3.increase_cn2()
print('Class variable %d, Data variable %d' %(Counter.cn1, a1.cn2))
######################
#class Customer:
#    def __init__(self,name):
#        self.name = name
#c2 = Customer("zw")
#print(c2.name)
