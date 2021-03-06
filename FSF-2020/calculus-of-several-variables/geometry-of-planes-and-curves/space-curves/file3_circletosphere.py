from manimlib.imports import *

class sphere(GraphScene, ThreeDScene):
    CONFIG = {
    'x_min': -10,
    'x_max': 10,
    'y_min': -10,
    'y_max': 10,
    'graph_origin': ORIGIN,
    "x_axis_width": 10,
    "y_axis_height": 10,
    }
    def construct(self):
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)
        circleeqn = TextMobject(r'Hence, $x^{2} + y^{2} = 2(r^{2} - u^{2})$')
        plottext = TextMobject(r'$x = \sqrt{r^{2} - u^{2}}cos\theta$ \\ $y = \sqrt{r^{2} - u^{2}}sin\theta$').shift(2*UP + 3*RIGHT)


        self.setup_axes()
        self.play(FadeIn(self.axes), FadeIn(plottext))

        dots = []
        for t in range(19):
            dot = Dot().shift((3*XTD*np.cos(t), 3*YTD*np.sin(t),0))
            dots.append(dot)
            self.play(FadeIn(dot), run_time = 0.2)
        dots = VGroup(*dots)
        circle = Circle(radius = 3*XTD).set_color(WHITE).set_stroke(width = 10)
        self.play(FadeIn(circle), FadeOut(dots), FadeOut(plottext))
        self.wait(2)


        axes = ThreeDAxes(**self.CONFIG)
        sph = Sphere(radius = 3).scale(0.5)
        text2 = TextMobject(r'Setting $u = 3$,\\$z = u$').shift(4*YTD*UP + 5*XTD*RIGHT)

        self.play(Transform(self.axes,axes), ReplacementTransform(circle, sph))
        self.add(text2)
        self.wait(2)
        self.remove(text2)
        self.move_camera(phi = 60*DEGREES, theta=45*DEGREES,run_time=5)
        self.begin_ambient_camera_rotation(rate=0.03)
        self.play(FadeOut(axes), FadeOut(sph), FadeOut(self.axes))
        self.wait(1)
