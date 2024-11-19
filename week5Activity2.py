class Vehicle:
    def move(self):
        raise NotImplementedError("Move() method must be implemented")

class Car(Vehicle):
    def move(self):
        return "DRiving"
    
class Airplane(Vehicle):
    def move(self):
        return "Flying"
    
for Vehicle in[Car() , Airplane()]:
        print(Vehicle.move)