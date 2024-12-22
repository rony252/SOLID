#follow LSP
class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def _init_(self, side):
        super()._init_(side, side)


def print_area(shape: Shape):
    print(shape.get_area())

rectangle = Rectangle(5, 10)
square = Square(5)

print_area(rectangle)  
print_area(square)  


   
#not following LSP
class Rectangle:
    def _init_(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height  
        
def print_area(shape: Rectangle):
    shape.set_width(5)
    shape.set_height(10)
    print(shape.get_area())

square = Square(5, 5)
print_area(square)