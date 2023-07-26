# Задача с предыдущего семинара:
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from home_task_2 import Human
import random


class IdException(Exception):
    def __init__(self, id_num):
        self.id_num = id_num

    def __str__(self):
        return f'ID сотрудника должен состоять из 6 цифр.'


class Employee(Human):
    MAG = 7

    def __init__(self, id_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_num = self.get_id(id_num)
        self.level = self.level_gen()

    def level_gen(self):
        return sum(map(int, list(str(self.id_num)))) % self.MAG

    def get_id(self, id_num):
        if len(str(id_num)) != 6:
            # return random.randint(100000, 999999)
            raise IdException(id_num)
        else:
            return id_num


emp1 = Employee(1456, 18, "Кириллов", "Кирилл", "Сергеевич")
