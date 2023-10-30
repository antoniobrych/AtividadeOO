class Product():
    def __init__(self,price,productype,barcode,brand):
        self.barcode = barcode
        self.productype = productype
        self.price = price
        self.brand = brand
        
    #Ve quanto custa o produto
    def price(self):
        return self.price

class Shoe(Product):
    
    #A inicialização do sapato precisa do tamanho do sapato
    def __init__(self,price,productype,barcode,size,brand):
        super().__init__(price=price,productype='Shoe',barcode=barcode)
        self.size = size
    
    def __str__(self):
        return f"O preço do sapato com tamanho {self.size}, da marca {self.brand} é {self.price}."
    
    
class Bottle(Product):
    
    #A inicialização da garrafa precisa do volume da garrafa
    def __init__(self,price,productype,barcode,brand,volum):
        super().__init__(price=price,productype='Bottle',barcode=barcode,brand=brand)
        self.volum = volum
    
    def __str__(self):
        return f"O preço da garrafa com volume {self.volum}, da marca {self.brand} é {self.price}."
    
