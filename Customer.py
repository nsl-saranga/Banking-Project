from SAccount import SAccount
from CAccount import CAccount


class Customer:

    def __init__(self, cust_no, cust_name, age, city, acc_obj):
        self.custNo = cust_no
        self.custName = cust_name
        self.age = age
        self.city = city

        if isinstance(acc_obj, (SAccount, CAccount)):
            self.accObj = acc_obj
        else:
            raise ValueError("Not a valid account object")

    def get_cust_no(self):
        return self.custNo

    def get_cust_name(self):
        return self.custName

    def get_age(self):
        return self.age

    def get_city(self):
        return self.city

    def get_acc_obj(self):
        return self.accObj

    def __str__(self):
        return ("Customer N0 : " + str(self.custNo) + "\n" +
                "Customer Name : " + self.custName + "\n" +
                "Age : " + str(self.age) + "\n" +
                "City : " + str(self.city))