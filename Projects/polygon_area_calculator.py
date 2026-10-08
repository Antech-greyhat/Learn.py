class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagnoal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.width > 50:
            return 'Too Big for Picture'
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self,shape):
        return (self.width // shape.width) ** (self.height // shape.height)

    def __str__(self) -> str:
        return f"Rectangle (Width = {self.width}, height = {self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self,side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self,side):
        self.set_side(side)

    def __str__(self) -> str:
        return f"Square(side = {self.width})"