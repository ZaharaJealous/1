class SalesPerson:
	def __init__(self):
		self.__name = None
		self.__commission = 0
	def set_name(self,name):
		self.__name = name
	def get_name(self):
		return self.__name
	def salesperson_commission(self,payment):
		self.__commission = 0.02 * payment
	def __str__(self):
		s = "Commission of Salesperson {} is ${:.2f}".format(self.__name, self.__commission)
		return s
input_name = input("Enter salesperson name: ")
input_payment = float(input("Enter payment received by salesperson: "))
sp = SalesPerson()
sp.set_name(input_name)
sp.salesperson_commission(input_payment)
print(sp.__str__())

class Phone:
	count = 0
	def __init__(self):
		self.__make = None
		self.__model = None
		self.__price = 0
		self.__class__.count += 1
	def set_make(self, make):
		self.__make = make
	def set_model(self, model):
		self.__model = model
	def set_price(self, price):
		if price.isnumeric():
			self.__price = price
		else:
			print("price should consist of numbers")
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
sp_name = input("Enter salesperson name: ")
sp_payment = float(input("Enter payment received: "))
s1 = SalesPerson()
s1.set_name(sp_name)
s1.salesperson_commission(sp_payment)
print(s1)
