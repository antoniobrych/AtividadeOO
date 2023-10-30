from products import *
from enum import Enum

class Brand(Enum):
    NIKE = "Nike"
    ADIDAS = "Adidas"
    REEBOK = "Reebok"
    COCA_COLA = "Coca-Cola"
    PEPSI = "Pepsi"
    NESTLE = "Nestlé"
    LINDT = "Lindt"

class Inventory():
    
    #Inicia uma lista vazia 
    def __init__(self):
        self.inv = []
    
    def add_item(self,barcode,amount):
        item = [barcode,amount]
        self.inv.append(item)
    
    # Mostra o que tem no inventário
    def summary(self):
        print(self.inv)
    
    # Vende um produto
    def sell_product(self, product):
       if product in self.inv:
           self.inv.remove(product)
       else:
           raise ProductNotFoundError("Product not found in the inventory.")

    # Para devolver um produto    
    def return_product(self, product):
        self.inv.append(product)

    def restock_product(self, product, quantity):
        # Supondo que a quantidade seja adicionada ao estoque
        for i in range(quantity):
            self.add_item(product)

class ProductNotFoundError(Exception):
    pass
