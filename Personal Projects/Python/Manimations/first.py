from manim import *

class CreateCircle(Scene):
    def construct(self):
        # 1. Create Mobjects (Mathematical Objects)
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        # 2. Add Animations
        self.play(Create(circle))
        self.wait(2) # Pause for 2 seconds