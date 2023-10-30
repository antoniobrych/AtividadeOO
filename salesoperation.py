from products import *

class Sales():
    total_sales = 0
    #Métodos para vender os produtos criados
    def sale():
        
        total_sales += 1
    
class Inventory():
    def __init__(self,barcode,amount,inv=[]):
        self.barcode = barcode
        self.amount = amount
        self.inv = inv
    def add_item(self,barcode,amount):
        item = [barcode,amount]
        item.append(inv)
    def summary(self):
        print(inv)



class SalesOperationError():
    #Erros possiveis nas operçãoes de venda
    pass

kop_bar = Chocolate(45.32,"A01392","Kopenhagen","Brasil","Tablete Clássico",42,100)
my_shoe = Shoe(450.99,"S01221",42,"Puma")
my_bottle = Bottle(99.99,"P03444","Termolar",1000)
print(my_bottle)
