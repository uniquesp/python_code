class Car :
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyataCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyataCar):
    def __init__(self, type):
        self.type = type


Car().start()
print(Car().color)
c1 = ToyataCar("fortuner")
c1.stop()
print(c1.color)

