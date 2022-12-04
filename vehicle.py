
from abc import ABC, abstractmethod

from pyautogui import sleep


class Vehicle(ABC):
    speeds = {
        "car": 30,
        "bike": 50,
        "cng": 15
    }

    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.status = "available"
        self.driver = driver
        self.speed = self.speeds[self.vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "Unavailable"
        print(self.vehicle_type, self.license_plate, "stared")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(
                f"driving: {self.license_plate} current position: {i} of {distance}")
        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Complete trip")


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "Unavailable"
        print(self.vehicle_type, self.license_plate, "stared")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(
                f"driving: {self.license_plate} current position: {i} of {distance}")
        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Complete trip")


class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.status = "Unavailable"
        print(self.vehicle_type, self.license_plate, "stared")
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(
                f"driving: {self.license_plate} current position: {i} of {distance}")
        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Complete trip")
