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


# Явное переопределение
class Parent(object):
    def override(self):
        print("Родитель 2")


class Child(Parent):
    def override(self):
        print("Потомок 2")


dad = Parent()
son = Child()

dad.override()
son.override()


# Видоизменение до и после
class Parent(object):
    def altered(self):
        print("Родитеь 3")


class Child(Parent):
    def altered(self):
        print("Потомок 3 до вызова в родителе")
        super(Child, self).altered()
        print("Потомок 3 после вызова в родителе")


dad = Parent()
son = Child()

dad.altered()
son.altered()


# Комбинация взаимодействий
class Parent(object):
    def override(self):
        print("Родитель override")
    def implicit(self):
        print("Родитель")
