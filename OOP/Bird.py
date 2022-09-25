class Bird:
    ruClassName = "Птица"
    objInstancesCount = 0

    def __init__(self, name, id, age):
        self._name = name
        self._id = id
        self._age = age
        Bird.objInstancesCount = Bird.objInstancesCount + 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if (age >= 0):
            self._age = age
        else:
            self._age = 0

    @property
    def id(self):
        return self._id

    def info(self):
        print("Имя: " + self._name)
        print("Идентификационный номер: " + str(self._id))
        print("Возраст: " + str(self._age))


class Duck(Bird):
    species = "Утка"

    def __init__(self, name, id, age, fly_speed, fly_height):
        super().__init__(name, id, age)
        self.__fly_speed = fly_speed
        self.__fly_height = fly_height

    @property
    def fly_speed(self):
        return self.__fly_speed

    @fly_speed.setter
    def fly_speed(self, fly_speed):
        self.__fly_speed = fly_speed

    @property
    def fly_height(self):
        return self.__fly_height

    @fly_height.setter
    def fly_height(self, fly_height):
        self.__fly_height = fly_height

    def info(self):
        super().info()
        print("Вид: " + Duck.species)
        print("Скорость полета: " + str(self.__fly_speed))
        print("Высота полета: " + str(self.__fly_height))


class GalaBacklane(Bird):
    species = "Галапагосский баклан"

    def __init__(self, name, id, age, population):
        super().__init__(name, id, age)
        self.__population = population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    def info(self):
        super().info()
        print("Вид: " + GalaBacklane.species)
        print("Количество особей: " + str(self.__population))


g = GalaBacklane("galaBacklane1", 22, 2, 60)
g.info()

b = Bird("bird1", 9, 4)
b.info()

d = Duck("duck1", 77, 9, 110, 5)
d.info()
