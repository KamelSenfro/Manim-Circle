from manim import *

class DivideCircle(Scene):
    def construct(self):
        # Draw a circle
        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

        # Find center and endpoints of the diameter
        center = circle.get_center()
        diameter = Line(circle.get_start(), circle.get_end())

        # Divide the circle into 2 parts using the diameter
        div_2 = VGroup(diameter)
        self.play(Create(div_2))

        # Section the circle into equal parts
        num_parts = 2
        div_angle = TAU / num_parts
        div_lines = VGroup(*[Line(center, circle.point_at_angle(i * div_angle)) for i in range(1, num_parts)])
        self.play(*[Create(line) for line in div_lines])

        # Update num_parts for subsequent divisions
        num_parts *= 2

        for _ in range(2, num_parts):
            # Create new division lines
            div_lines = VGroup(*[Line(center, circle.point_at_angle(i * div_angle)) for i in range(1, num_parts)])

            # Display the division lines
            self.play(*[Create(line) for line in div_lines])

            # Update the division angle for the next iteration
            div_angle = TAU / num_parts

        self.wait()

# Render the scene
if __name__ == "__main__":
    renderer = "opengl" # Use "cairo" if you encounter issues with opengl
    resolution = (800, 600)
    file_name = "divide_circle"
    scene = DivideCircle()
    scene.render()
