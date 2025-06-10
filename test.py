import math
dimension=eval(input("Enter Shape dimesnion number : "))

class shape:
    def first(self, dimension):
        self.dimension=dimension
        if dimension == 2:
            print("Available 2D shapes: \nrectangle\nsquare\ntriangle")
        elif dimension == 3:
            print("Available 3D shapes:\ncube\ncuboid\ncylinder")
        else:
            print("Invalid shape dimension.")
            exit()
        self.shape = input("Enter shape name: ").lower()    
            

class shape_input(shape):
    def input_values(self):
        values = {}
        if self.dimension == 2:
            if self.shape == "rectangle":
                values['l'] = eval(input("Enter length: "))
                values['w'] = eval(input("Enter width: "))
            elif self.shape == "square":
                values['side'] = eval(input("Enter side: "))
            elif self.shape == "triangle":
                values['b'] = eval(input("Enter base: "))
                values['h'] = eval(input("Enter height: "))

        elif self.dimension == 3:
            if self.shape == "cube":
                values['side'] = eval(input("Enter side: "))
            elif self.shape == "cuboid":
                values['l'] = eval(input("Enter length: "))
                values['w'] = eval(input("Enter width: "))
                values['h'] = eval(input("Enter height: "))
            elif self.shape == "cylinder":
                values['r'] = eval(input("Enter radius: "))
                values['h'] = eval(input("Enter height: "))
        return values


class Formula:
    def rectangle_area(self, l, w):
        return l * w

    def square_area(self, side):
        return side ** 2

    def triangle_area(self, b, h):
        return 0.5 * b * h

    def cube_volume(self, side):
        return side ** 3

    def cuboid_volume(self, l, w, h):
        return l * w * h

    def cylinder_volume(self, r, h):
        return math.pi * r * r * h
    
class cal(Formula,shape_input):
    def calculation(self):
        values = self.input_values()
        if self.dimension == 2:
            if self.shape == "rectangle":
                result = self.rectangle_area(values['l'], values['w'])
                print("Area of Rectangle:", result)
            elif self.shape == "square":
                result = self.square_area(values['side'])
                print("Area of Square:", result)
            elif self.shape == "triangle":
                result = self.triangle_area(values['b'], values['h'])
                print("Area of Triangle:", result)

        elif self.dimension == 3:
            if self.shape == "cube":
                result = self.cube_volume(values['side'])
                print("Volume of Cube:", result)
            elif self.shape == "cuboid":
                result = self.cuboid_volume(values['l'], values['w'], values['h'])
                print("Volume of Cuboid:", result)
            elif self.shape == "cylinder":
                result = self.cylinder_volume(values['r'], values['h'])
                print("Volume of Cylinder:", round(result, 2))
        
c=cal()
c.first(dimension)
c.calculation()
