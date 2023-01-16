import Guest
class Member(Guest.Guest):
    count_id = 0
    def __init__(self, first_name, last_name, gender, email, birthday, address, payment_method, credit_number, exp_number, remarks):
        super().__init__(address, payment_method, credit_number, exp_number, remarks)
        Member.count_id += 1
        self.__member_id = Member.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__birthday = birthday
    def get_member_id(self):
        return self.__member_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_gender(self):
        return self.__gender
    def get_email(self):
        return self.__email
    def get_birthday(self):
        return self.__birthday
    def set_member_id(self, member_id):
        self.__member_id = member_id
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_gender(self, gender):
        self.__gender = gender
    def set_email(self, email):
        self.__email = email
    def set_birthday(self, birthday):
        self.__birthday = birthday


    def __reduce__(self):
        return (self.__class__,
                (self.__member_id,
                 self.__first_name,
                 self.__last_name,
                 self.__gender,
                 self.__email,
                 self.__birthday,
                 self.get_address(),
                 self.get_payment_method,
                 self.get_credit_number(),
                 self.get_exp_number(),
                 self.get_remarks))

