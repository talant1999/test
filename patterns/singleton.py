class DB:
    __instance = None

    def __init__(self):
        connect = open()

    @staticmethod
    def get_instance():
        if DB.__instance == None:
            DB.__instance = DB()
        return DB.__instance

    def select(self, query):
        pass

    def update(self, query):
        pass

    def insert(self, query):
        pass

    def delete(self, query):
        pass


class Good:
    def __init__(self):
        db = DB.get_instance()

    def getGoods(self):
        return self.db.select("Select * from Goods")

    def addGood(self):
        return self.db.insert("...")


class User:
    def __init__(self):
        db = DB.get_instance()

    def getUsers(self):
        return self.db.select("Select * from Goods")

    def addUser(self):
        return self.db.insert("...")


