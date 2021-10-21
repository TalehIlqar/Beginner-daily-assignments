class BankAccount():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def pulqoymaq(self, amount):
        self.balance += amount
        pr = f'''
        {amount} mebleg elave olundu
        Balance {self.balance - self.balance * 0.05} oldu
        '''
        return pr
    
    def pulchekme(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            pr = f'''
            {amount} mebleg silindi
            Tutulan faiz - {self.balance * 0.05} 
            Balansda  {self.balance - self.balance * 0.05} qaldi
            '''
            return pr
        return "Balansinizda kifayet qeder yoxdur"



    def faiztutmaq(self):
        self.balance -= self.balance * 0.05
        pr = f'''
        
        balans - {self.balance}
        '''
        return pr


    def display(self):
        pr = f'''
        Acount_number: {self.account_number}
        Name: {self.name}
        Balans: {self.balance}
        '''
        return pr

b = BankAccount(89273, "Taleh", 1000)
print(b.pulqoymaq(400))
print(b.pulchekme(500))
print(b.faiztutmaq())
print(b.display())