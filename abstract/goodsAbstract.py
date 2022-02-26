from abc import ABC, abstractmethod


class Goods(ABC):

    def __init__(self, title, price, count, percent):
        self.title = title
        self.price = price
        self.count = count
        self.percent = percent

    def find_summary(self):
        return self.price * self.count

    @abstractmethod
    def find_profit(self, percent):
        pass


class Digital(Goods):

    def __init__(self, title, price, count, percent):
        super().__init__(title, price, count, percent)

    def find_profit(self):
        print(self.find_summary() * self.percent)
        return self.find_summary() * self.percent


class Piece(Digital):
    rate = 2

    def __init__(self, title, price, count, percent):
        super().__init__(title, price * self.rate, count, percent)


class ByWeight(Goods):
    def __init__(self, title, price, count, percent):
        super().__init__(title, price, count, percent)

    def find_profit(self):
        if self.count > 100:
            print(self.find_summary() * self.percent * 0.85)
            return self.find_summary() * self.percent * 0.85
        elif self.count > 10:
            print(self.find_summary() * self.percent * 0.95)
            return self.find_summary() * self.percent * 0.95
        else:
            print(self.find_summary() * self.percent)
            return self.find_summary() * self.percent


print("Доходы с продаж: цифровой, поштучный и весовой")
dg = Digital('digital good', 100, 16, 0.2)
dg.find_profit()

pc = Piece('piece good', dg.price, 16, 0.2)
pc.find_profit()

bw = ByWeight('weight good', 100, 16, 0.2)
bw.find_profit()


