class Product:
    tax_level = 7

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def tax(self):
        return self.price * self.tax_level / 1000

    @classmethod
    def change_tax_level(cls, rate: int):
        cls.tax_level = rate

    @classmethod
    def create(cls, data):
        return cls(*data)

    @staticmethod
    def tax_levels():
        return [0.07, 0.1]


p = Product("Chleb", 10)
print(Product.tax_level)

p.change_tax_level(10)
print(Product.tax_level)

p2 = Product.create(["piwo", 7])


data = ["Sok", 20]
Product(data[0], data[1])
Product(*data)


data = {"name": "Sok", "price": 20}
Product(**data)
