from mcpi .minecraft import Minecraft
pe= Minecraft.create()
import random

x,y,z = pe.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    if r == 1:
        pe.setBlocks(x,y,z,x,y,z+4,46)
        z = z+4
    if r == 2:
        pe.setBlocks(x,y,z,x,y,z-4,46)
        z = z-4
    if r == 3:
        pe.setBlocks(x,y,z,x+4,y,z,46)
        x = x+4
    if r == 4:
        pe.setBlocks(x,y,z,x,y,z-4,46)
        x = x-4
    if r == 5:
        pe.setBlocks(x,y,z,x,y+4,z,46)
        y = y+4
    if r == 6:
        pe.setBlocks(x,y,z,x,y-4,z,46)
        y = y-4