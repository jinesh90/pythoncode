"""
This python example of builder pattern
Main parts of builder pattern are
- Complex Object.
- Builder Interface.
- Builder Concrete Implementation.
- Director.

and finally product
"""

# This is Complex Object that want to build into Final product aka car.
class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: {}".format(self.__body.shape))
        print("engine horsepower: {}".format(self.__engine.horsepower))
        print("tire size: {}".format(self.__wheels[0].size))

# Car parts
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None


# Director Example, which set builder and has method to build complex product ( get_car)

class Director:
    __builder = None

    def set_builder(self,builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        # first get body and fit it
        body = self.__builder.get_body()
        car.set_body(body)

        #get engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        #wheels
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1
        return car


# Builder Abstract
class BuilderInterface:
    def get_wheel(self):
        pass

    def get_engine(self):
        pass

    def get_body(self):
        pass

#Builder Implementation
class JeepBuilder(BuilderInterface):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 412
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body

class BMWBuilder(BuilderInterface):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 19
        return  wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 600
        return  engine

    def get_body(self):
        body = Body()
        body.shape = "Sedan"
        return body



def main():
    # get director
    dir = Director()
    #set builder
    dir.set_builder(JeepBuilder())
    jeep  = dir.get_car()
    print("I am gtting jeep car objcet {}".format(jeep))
    print(jeep.specification())

main()