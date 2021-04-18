class Budget:

   def __init__(self, name,  amount, balance):
      self.name= name
      self.amount = amount
      self.balance = balance
   def expense(self):
      print(f'{self.name} monthly expenses')

   def deposit(self):
       amount = float(input("Enter amount to be deposited: "))
       self.balance += amount
       print("\n Amount Deposited:", amount)
   def withdraw(self):
       amount = float (input("Enter amount to be withdrawn: "))
       if self.balance >= amount:
          print("\n you withdrew : ", amount)
       else:
           print("\n insufficient balance ")
   def display(self):
        print("\n Net available balance =", self.balance)

   def trasfer(self, from_budget_1, to_budget_2, to_budget_3, amount) :
        from_budget_1.withdraw(amount)
        to_budget_2(amount)
        to_budget_3(amount)



budget_1 = Budget('food', 5000, 000)
budget_1.deposit()
budget_1.withdraw()
budget_1.display()
budget_2 = Budget('clothing', 3000, 000)
budget_2.deposit()
budget_2.withdraw()
budget_2.display()
budget_3 = Budget('entertainment', 1000,000)
budget_3.deposit()
budget_3.withdraw()
budget_3.display()
Budget.transfer(budget_1, budget_2, budget_3)
budget_1.expense()