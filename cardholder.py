class cardholder:
    def __init__(self,cardnum,pin,firstname,lastname,balance):
        self.cardnum=cardnum
        self.pin=pin
        self.firstname=firstname
        self.lastname=lastname
        self.balance=balance
    def get_cardnum(self):
        return self.cardnum
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
    

    def set_cardnum(self,newval):
        self.cardnum=newval
    def set_pin(self,newval):
        self.pin=newval
    def set_firstname(self,newval):
        self.firstname=newval
    def set_lastname(self,newval):
        self.lastname=newval
    def set_balance(self,newval):
        self.balance=newval

    def print_out(self):
        print("Card:",self.cardnum)
        print("pin:",self.pin)
        print("First Name:",self.firstname)
        print("Last Name:",self.lastname)
        print("Balance:",self.balance)

