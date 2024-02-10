from manim import *

class DivideCircle(Scene):
    def construct(self):
        # Draw a circle
        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

        # Divide the circle into 2 parts
        div_2 = VGroup(*[Line(circle.point_at_angle(i*TAU/2), circle.point_at_angle((i+1)*TAU/2)) for i in range(2)])
        self.play(Create(div_2))

        # Divide the circle into 3 parts
        div_3 = VGroup(*[Line(circle.point_at_angle(i*TAU/3), circle.point_at_angle((i+1)*TAU/3)) for i in range(3)])
        self.play(Create(div_3))

        # Divide the circle into 4 parts
        div_4 = VGroup(*[Line(circle.point_at_angle(i*TAU/4), circle.point_at_angle((i+1)*TAU/4)) for i in range(4)])
        self.play(Create(div_4))

        # Divide the circle into 5 parts
        div_5 = VGroup(*[Line(circle.point_at_angle(i*TAU/5), circle.point_at_angle((i+1)*TAU/5)) for i in range(5)])
        self.play(Create(div_5))

        # Divide the circle into 6 parts
        div_6 = VGroup(*[Line(circle.point_at_angle(i*TAU/6), circle.point_at_angle((i+1)*TAU/6)) for i in range(6)])
        self.play(Create(div_6))

        # Divide the circle into 8 parts
        div_8 = VGroup(*[Line(circle.point_at_angle(i*TAU/8), circle.point_at_angle((i+1)*TAU/8)) for i in range(8)])
        self.play(Create(div_8))

        # Divide the circle into 9 parts
        div_9 = VGroup(*[Line(circle.point_at_angle(i*TAU/9), circle.point_at_angle((i+1)*TAU/9)) for i in range(9)])
        self.play(Create(div_9))

        # Divide the circle into 10 parts
        div_10 = VGroup(*[Line(circle.point_at_angle(i*TAU/10), circle.point_at_angle((i+1)*TAU/10)) for i in range(10)])
        self.play(Create(div_10))

        self.wait()

# Render the scene
if __name__ == "__main__":
    renderer = "opengl" # Use "cairo" if you encounter issues with opengl
    resolution = (800, 600)
    file_name = "divide_circle"
    scene = DivideCircle()
    scene.render()
