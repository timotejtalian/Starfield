import py5
import random

def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

class Star:
    def __init__(self):
        self.randomize()
    
    def randomize(self):
        self.x = random.uniform(-py5.width, py5.width)
        self.y = random.uniform(-py5.height, py5.height)
        self.z = random.uniform(1, py5.width)
        self.pz = self.z
    
    def update(self, speed):
        self.z -= speed
        if self.z < 1: 
            self.randomize()
    def show(self):
        sx = map_value(self.x / self.z, 0, 1, 0, py5.width)
        sy = map_value(self.y / self.z, 0, 1, 0, py5.height)
        r = map_value(self.z, 0, py5.width, 20, 0)
        px = map_value(self.x / self.pz, 0, 1, 0, py5.width)
        py = map_value(self.y / self.pz, 0, 1, 0, py5.height)
        py5.fill(255)
        py5.no_stroke()
        py5.ellipse(sx,sy, r, r)
        alpha = map_value(self.z, 0, py5.width, 255, 0)
        py5.stroke(255, alpha)
        py5.line(px, py, sx, sy)

Stars = [Star() for i in range(1000)]

def setup():
    py5.size(1000, 1000)

def draw():
    speed = map_value(py5.mouse_x, 0, py5.width, 0, 25)   
    py5.background(0)
    py5.translate(py5.width/2, py5.height/2)
    for star in Stars:
        star.update(speed)
        star.show()
        star.pz = star.z 

py5.run_sketch()
