from mcpi .minecraft import Minecraft
pe= Minecraft.create()

list2 = [[12,41,14],[35,73,86]]
myID = pe.getPlayerEntityId("willwill1491")
x,y,z = pe.entity.getTilePos(myID)
startX = x
for i in list2:
    for j in i:
        pe.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1