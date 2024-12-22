# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:10:58 2024

@author: CompuStore
"""
#follow O/C
class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
#added class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius
    
    
#not following O/C
class Shape:
    def get_area(self):
        if isinstance(self, Rectangle):
            return self.width * self.height
        elif isinstance(self, Circle):
            return 3.14 * self.radius * self.radius
        elif isinstance(self, Triangle):
            return 0.5 * self.base * self.height
