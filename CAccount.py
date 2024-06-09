class CAccount:
    bsb_no = 1246

    def __init__(self, acc_no, acc_type, balance, min_amount=50.00):
        self.accNo = acc_no
        self.accType = acc_type
        self.bal = balance
        self.minAmt = min_amount

    def get_acc_no(self):
        return self.accNo

    def get_acc_type(self):
        return self.accType

    def get_acc_bal(self):
        return self.bal

    def get_min_amt(self):
        return self.minAmt

    def deposit(self, deposit_amount):
        if isinstance(deposit_amount, (int, float)):
            if deposit_amount < self.minAmt:
                print("Account Number : " + str(self.accNo) + "\n" +  # Convert accNo to str
                "Deposit Amount: " + str(deposit_amount) + "\n" +
                "Minimum Amount: " + str(self.minAmt) + "\n" +  # Convert bal to str
                "Error: " + "The deposit should be minimum of" + str(self.minAmt) + "\n")
            else:
                self.bal += deposit_amount
                print("Account Number : " + str(self.accNo) + "\n" +  # Convert accNo to str
                        "Deposit Amount: " + str(deposit_amount) + "\n" +
                        "Closing Amount: " + str(self.bal) + "\n" +  # Convert bal to str
                        "The transaction was successful" + "\n")
        else:
            print("Invalid Input")

    def __str__(self):
        return ("Account Number : " + str(self.accNo) + "\n" +  # Convert accNo to str
                "Account Type : " + self.accType + "\n" +
                "Balance : " + str(self.bal) + "\n" +  # Convert bal to str
                "Min Amount : " + str(self.minAmt) + "\n")  # Convert minAmt to str


