from mcpi import minecraft
from mcpi.vec3 import Vec3
import random
from .window import Window

class Wall:
    def __init__(self, pos : Vec3, size : Vec3, **kwargs):
        #wall_base=None, conf=(1, 2)
        self.pos = pos
        self.size = size - Vec3(1, 1, 1)
        l = size.x + size.z - 1
        
        if size.x == 1:
            step = Vec3(0,0,1)
        else:
            step = Vec3(1,0,0)
        self.base = kwargs["base"]
        conf = kwargs["conf"]
        
        # wood (5)
        # log (17)
        # cobble (4)
        # stone (1)
        # glass (20)
        # slab (43)
##        base_blocks = [5, 17, 4, 1, 43]
##        window_blocks = [5, 17, 4, 1, None, 43]
##        if base == None:
##            self.base = random.choices(base_blocks)[0]
##        if window_base == None:
##            self.window_base = random.choices(window_blocks)[0]
        
        self.pane = kwargs["pane"]
        self.objects = []
        
        # Make windows
##        c_conf = [(1, 1)]
##        c_weights = [1]
##        if (l + 1) % 2 == 0:
##            c_conf.append((1, 2))
##            c_weights.append(8)
##        if (l + 1) % 3 == 0:
##            c_conf.append((2, 3))
##            c_weights.append(4)
##        if (l + 2) % 4 == 0:
##            c_conf.append((2, 4))
##            c_weights.append(3)
##        
##        conf = random.choices(c_conf, weights=c_weights)[0]
        amount = (l + conf[1] - 1) // conf[1]
        for i in range(amount):
            tsize = step * conf[0] + Vec3(0, size.y, 0)
            tsize.x = max(1, tsize.x)
            tsize.y = max(1, tsize.y)
            tsize.z = max(1, tsize.z)
            self.objects.append(Window(pos + step * conf[1] * i,
                                       tsize, {
                                           bottom: kwargs["window_base"],
                                           top: kwargs["window_top"],
                                           pane: kwargs["pane"]}
                                       ))
        
    def build(self, mc):
        mc.setBlocks(self.pos, self.pos + self.size, self.base)
        # TODO: implement wall_base
        for obj in self.objects:
            obj.build(mc)
            
    def __repr__(self):
        return f"Window<{self.pos};{self.size}>"
