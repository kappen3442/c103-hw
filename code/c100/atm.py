class Atm:
    def __init__(self,cash,credit,debit) :
      self.cash=cash
      self.credit=credit
      self.debit=debit

    def displaycash(self):
        print("this is how much cash you have")

atmm=Atm(cash="388",credit="4500",debit="200")
print(atmm.debit)
print(atmm.cash)
print(atmm.credit)


atmm.displaycash()