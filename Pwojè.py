class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: ${self.daily_rate:.2f}")
        #Mwen itilize (:.2f) kise yon fomaje nan notasyon foma,li afiche 2 chif apre pwen desimal la.


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_seats):
        super().__init__(make, model, year, daily_rate)
        self.num_seats = num_seats
        #Mwen itilize komand super() nan sou klas yo poum rele method nan klas paran.

    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seats}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type

    def display_info(self):
        super().display_info()
        print(f"Frame Type: {self.frame_type}")


class Rental:
    def __init__(self, vehicle, rental_days):
        self.vehicle = vehicle
        self.rental_days = rental_days

    def calculate_total_cost(self):
        return self.vehicle.daily_rate * self.rental_days

    def display_receipt(self):
        print("Rental Receipt")
        print("---------------")
        self.vehicle.display_info()
        print(f"Rental Days: {self.rental_days}")
        total_cost = self.calculate_total_cost()
        print(f"Total Cost: ${total_cost:.2f}")


car = Car("Toyota", "Corolla", 2023, 70, 5)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 90, "V-twin")
bicycle = Bicycle("Trek", "FX", 2023, 20, "Hybrid")

car.display_info()
motorcycle.display_info()
bicycle.display_info()

rental_car = Rental(car, 5)
rental_car.display_receipt()

rental_motorcycle = Rental(motorcycle, 4)
rental_motorcycle.display_receipt()

rental_bicycle = Rental(bicycle, 10)
rental_bicycle.display_receipt()
