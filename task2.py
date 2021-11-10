class Product:

    id = 0

    def __init__(self, title: str, price: float, desc: str, size: tuple):
        if not isinstance(title, str):
            raise TypeError('Title should be a string')
        if not isinstance(price, (float, int)):
            raise TypeError('Price should be a number')
        if price <= 0:
            raise ValueError('Price should be more than zero')
        self.id = Product.id
        self.title = title
        self.price = price
        self.desc = desc
        self.width, self.length, self.height = size
        Product.id += 1

    def __str__(self):
        return f'{self.id}: {self.title}; {self.price}'


class Customer:

    id = 0

    def __init__(self, surname: str, name: str, phone: str):

        self.id = Customer.id
        self.surname = surname
        self.name = name
        self.phone = phone
        Customer.id += 1

    def __str__(self):
        return f'{self.id}: {self.surname} {self.name[0]}.'


class Order:

    def __init__(self, customer: Customer, products: list):
        for i, item in enumerate(products):
            if not isinstance(item, Product):
                raise TypeError(f'{i}th product in cart should be Product\'s instance')

        self.customer = customer
        self.cart = products

    def add_product(self, value: Product):
        self.cart.append(value)

    def remove_product(self, value: Product):
        self.cart.remove(value)

    def __str__(self):
        cart_tmp = "\n".join(map(str, self.cart))
        return f'{self.customer}\n{cart_tmp}\nTotal: {self.total_price()}'

    def __iter__(self):
        return OrderIterator(self.cart)

    def total_price(self):
        summa = 0
        for item in self.cart:
            summa += item.price
        return summa

class OrderIterator:
    def __init__(self, goods):
        self.goods = goods
        self.index = 0

    def __next__(self):
        if self.index < len(self.goods):
            self.index = self.index + 1
            return self.goods[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':

    try:
        pr_1 = Product('laptop', 20000, "", (20, 20, 20))
        pr_2 = Product('phone', 30000, "", (21, 23, 25))
        pr_3 = Product('tv', 40000, "", (22, 24, 26))
        pr_4 = Product('smartwatch', 10000, "", (22, 24, 26))

        customer = Customer('Ivanov', 'Ivan', '099-0101011')

        order = Order(customer, [pr_1, pr_2, pr_3, pr_1])
        print(order)
        order.remove_product(pr_3)
        print(order)
        order.add_product(pr_4)
        print(order)
    except Exception as ex:
        print(ex)
