from manimlib.imports import *

class three(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=14.25* DEGREES,theta=0*DEGREES,distance=8)
        self.play(FadeIn(axes))

        plane = ParametricSurface(
            lambda u,v: np.array([
                6,
                8*v,
                3*u
                ]), u_min = -0.8, u_max = 0.8, fill_opacity = 0.4).rotate(45*DEGREES).move_to(ORIGIN).shift(RIGHT+UP)
        d2text = TextMobject(r'$\mathbb{R}^{2}: y = mx + c$').shift(3*LEFT + 2*UP).rotate(np.pi/2)
        d3text = TextMobject(r'$\mathbb{R}^{3}: y = mx + c$').shift(4*RIGHT+3*UP)
        self.play(FadeIn(plane), FadeIn(d2text))
        self.wait(3)
        self.play(FadeOut(d2text))
        self.move_camera(phi = 60*DEGREES, theta=45*DEGREES,run_time=3)
        self.begin_ambient_camera_rotation(rate=0.02)
        self.add_fixed_in_frame_mobjects(d3text)
        self.play(FadeIn(d3text))
        self.wait(3)
        self.play(FadeOut(d3text), FadeOut(plane), FadeOut(axes))
        self.wait()
