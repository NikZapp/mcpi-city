from mcpi import minecraft
from mcpi.vec3 import Vec3

class Outline:
    def __init__(self, p0 : Vec3, p1 : Vec3, **kwargs):
        self.p0 = Vec3(min(p0.x, p1.x), min(p0.y, p1.y), min(p0.z, p1.z))
        self.p1 = Vec3(max(p0.x, p1.x), max(p0.y, p1.y), max(p0.z, p1.z))
        self.block = kwargs["block"]
        
    def build(self, mc):
        a = self.p0
        b = self.p1

        # x
        mc.setBlocks(a.x, a.y, a.z, b.x, a.y, a.z, self.block)
        mc.setBlocks(a.x, a.y, b.z, b.x, a.y, b.z, self.block)
        mc.setBlocks(a.x, b.y, a.z, b.x, b.y, a.z, self.block)
        mc.setBlocks(a.x, b.y, b.z, b.x, b.y, b.z, self.block)

        # y
        mc.setBlocks(a.x, a.y, a.z, a.x, b.y, a.z, self.block)
        mc.setBlocks(a.x, a.y, b.z, a.x, b.y, b.z, self.block)
        mc.setBlocks(b.x, a.y, a.z, b.x, b.y, a.z, self.block)
        mc.setBlocks(b.x, a.y, b.z, b.x, b.y, b.z, self.block)

        # z
        mc.setBlocks(a.x, a.y, a.z, a.x, a.y, b.z, self.block)
        mc.setBlocks(a.x, b.y, a.z, a.x, b.y, b.z, self.block)
        mc.setBlocks(b.x, a.y, a.z, b.x, a.y, b.z, self.block)
        mc.setBlocks(b.x, b.y, a.z, b.x, b.y, b.z, self.block)

    def __repr__(self):
        return f"Outline<{self.p0};{self.p1}>"

if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    Outline(Vec3(10,10,10), Vec3(20,30,40)).build(mc)
