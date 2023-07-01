from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)
                break

    def __repr__(self):
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
