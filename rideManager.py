

class RideManager:

    def __init__(self):
        print("ride manager activated")
        self.__income = 0
        self.__trip_history = []
        self.__available_car = []
        self.__available_bike = []
        self.__available_cng = []

    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_car.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bike.append(vehicle)
        elif vehicle_type == 'cng':
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_car

    def total_income(self):
        return self.__income

    def find_a_vehicle(self, rider, vehicle_type, destination):

        if vehicle_type == "car":
            vehicles = self.__available_car
        elif vehicle_type == 'bike':
            vehicles = self.__available_bike
        else:
            vehicles = self.__available_cng
        if len(vehicles) == 0:
            print("sorry no  available")
            return False
        for item in vehicles:
            print("potential", rider.location, item.driver.location)
            if abs(rider.location - item.driver.location) < 10:
                distance = abs(rider.location - destination)
                fare = distance * item.rate
                if rider.balance < fare:
                    print("you do not have enough money for this trip.",
                          fare, rider.balance)
                    return False
                if item.status == 'available':

                    vehicles.remove(item)
                    trip_info = f' match{vehicle_type} for {rider.name} for fare {fare} with {item.driver.name} started: {rider.location} to {destination}\n'
                    rider.start_a_trip(fare, trip_info)
                    item.driver.start_a_trip(rider.location,
                                             destination, fare*0.8, trip_info)
                    self.__income += fare * 0.2
                    self.__trip_history.append(trip_info)

                    return True


uber = RideManager()
