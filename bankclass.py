class Bank:
    def __init__(self):
        self.account_number = ""
        self.balance = 0
        self.name = 0

    def input_data(self):
        self.name = input("Enter the name: ")
        self.account_number = int(input("Enter the account number: "))
        self.balance= int(input("Enter the account balance: "))

    def display_data(self):
        print("\nStudent Details\n")
        print("Account holder name:", self.name)
        print("Account Number:", self.account_number)
        print("Available Balance:", self.balance)


students = []

n = int(input("Enter the no. of students: "))

for i in range(n):
    print(f"\n Account Details /n}")
    s = Bank()
    s.input_data()
    Bank.append(s)

print("\n--------Bank Details---------\n")

for s in Bank:
    s.display_data()
