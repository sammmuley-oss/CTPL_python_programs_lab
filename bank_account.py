

class Bank:
    def input_info(self):
        self.account_no = int(input("Enter account number: "))
        self.balance = float(input("Enter account balance: "))
        self.owner_name = input("Enter account holder name: ")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds")

    def display(self):
        print("\n--- Account Details ---")
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
        print("Holder Name:", self.owner_name)


s1 = Bank()
s2 = Bank()

print("\nEnter details for Account 1")
s1.input_info()
s1.deposit()
s1.withdraw()
s1.display()


print("\nEnter details for Account 2")
s2.input_info()
s2.deposit()
s2.withdraw()
s2.display()


