class Product():
    def __init__(self,price,productype,barcode,brand):
        self.barcode = barcode
        self.productype = productype
        self.price = price
        self.brand = brand
        
    #Ve quanto custa o produto
    def price(self):
        return self.price
    
    #Ve o codigo de barras do produto
    def barcode(self):
        return self.barcode       
            
class Shoe(Product):
    
    #A inicialização do sapato precisa do tamanho do sapato
    def __init__(self,price,barcode,size,brand):
        super().__init__(price=price,productype='Shoe',brand=brand,barcode=barcode)
        self.size = size
    
    def __str__(self):
        return f"O preço do sapato com tamanho {self.size}, da marca {self.brand} é {self.price}."    
    
class Bottle(Product):
    
    #A inicialização da garrafa precisa do volume da garrafa
    def __init__(self,price,barcode,brand,volum):
        super().__init__(price=price,productype='Bottle',barcode=barcode,brand=brand)
        self.volum = volum
    
    def __str__(self):
        return f"O preço da garrafa com volume {self.volum}, da marca {self.brand} é {self.price}."
        
class Chocolate(Product):
    
    #inicializando classe Chocolate, onde herda certas propriedades da classe Product
    def __init__(self,price,barcode,brand,origin,model,cocoa_pct,weight):
        super().__init__(price=price,productype='Chocolate Bar',barcode=barcode,brand=brand)
        self.origin = origin
        self.model = model
        self.cocoa_pct = cocoa_pct
        if self.cocoa_pct > 100:
            self.cocoa_pct = 100
        self.weight = weight
    
    def __str__(self):
        return f"O preço do chocolate modelo {self.model}, da marca {self.brand}, produzido em {self.origin}, com {self.cocoa_pct}% de cacau puro, custa {self.price} e pesa {self.weight} gramas"
