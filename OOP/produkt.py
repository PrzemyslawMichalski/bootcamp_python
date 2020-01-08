class Product:
    NEXT_ID = 1

    def __init__(self, id, name, price):
        self.id = Product.NEXT_ID
        self.name = name
        self.price = price
        self.incr_next_id()

        @classmethod
        def incr_next_id(cls):
            cls.NEXT_ID += 1


    def show(self):
        return f"{self.name} ({self.id}), cena: {self.price}"


def test_product():
    pr = Product(1, "woda", 10.99)
    assert pr.id == 1
    assert pr.name == "woda"
    assert pr.price == 10.99

def test_product_show():
    pr = Product(1, "woda", 10.99)
    pr = Product(1, "chleb", 8.99)
    assert pr.show() == "woda (1), cena: 10.99"
    assert pr.show() == "woda (1), cena: 8.99"
