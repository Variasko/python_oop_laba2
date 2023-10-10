class Car:
    color = None
    fuel = None
    mark = None
    horsepower = None

    def go(self):
        ...

    def turn(self):
        ...

    def stop(self):
        ...

    def outputInfo(self, car):
        print(f'color: {car.color}'
              f'\nfuel: {car.fuel}'
              f'\nmark: {car.mark}'
              f'\nhorsepower: {car.horsepower}')

myCar = Car()

myCar.color = 'green'
myCar.fuel = 60
myCar.mark = 'BMW'
myCar.horsepower = '250'

myCar.outputInfo(myCar)