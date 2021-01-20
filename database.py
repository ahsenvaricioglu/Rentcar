from car import Car

class Database:
    def __init__(self):
        self.cars = {}
        self._last_car_key = 0

    def add_car(self, cars):
        self._last_car_key += 1
        self.cars[self._last_car_key] = cars
        return self._last_car_key

    def delete_car(self, car_key):
        if car_key in self.cars:
            del self.cars[car_key]

    def get_car(self, car_key):
        car = self.cars.get(car_key)
        if car is None:
            return None
        car_ = Car(car.Model, car.Price, car.Year, car.Color, car.Plate_num, Status = car.Status)
        return car_
    def get_car(self):
        cars = []
        for car_key, car in self.cars.items():
            car_ = Car(car.Model, car.Price, car.Year, car.Color, car.Plate_num, Status = car.Status)
            cars.append((car_key, car_))
        return cars