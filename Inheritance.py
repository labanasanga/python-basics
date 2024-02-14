class Mpesa:
    def __init__(self, account_balance , phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self , amount , recepient ):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print (f"{amount} KES sent to {recepient} succesfully ")
        else:
            print (f"Insufficient Balance")


class Personal_Mpesa(Mpesa):
    def __init__(self , account_balance , phone_number , id_number):
        super().__init__(account_balance , phone_number)
        self.id_number = id_number
    def buy_airtime(self , amount ):
        if self.account_balance >= amount :
            self.account_balance -= amount
            print (f"{amount} KES airtime purchased succesfully")
        else:
            print (f"Insufficient Balance")

class Business_Mpesa(Mpesa):
    def __init__(self , account_balance , phone_number ,Business_name):
        super().__init__(account_balance , phone_number)
        self.business_name = Business_name

        print(f"Your {Business_name} balance of phone no {self.phone_number} is : {self.account_balance }")
    def receive_money(self , amount ):
        self.account_balance += amount
        print (f"{amount} KES received succesfully")
        print(f"Your account balance is {self.account_balance - amount }  KES")

personal = Personal_Mpesa(500 , 798162561, 22515345 )
personal.send_money( 400 , 798162561)
personal.buy_airtime(50)
business = Business_Mpesa(350, 798162561, "M-pesa")
business.receive_money( 51 )











