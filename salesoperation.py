from products import *

class Sales():
    total_sales = 0
    #Métodos para vender os produtos criados
    def sale():
        
        total_sales += 1
    
class Inventory():
    def __init__(self):
        self.inv = []
    def add_item(self,barcode,amount):
        item = [barcode,amount]
        self.inv.append(item)
    def summary(self):
        print(self.inv)

my_inv = Inventory()
my_inv.add_item("A01392",21)
my_inv.summary()

class SalesOperationError():
    #Erros possiveis nas operçãoes de venda
    pass

kop_bar = Chocolate(45.32,"A01392","Kopenhagen","Brasil","Tablete Clássico",42,100)
my_shoe = Shoe(450.99,"S01221",42,"Puma")
my_bottle = Bottle(99.99,"P03444","Termolar",1000)
print(my_bottle)
