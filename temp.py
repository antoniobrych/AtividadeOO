class Product():
    def __init__(self,productype,barcode):
        self.barcode = barcode
        self.productype = productype
    
    def price(self,price):
        self.price = price
    
    
class Shoe(Product):
    def __init__(self,productype,barcode,size):
        super().__init__(productype='Shoe',barcode=barcode)
        self.size = size

class Bottle(Product):
    def __init__(self,barcode,volum):
        super().__init__(productype='Bottle',barcode=barcode)
        self.volum = volum
        
