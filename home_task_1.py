# Задача с предыдущего семинара:
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class SideException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Сторона {self.side} не может быть отрицательной или равной нулю.'


class Rectangle:
    def __init__(self, side1, side2=None):
        if side1 <= 0:
            raise SideException(side1)
        if side2 <= 0:
            raise SideException(side2)
        if side2 == None:
            self.side2 = self.side1 = side1
        else:
            self.side1 = side1
            self.side2 = side2

    def perimeter(self):
        return (self.side1 + self.side2) * 2

    def area(self):
        return self.side1 * self.side2


rec_1 = Rectangle(-2, 4)
print(rec_1.perimeter())
