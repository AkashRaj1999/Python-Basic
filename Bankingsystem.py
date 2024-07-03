class user:
    def __init__(self,name,age) :
        self.name = name 
        self.age = age

    def show_details(self):
        return f"Thank You,{self.age}year old,{self.name.title()}"

class Bank(user):
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, age,balance):
        super().__init__(name, age)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of : {round(self.balance,2)}"

    def deposit(self):
        dp = float(input(f"{self.name.title()},please enter how much you would like to deposit"))
        print("Thank you for depositing -------")
        self.balance =+ dp
        self.total_deposits += 1

        return f"Your balance is now {round(self.balance,2)}"

    def withdraw(self):
        wd = float(input(f"{self.name.title()},please enter how much you would like to withdraw"))
        if self.balance <wd :
            return "You can not withdraw that amount"
        else:
            print("Thank You for withdrawing ---")
            self.balance -= wd
            self.total_withdraws += 1

    def options(user_two):
        print("Thank You for cheating your bank account")
        print("Here are a list of options,please choose the number you wait")

        while True:
            option_choice = int(input("1)see balance\n2)withdraw\n3)deposit\n4)see total withdrawness\n5)see total deposits\n6)Quit\n"))
        
           