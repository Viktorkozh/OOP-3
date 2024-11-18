#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Number:
    def __init__(self, value: float):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        raise ValueError()

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        raise ValueError()

    def __repr__(self):
        return f"Number({self.value})"


class Real(Number):
    def root(self, n: float):
        if n == 0:
            raise ValueError("Степень не может быть нулевой.")
        return Number(self.value ** (1 / n))

    def power(self, n: float):
        return Number(self.value ** n)


if __name__ == "__main__":
    num1 = Number(10.0)
    num2 = Number(5.0)

    print(f"Умножение: {num1 * num2}")
    print(f"Вычитание: {num1 - num2}")

    real_num = Real(27.0)

    print(f"Кубический корень: {real_num.root(3)}")
    print(f"27 в кубе: {real_num.power(3)}")
