# Animal наследует обьект
class Animal(object):
    pass


# класс Dog наследует Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name


# класс Cat наследует Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name


# класс Person наследует обьект
class Person(object):
    def __init__(self, name):
        self.name = name
        # Person композиция животного некоторого вида
        self.pet = None


# класс Employee наследует Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


# класс Fish наследует обьект
class Fish(object):
    pass


# класс Salmon наследует Fish
class Salmon(Fish):
    pass


# класс Halibut наследует Fish
class Halibut(Fish):
    pass


# Барбос наследует Dog
barbos = Dog("Барбос")
# барсик наследует Cat
barsik = Cat("Барсик")
# мэри наследует Person
mary = Person("Маша")
#
mary.pet = barsik
# филька наследует Employee
filka = Employee("Филька", 120000)
#
filka.pet = barbos
# flipper наследует Fish
flipper = Fish()
crouse = Salmon()
harry = Halibut()
