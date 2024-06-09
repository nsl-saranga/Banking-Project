class SAccount:
    bsb_no = 1246

    def __init__(self, acc_no, acc_type, balance, max_amount=500.00):
        self.accNo = acc_no
        self.accType = acc_type
        self.bal = balance
        self.maxAmt = max_amount

    def get_acc_no(self):
        return self.accNo

    def get_acc_type(self):
        return self.accType

    def get_acc_bal(self):
        return self.bal

    def get_max_amt(self):
        return self.maxAmt

    def deposit(self, deposit_amount):
        if isinstance(deposit_amount, (int, float)):
            if deposit_amount > self.maxAmt:
                print("Account Number : " + str(self.accNo) + "\n" +  # Convert accNo to str
                        "Deposit Amount: " + str(deposit_amount) + "\n" +
                        "Maximum Amount: " + str(self.maxAmt) + "\n" +  # Convert bal to str
                        "Error: " + "The deposit should be maximum of" + str(self.maxAmt) + "\n")
            else:
                self.bal += deposit_amount
                print("Account Number : " + str(self.accNo) + "\n" +  # Convert accNo to str
                        "Deposit Amount: " + str(deposit_amount) + "\n" +
                        "Closing Amount: " + str(self.bal) + "\n" +  # Convert bal to str
                        "The transaction was successful" + "\n")
        else:
            print("Invalid Input")

    def __str__(self):
        return ("Account Number : " + str(self.accNo) + "\n" +
                "Account Type : " + self.accType + "\n" +
                "Balance : " + str(self.bal) + "\n" +
                "Max Amount : " + str(self.maxAmt) + "\n")



