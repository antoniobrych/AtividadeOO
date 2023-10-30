from products import *
from salesoperation import *

#TODO - testar o codiguinho, usar as brands enumeradas

kop_bar = Chocolate(45.32,"A01392","Kopenhagen","Brasil","Tablete Clássico",42,100)


my_shoe = Shoe(450.99,"S01221",42,"Puma")


my_bottle = Bottle(99.99,"P03444","Termolar",1000)
    

my_inv = Inventory()
my_inv.add_item("A01392",21)
my_inv.summary()