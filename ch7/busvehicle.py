class Vehicle:
    def __init__(self, setting_capacity):
        self.capacity = setting_capacity

    def get_capacity(self):
        return self.capacity * 100
    
    
class bus(Vehicle):
    def __init__(self, setting_capacity):
        super().__init__(setting_capacity)

    def get_fare(self):
        vehical_fare = super().get_capacity()
        maintenance_charge = vehical_fare * 0.1
        total_fare = vehical_fare + maintenance_charge
        return total_fare
    
    
vehicle1 = Vehicle(50)
print("Vehicle Capacity:", vehicle1.get_capacity())


bus1 = bus(50)
print("Bus Total Fare:", bus1.get_fare())