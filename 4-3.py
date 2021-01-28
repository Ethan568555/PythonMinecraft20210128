from mcpi .minecraft import Minecraft
pe= Minecraft.create()
from random import randrange


for i in range(10):
    x,y,z = pe.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        pe.setBlock(x,y,z,35,color)
ans = randrange(0,16)
while True:
    hits = pe.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = pe. getBlockWithData(h.pos)
        data = block.data
        if data == ans:
            pe.postToChat("you find it!!")
            pe.setBlock(h.pos,46)
            break
        elif data < ans:
            pe.postToChat("no bigger")
        elif data > ans:
            pe.postToChat("no smaller")
                