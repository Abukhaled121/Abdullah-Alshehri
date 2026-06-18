# class student():
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
        



# s1 =student("Sara", 17, "11A")
# s2 =student("Ahmed", 18, "12B")

# print(s1.name,s1.age,s1.gender)
# print(s2.name,s2.age,s2.gender)




# class car ():
#     def __init__(self,Brand,model,color):
#         self.Brand=Brand
#         self.model=model
#         self.color=color
#     def describe (self):
#         print(f"this is a {self.color} {self.Brand} {self.model}")

# c1 = car("toyota","corolla","red")
# c1.describe()


class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def Deposit (self,amount):
        self.balance+=amount
    def withdraw (self,amount):
        self.balance-=amount
    def show (self):
        print (f"{self.owner} has {self.balance} SAR")


b1=BankAccount("Sara",1000)
b1.Deposit(500)
b1.withdraw(300)
b1.show()
