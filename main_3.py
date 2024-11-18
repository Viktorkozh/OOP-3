#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import sqrt


class Norm(ABC):

    @abstractmethod
    def CalculateNorm(self):
        pass

    @abstractmethod
    def CalculateAbsolute(self):
        pass


class Complex(Norm):
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img

    def CalculateAbsolute(self):
        return sqrt(self.real ** 2 + self.img ** 2)

    def CalculateNorm(self):
        return self.CalculateAbsolute() ** 2


class Vector3D(Norm):
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def CalculateAbsolute(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def CalculateNorm(self):
        return max(abs(self.x), abs(self.y), abs(self.z))


if __name__ == "__main__":
    c = Complex(5, 2)
    print("Комплексное число", c.real, "+", c.img, "i")
    print("Модуль комплексного числа", c.CalculateAbsolute())
    print("Норма комплексного числа", c.CalculateNorm())
    v = Vector3D(1, 5, 7)
    print("Вектор", v.x, v.y, v.z)
    print("Модуль вектора", v.CalculateAbsolute())
    print("Норма вектора", v.CalculateNorm())
