class FastFood:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def quantity_increase(self):
        if(self.__check_availability()==True):
            self.quantity += 5
    def total_value(self):
        return self.price * self.quantity

    def __check_availability(self):
        if self.quantity == 0:
            return True
        else:
            return False

    def printProduct(self):
        print(f"Product name is: {self.name}, price is: {self.price} and quantity of product is: {self.quantity}")

pizza = FastFood("Pepperoni", 10, 5)
pasta = FastFood("Carbonara", 14, 10)
duner = FastFood("Duner", 10, 0)

print("Initial printing")
pizza.printProduct()
pasta.printProduct()
duner.printProduct()
print("After operations")
pizza.quantity_increase()
pizza.printProduct()
pasta.quantity_increase()
pasta.printProduct()
duner.quantity_increase()
duner.printProduct()
print("Total value of products:")
print("Total price: ",pizza.total_value())
print("Total price: ",pasta.total_value())
print("Total price: ",duner.total_value())
