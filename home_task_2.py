# Задача с предыдущего семинара:
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class AgeException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Возраст {self.age} не может быть отрицательной величиной.'


class Human:
    def __init__(self, age, surname, name, patronymic):
        if age >= 0:
            self.__age = age
        else:
            raise AgeException(age)
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"


human1 = Human(18, "Кириллов", "Кирилл", "Сергеевич")
