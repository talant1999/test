class Coffee:

    def grindCoffee(self):
        pass

    def makeCoffee(self):
        pass

    def sendCoffee(self):
        pass


class Americano(Coffee):
    def __init__(self):
        self.title = "Американо"

    pass


class Cappuchino(Coffee):
    def __init__(self):
        self.title = "Капучино"

    pass


class Expresso(Coffee):
    def __init__(self):
        self.title = "Экспрессо"

    pass


class CoffeeFactory:
    def createCoffee(self, type):
        if type == "Американо":
            coffee = Americano()
        elif type == "Экспрессо":
            coffee = Expresso()
        elif type == "Капучино":
            coffee = Cappuchino()
        return coffee


class CoffeeMachine:
    def getCoffee(self, coffeeFactory):
        coffeeFactory.grindCoffee()
        coffeeFactory.makeCoffee()
        coffeeFactory.sendCoffee()
        print(f"Кофе {coffeeFactory.title} готов")
        return coffeeFactory

factory = CoffeeFactory().createCoffee('Капучино')
CoffeeMachine().getCoffee(factory)
