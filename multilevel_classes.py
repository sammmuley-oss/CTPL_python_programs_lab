
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model:", self.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def show_battery(self):
        print("Battery Capacity:", self.battery_capacity, "kWh")

ecar = ElectricCar("Tesla", "Model X", 100)

ecar.show_brand()      
ecar.show_model()      
ecar.show_battery()    