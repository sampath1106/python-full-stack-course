#encapsilation in oops 


class bank:
    def __init__(self,amount):
        self.__amount=amount

    def deposit(self,amount):
        self.__value=amount
        self.__amount+=self.__value
        print("self.__value:",self.__value)

    def withdraw(self,amount):
        self.__value=amount
        self.__amount-=self.__value
        print("self.__value:",self.__value)
        
    def balance(self):
        print("balance",self.__amount)
        
b1=bank(999)
b1.deposit(2)
b1.withdraw(1)
b1.balance()
