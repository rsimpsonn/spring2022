from dataclasses import dataclass

@dataclass
class Account:
    id : int
    balance : float

@dataclass
class Customer:
    name : str
    acct : Account

all_custs = [Customer("kathi", Account(5, 225)),
             Customer("milda", Account(2, 300))]

accts_list = [Account(1, 100),
              Account(2, 300),
              Account(3, 200),
              Account(4,  75),
              Account(5, 225)]
