class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Audi', 'R8')  # This is an objcet tied to the vehicle class
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):  # refers to the vehicle class when making this class.
    # initalising the paramters here. this is needed due to faa_id being a new parameter
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # refers to vehicle parameters
        self.faa_id = faa_id  # new parameter that can be added

    # Overrides the moves(self) method in the vehicle class... I think.
    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'SkyHawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yahama', 'GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

# polymorphism - different responese despite the same inputs is polymorphism
print('\n\n')

# just a normal for loop and we used v. We could use x, y etc
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
