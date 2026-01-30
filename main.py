from kivy.config import Config
Config.set('kivy', 'audio', 'ffpyplayer')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Line, Ellipse
import random
import math

# ===================== WINDOW =====================
Window.size = (400, 700)
Window.fullscreen = False

SUN_REPEAT_DELAY = 20.0
SUN_EVENT_DURATION = 4.0


# ===================== UTILS =====================
def hsv_to_rgb(h, s, v):
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    return [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q)
    ][i]


# ===================== STAR =====================
class Star:
    def __init__(self, canvas, spin):
        self.canvas = canvas
        self.spin = spin
        self.depth = random.uniform(0.15, 1.0)
        with self.canvas:
            self.color = Color(1, 1, 1, 1)
            self.line = Line(width=1)
        self.reset()

    def reset(self):
        self.angle = random.uniform(0, math.pi * 2)
        self.radius = random.uniform(0.01, 0.12)
        self.speed = random.uniform(300, 1500) * self.depth

    def update(self, dt, warp, rot, bass, mid, high, hue, cx, cy):
        spiral = rot * self.spin * (0.4 + self.depth * 1.8)
        self.angle += spiral * dt * (1 + mid * 0.8)

        self.radius += self.speed * warp * dt * (0.0015 + bass * 0.002)

        if self.radius > 1.8:
            self.reset()

        x = cx + math.cos(self.angle) * self.radius * Window.width
        y = cy + math.sin(self.angle) * self.radius * Window.height

        stretch = 0.03 + bass * 0.12 * self.depth
        px = cx + math.cos(self.angle) * (self.radius - stretch) * Window.width
        py = cy + math.sin(self.angle) * (self.radius - stretch) * Window.height

        self.line.points = [px, py, x, y]
        self.line.width = 0.6 + self.depth * 2.4

        r, g, b = hsv_to_rgb((hue + high * 0.25) % 1.0, 0.65, 1)
        self.color.rgb = (r, g, b)
        self.color.a = 0.25 + self.depth * 0.75


# ===================== SUN =====================
class Sun:
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = 5
        self.phase = random.uniform(0, 10)
        self.birth_time = 0.0
        self.life_time = 0.0

        with self.canvas:
            self.core_color = Color(1, 0.95, 0.75, 0.85)
            self.core = Ellipse()

            self.fire = []
            for _ in range(6):
                c = Color(1, 0.4, 0.15, 0)
                e = Ellipse()
                self.fire.append((c, e))

    def update(self, dt, bass):
        self.birth_time += dt
        self.life_time += dt
        self.phase += dt * (2 + bass * 4)

        grow = min(self.birth_time / 2.5, 1.0)
        self.radius += dt * (18 + bass * 80) * grow

        cx, cy = Window.width / 2, Window.height / 2
        pulse = math.sin(self.phase) * (3 + bass * 8)
        r = self.radius + pulse

        self.core.size = (r * 2, r * 2)
        self.core.pos = (cx - r, cy - r)

        for i, (c, e) in enumerate(self.fire):
            rr = r + 10 + math.sin(self.phase + i) * 15
            c.a = min(0.25, self.birth_time * 0.1)
            e.size = (rr * 2, rr * 2)
            e.pos = (cx - rr, cy - rr)

        return self.life_time >= SUN_EVENT_DURATION

    def destroy(self):
        self.canvas.remove(self.core)
        for _, e in self.fire:
            self.canvas.remove(e)


# ===================== FLASH =====================
class Flash:
    def __init__(self, canvas):
        self.alpha = 0.7
        self.canvas = canvas
        with self.canvas:
            self.color = Color(1, 1, 1, self.alpha)
            self.circle = Ellipse(
                size=(Window.width * 2, Window.height * 2),
                pos=(-Window.width / 2, -Window.height / 2)
            )

    def update(self, dt):
        self.alpha -= dt * 1.4
        self.color.a = max(self.alpha, 0)
        return self.alpha <= 0

    def destroy(self):
        self.canvas.remove(self.circle)


# ===================== UNIVERSE =====================
class Universe(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.stars_a = [Star(self.canvas, 1) for _ in range(600)]
        self.stars_b = [Star(self.canvas, -1) for _ in range(600)]

        self.sun = None
        self.flash = None

        self.time = 0.0
        self.warp = 0.8
        self.rotation = 0.08
        self.hue = 0.0

        self.bass = 0
        self.mid = 0
        self.high = 0

        self.last_sun_time = 0.0

        self.sound = SoundLoader.load("assets/music/f321-ncs-lumora-462701.mp3")
        if self.sound:
            self.sound.play()

        Clock.schedule_interval(self.update, 1 / 60)

    def update_fft(self, dt):
        t = self.time
        self.bass += (max(0, math.sin(t * 1.2)) - self.bass) * dt * 3
        self.mid += (max(0, math.sin(t * 0.8 + 1)) - self.mid) * dt * 2
        self.high += (max(0, math.sin(t * 2.4 + 2)) - self.high) * dt * 4

    def update(self, dt):
        self.time += dt
        self.update_fft(dt)

        # === CIERRE AUTOMÁTICO CUANDO TERMINA LA MÚSICA ===
        if self.sound and self.sound.state == 'stop':
            App.get_running_app().stop()
            return

        self.hue = (self.hue + dt * 0.025 + self.high * 0.015) % 1.0

        drift_x = math.sin(self.time * 0.35) * Window.width * 0.03
        drift_y = math.cos(self.time * 0.27) * Window.height * 0.03
        cx = Window.width / 2 + drift_x
        cy = Window.height / 2 + drift_y

        calm = self.bass < 0.15 and self.mid < 0.2
        if calm:
            self.warp += (0.6 - self.warp) * dt
            self.rotation += (0.04 - self.rotation) * dt
        else:
            self.warp = min(self.warp + self.bass * dt * 1.5, 3.0)
            self.rotation = min(self.rotation + self.mid * dt * 0.22, 0.5)

        for s in self.stars_a:
            s.update(dt, self.warp, self.rotation,
                     self.bass, self.mid, self.high,
                     self.hue, cx, cy)

        for s in self.stars_b:
            s.update(dt, self.warp * 0.9, self.rotation * 0.8,
                     self.bass, self.mid, self.high,
                     self.hue + 0.15, cx, cy)

        if not self.sun and self.time - self.last_sun_time >= SUN_REPEAT_DELAY:
            self.sun = Sun(self.canvas)
            self.last_sun_time = self.time

        if self.sun:
            if self.sun.update(dt, self.bass):
                self.sun.destroy()
                self.sun = None
                self.flash = Flash(self.canvas)

        if self.flash:
            if self.flash.update(dt):
                self.flash.destroy()
                self.flash = None


# ===================== APP =====================
class UniverseApp(App):
    def build(self):
        return Universe()


if __name__ == "__main__":
    UniverseApp().run()