class Other(object):
    def override(self):
        print("класс other override")

    def implicit(self):
        print("класс other implicit")

    def altered(self):
        print("класс other altered")


class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("класс child override")

    def altered(self):
        print("Потомок до вызова altered() в классе Other")
        self.other.altered()
        print("Потомок после вызова altered() в классе Other")


son = Child()
son.implicit()
son.override()
son.altered()
