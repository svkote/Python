# Неявное наследование
class Parent(object):
    def implicit(self):
        print("Родитель")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
