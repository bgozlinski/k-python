class Vehicle:
    description: str = "Pojazdy wszelkie"
    count = 0

    def __init__(self, name: str):
        # Vehicle.count += 1
        self.__class__.count += 1
        self.name = name

    def __del__(self):
        self.__class__.count -= 1
        # Vehicle.count -=

    def __repr__(self):
        return self.name

    def drive(self):
        print(f"{self} is driving")

    @property
    def name_len(self):
        return len(self.name)

    @property
    def energy(self):
        self._energy


f = Vehicle("Ford")
v = Vehicle("Volkswagen")

f.drive()
print(f.name_len)

f.name = "Ford Mustang"
print(f.name_len)

print(v)  # __str__
print([v])  # __repr__

print(f.count)


del v

print(f.count)
