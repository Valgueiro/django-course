class Product:
    def __init__(self):
        self.name = "Produto qualquer" 
        self.price = 100



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, discount_rate):
        """
        Give a discount of discount_rate on the price
        """
        discount_value = discount_rate*self.price
        self.price = self.price - discount_value
