class Order:
    count_id = 0
    def __init__(self, food_img, food_name, quantity, price):
        Order.count_id += 1
        self.__order_id = Order.count_id
        self.__food_img = food_img
        self.__food_name = food_name
        self.__quantity = quantity
        self.__price = price
    def get_order_id(self):
        return self.__order_id

    def get_food_img(self):
        return self.__food_img

    def get_food_name(self):
        return self.__food_name

    def get_quanity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_food_img(self, food_img):
        self.__food_img = food_img

    def set_food_name(self, food_name):
        self.__food_name = food_name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price
