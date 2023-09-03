# from mcpi.minecraft import Minecraft

# mc = Minecraft.create()

# p = mc.player.getTilePos()


# x = p.x
# y = p.y
# z = p.z

# def create_sqare(widht, id):
#     mc.setBlocks(x, y, z, x + widht, y, z + widht, id)
# create_sqare(10, 41)





# from mcpi.minecraft import Minecraft
# from minecraftstuff import MinecraftDrawing, MinecraftShape, MinecraftTurtle
# from mcpi import block
# import time

# mc = Minecraft.create()

# pos = mc.player.getTilePos()

# steve = MinecraftTurtle(mc, pos)

# # def right():
# # steve.right(90)
# # steve.forward(15)
# # def left():
# # steve.left(90)
# # steve.forward(15)
# steve.penblock(169)

# steve.forward(15)

# steve.left(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.left(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.left(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)

# steve.left(90)
# steve.forward(15)

# steve.right(90)
# steve.forward(15)


from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

p = mc.player.getTilePos()

x = random.randint(400, 500)
y = random.randint(100, 150)
z = random.randint(250, 300)



def create_square(width, id):


    mc.setBlocks(x, y, z, x + width, y, z + width, id)


id = random.randint(1, 50)
create_square(10, id)
