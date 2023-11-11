
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return "Beep beep!"


class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        return "Charging..."


class Computerized:
    def __init__(self, software_version):
        self.software_version = software_version

    def update_software(self):
        return "Updating software to version " + self.software_version

class ElectricVehicle(Vehicle, Electric, Computerized):
    def __init__(self, brand, battery_capacity, software_version):
        Vehicle.__init__(self, brand)
        Electric.__init__(self, battery_capacity)
        Computerized.__init__(self, software_version)


    def display_vehicle_info(self):
        return (f"This is a {self.brand} with a battery capacity of {self.battery_capacity} kWh "
                f"and running software version {self.software_version}.")



tesla_model_s = ElectricVehicle('Tesla Model S', 100, '2023.4.1')


vehicle_info = tesla_model_s.display_vehicle_info()
honk_sound = tesla_model_s.honk()
charging_message = tesla_model_s.charge()
software_update_message = tesla_model_s.update_software()

print(vehicle_info)
print(honk_sound)
print(charging_message)
print(software_update_message)

(vehicle_info, honk_sound, charging_message, software_update_message)
