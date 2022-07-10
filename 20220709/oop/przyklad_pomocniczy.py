class Engine:
    def __init__(self, capacity, type):
        self.capacity = capacity
        self.type = type


class Car:
    def __init__(self, name, engine: Engine):
        self.name = name
        self.engine = engine
