class Account:
    '''Account class containing private account number and balance attributes'''
    def __init__(self, accnumber, balance):
        self.__accnumber = accnumber
        self.__balance = balance

    def get_balance(self):
        return self.__balance

class SBAccount(Account):
    def __init__(self, accnumber, init_balance):
        super().__init__(accnumber, init_balance)

    def deposit(self, amount):
        if amount >= 0:
            self._Account__balance += amount  # Accessing the protected variable
            print(f"Deposited: {amount}. New balance: {self.get_balance()}")

    def withdraw(self, amount):
        if self.get_balance() > 1000 and amount <= self.get_balance() - 1000:
            self._Account__balance -= amount  # Accessing the protected variable
            print(f"Withdrew: {amount}. New balance: {self.get_balance()}")
        else:
            print("Not Enough Balance or minimum balance condition not met.")

    def calc_interest(self):
        interest = self.get_balance() * 0.04
        print(f"It's been a year, and this is your Interest Accumulated: {interest}")
        new_balance = self.get_balance() + interest
        print(f"The balance after interest is: {new_balance}")

class FDAccount(Account):
    def __init__(self, accno, period, deposit_amt):
        super().__init__(accno, deposit_amt)
        self.period = period
        self.deposit_amt = deposit_amt

    def calc_interest(self):
        interest = self.deposit_amt * 0.0825 * self.period
        return interest

    def close(self):
        total_amount = self.deposit_amt + self.calc_interest()
        print(f"FD Account closed. Total amount received: {total_amount}")

class Customer:
    def __init__(self, cust_id, name, address):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.account = None

    def create_account(self, acc_type, accnumber, balance=None, period=None, deposit_amt=None):
        if acc_type == "SB":
            self.account = SBAccount(accnumber, balance)
            print("Savings Account created.")
        elif acc_type == "FD":
            self.account = FDAccount(accnumber, period, deposit_amt)
            print("Fixed Deposit Account created.")
        else:
            print("Invalid account type")

    def transaction(self, trans_type, amount=None):
        if isinstance(self.account, SBAccount):
            if trans_type == "withdraw":
                self.account.withdraw(amount)
            elif trans_type == "deposit":
                self.account.deposit(amount)
            elif trans_type == "calc_interest":
                self.account.calc_interest()
        elif isinstance(self.account, FDAccount):
            if trans_type == "close":
                self.account.close()
        else:
            print("No account exists for this customer.")

class BankDemo:
    def main(self):
        n = int(input("Enter the number of Customers: "))
        customer_list = []
        
        for i in range(n):
            name = input("Enter name of the Customer: ")
            cust_id = input("Enter the customer ID of the Customer: ")
            address = input("Enter the address of the Customer: ")
            customer_list.append(Customer(cust_id, name, address))
        
        while True:
            print(f"\nWhich customer menu do you want to enter (1 to {n} or 0 to exit):", end=' ')
            x = int(input())
            if x == 0:
                break
            
            if 1 <= x <= n:
                customer = customer_list[x - 1]
                print(f"\nWelcome {customer.name}!\nWhat operation do you want to perform?\n\t1. Create Account\n\t2. Deposit\n\t3. Withdraw\n\t4. Calculate Interest\n\t5. Close FD Account")
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    acc_type = input("Enter account type (SB/FD): ")
                    accnumber = input("Enter account number: ")
                    if acc_type == "SB":
                        balance = float(input("Enter initial balance: "))
                        customer.create_account(acc_type, accnumber, balance)
                    elif acc_type == "FD":
                        period = int(input("Enter FD period in years: "))
                        deposit_amt = float(input("Enter deposit amount: "))
                        customer.create_account(acc_type, accnumber, deposit_amt=deposit_amt, period=period)

                elif choice in [2, 3, 4] and isinstance(customer.account, SBAccount):
                    amount = float(input("Enter amount: "))
                    if choice == 2:
                        customer.transaction("deposit", amount)
                    elif choice == 3:
                        customer.transaction("withdraw", amount)
                    elif choice == 4:
                        customer.transaction("calc_interest")

                elif choice == 5 and isinstance(customer.account, FDAccount):
                    customer.transaction("close")

                else:
                    print("Invalid operation or account type.")
            else:
                print("Invalid customer selection.")

if __name__ == "__main__":
    bank_demo = BankDemo()
    bank_demo.main()
