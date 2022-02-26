class Auto:
    def __init__(self, body, engine):
        self.__isStart = False
        self.__body = body
        self.__engine = engine

    def on(self):
        self.__isStart = True

    def off(self):
        self.__isStart = False

    def __str__(self):
        self.__isStart = 'работает' if self.__isStart else 'не работает'
        return f"Машина {self.__isStart}.\nТип двигателя: {self.__engine.getTypeEngine}, Номер двигателя: {self.__engine.getNumber}\nТип кузова: {self.__body.getTypeBody}, Цвет кузова: {self.__body.getColor}"


class Engine:
    def __init__(self, typeEngine, number):
        self.__typeEngine = typeEngine
        self.__number = number

    @property
    def getTypeEngine(self):
        return self.__typeEngine

    @property
    def getNumber(self):
        return self.__number


class Body:
    def __init__(self, typeBody, color):
        self.__typeBody = typeBody
        self.__color = color

    @property
    def getTypeBody(self):
        return self.__typeBody

    @property
    def getColor(self):
        return self.__color


class BuilderAuto:
    def build_body(self, typeBody, color):
        return Body(typeBody, color)

    def build_engine(self, typeEngine, number):
        return Engine(typeEngine, number)

    def create_builder(self, typeBody, color, typeEngine, number):
        body = self.build_body(typeBody, color)
        engine = self.build_engine(typeEngine, number)
        return Auto(body, engine)


builder = BuilderAuto()
auto1 = builder.create_builder("Седан","Серый","Дизель","1253627")
auto1.on()
print(auto1)
