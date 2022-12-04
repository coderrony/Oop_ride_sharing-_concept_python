

import threading
from rideManager import uber
import hashlib
from brta import BRTA
import vehicle
from random import random, randint, choice


license_authority = BRTA()


class UserAlreadyExits(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f"user: {email} already Exits")
        super().__init__(*args)


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email

        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exits = False
        with open('userTwo.txt', 'r') as file:
            if email in file.read():
                already_exits = True

                # raise UserAlreadyExits(self.email)
        file.close()

        if already_exits == False:
            with open('userTwo.txt', 'a') as file:
                file.write(f"{email} {pwd_encrypted}\n")
            file.close()
            print(self.name, "user created")

    @staticmethod
    def log_in(email, password):
        store_pass = ""
        with open("userTwo.txt", "r") as file:

            for line in file.readlines():
                if email in line:
                    store_pass = line.split(" ")[1]
                    break
        file.close()

        if store_pass == hashlib.md5(password.encode()).hexdigest():
            print("Valid user")
        else:
            print("Invalid user")


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.balance = balance

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, fare, trip_info):
        print(f"A trip started for {self.name}")
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            self.valid_driver = False
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver == True:

            if vehicle_type == 'car':
                self.vehicle = vehicle.Car(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = vehicle.Bike(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'cng':
                self.vehicle = vehicle.Cng(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
        else:
            print("you have not pass the driving test please try again")
            pass

    def start_a_trip(self, start, destination, free, trip_info):
        self.earning += free
        self.location = destination
        self.__trip_history.append(trip_info)
        # start a thread
        trip_thread = threading.Thread(
            target=self.vehicle.start_driving, args=(start, destination,))
        trip_thread.start()


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 1000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000)
vehicle_types = ['car', 'bike', 'cng']
for i in range(1, 20):
    driver1 = Driver(f"driver{i}", f'driver{i}@gmail.com',
                     f'driver{i}', randint(0, 30), randint(100, 1000))
    driver1.take_driving_test()
    driver1.register_a_vehicle(
        choice(vehicle_types), randint(10000, 99999), 10)


print(uber.get_available_cars())
uber.find_a_vehicle(rider1, choice(vehicle_types), randint(1, 100))
# uber.find_a_vehicle(rider2, choice(vehicle_types), randint(1, 100))
# uber.find_a_vehicle(rider3, choice(vehicle_types), randint(1, 100))

print(rider1.get_trip_history())
print(uber.total_income())
