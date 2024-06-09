from SAccount import SAccount
from CAccount import CAccount
from Customer import Customer

class Bank:
    def main(self):
        account_objects = []
        customer_objects = []

        with open('CAccounts.txt', 'r') as file:
            for line in file:
                data = line.strip().split(';')
                account_number = int(data[0])
                account_type = data[1]
                balance = float(data[2])
                if len(data) > 3:
                    min_amount = float(data[3])
                    account_objects.append(CAccount(account_number,account_type, balance, min_amount))
                else:
                    account_objects.append(CAccount(account_number,account_type, balance))

        with open('SAccounts.txt', 'r') as file:
            for line in file:
                data = line.strip().split(';')
                account_number = int(data[0])
                account_type = data[1]
                balance = float(data[2])
                if len(data) > 3:
                    max_amount = float(data[3])
                    account_objects.append(SAccount(account_number, account_type, balance, max_amount))
                else:
                    account_objects.append(SAccount(account_number, account_type, balance))

        with open('Customers.txt', 'r') as file:
            i = 0
            for line in file:
                data = line.strip().split(';')
                customer_number = int(data[0])
                customer_name = data[1]
                customer_age = int(data[2])
                customer_city = data[3]
                customer_account = account_objects[i]
                i += 1
                customer_objects.append(Customer(customer_number, customer_name, customer_age, customer_city, customer_account))


        print("sds")
        checking_acc = customer_objects[0].get_acc_obj()
        if isinstance(checking_acc, CAccount):
            print("Checking Account Details: \n" + "Account Number :" + str(checking_acc.get_acc_no()) + "\n" + "Account Type :" + str(checking_acc.get_acc_type())+"\n"
                      + "Balance :" + str(checking_acc.get_acc_bal()) + "\n" + "Minimum Amount :" + str(checking_acc.get_min_amt()), "\n"
                    )
        else:
            print("This is not a Checking Account !!")

        saving_acc = customer_objects[5].get_acc_obj()
        if isinstance(saving_acc, SAccount):
            print(
                "Checking Account Details: \n" + "Account Number :" + str(saving_acc.get_acc_no()) + "\n" + "Account Type :"
                + str(saving_acc.get_acc_type()) + "\n" + "Balance :" + str(saving_acc.get_acc_bal()) + "\n" + "Maximum Amount :"
                + str(saving_acc.get_max_amt()) + "\n"
            )
        else:
            print("This is not a Saving Account !!")

        # Invalid deposit transaction on CAccount
        checking_acc.deposit(25.00) # Trying to deposit an amount less than min amount (50.00)

        # Invalid deposit transaction on SAccount
        saving_acc.deposit(550.00) # Trying to deposit an amount greater than max amount (500.00)

        # Valid deposit transaction on CAccount
        checking_acc.deposit(55.00)  # Trying to deposit an amount greater than min amount (50.00)

        # Valid deposit transaction on SAccount
        saving_acc.deposit(450.00)  # Trying to deposit an amount less than max amount (500.00)

        with open('BankingReceipt.txt', 'a') as file:
            file.write("Checking Account Details: \n" + "Account Number :" + str(checking_acc.get_acc_no()) + "\n" +
                       "Account Type :" + str(checking_acc.get_acc_type()) + "\n" + "Balance :" + str(checking_acc.get_acc_bal())
                       + "\n")

        with open('BankingReceipt.txt', 'a') as file:
            file.write("Saving Account Details: \n" + "Account Number :" + str(saving_acc.get_acc_no()) + "\n" +
                       "Account Type :" + str(saving_acc.get_acc_type()) + "\n" + "Balance :" + str(saving_acc.get_acc_bal())
                       + "\n")


if __name__ == "__main__":
    bank = Bank()
    bank.main()