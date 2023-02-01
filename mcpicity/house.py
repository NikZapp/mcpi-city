from mcpi import minecraft
from mcpi.vec3 import Vec3
from mcpi import block
from .outline import Outline
from .wall import Wall
import random

class HouseFloor:
    def __init__(self, p0 : Vec3, p1 : Vec3):
        self.pos = Vec3(min(p0.x, p1.x), min(p0.y, p1.y), min(p0.z, p1.z))
        self.size = Vec3(max(p0.x, p1.x), max(p0.y, p1.y), max(p0.z, p1.z)) - self.pos
        self.objects = []

        pane = random.randint(1, 9) == 1
        window_base_t = random.randint(1, 16) == 1
        base_t = (random.randint(1, 5) == 1) and window_base_t
        window_base = [5, 17][window_base_t]
        base = [5, 17][base_t]
        conf = (1, 2)
        
        self.objects.append(Outline(p0, p1, 1, 0))
        self.objects.append(Wall(p0 + Vec3(1, 1, 0), self.size - Vec3(1, 1, -1) - Vec3(0, 0, self.size.z),           base=base, window_base=window_base, pane=pane, conf=conf))
        self.objects.append(Wall(p0 + Vec3(1, 1, self.size.z), self.size - Vec3(1, 1, -1) - Vec3(0, 0, self.size.z), base=base, window_base=window_base, pane=pane, conf=conf))
        self.objects.append(Wall(p0 + Vec3(0, 1, 1), self.size - Vec3(-1, 1, 1) - Vec3(self.size.x, 0, 0),           base=base, window_base=window_base, pane=pane, conf=conf))
        self.objects.append(Wall(p0 + Vec3(self.size.x, 1, 1), self.size - Vec3(-1, 1, 1) - Vec3(self.size.x, 0, 0), base=base, window_base=window_base, pane=pane, conf=conf))

    def build(self, mc):
        mc.setBlocks(self.pos + Vec3(1, 0, 1), self.size + Vec3(1, 0, 1), 4)
        for obj in self.objects:
            obj.build(mc)

    def __repr__(self):
        return f"HouseFloor<{self.pos};{self.size}>"

if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    House(Vec3(0,0,0), Vec3(10,10,10)).build(mc)

