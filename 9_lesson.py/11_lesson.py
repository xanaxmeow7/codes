# number = 10
# while number < 21:
#     print(number)
#     number += 1



from mcpi.minecraft import Minecraft
import time
import random


mc = Minecraft.create()

# while True:
#     x = random.randint(100, 1000)
#     y = random.randint(100, 100)
#     z = random.randint(1000, 1500)
#     mc.player.setTilePos(x, y, z)
#     time.sleep(5)


# # mc.player.setTilePos(1000, 80, 1000)







# count = 0
# water = 8
# while count < 30:
#     x, y, z = mc.player.getPos()
#     mc.setBlock(x, y, z, water)
#     count += 1
#     time.sleep(1)








# flowers = 51

# #     x, y, z = mc.player.getPos()
# #     mc.setBlock(x, y, z, flowers)
# #     time.sleep(0,2)








# while True:
#     x, y, z = mc.player.getPos()
#     stop_block = mc.getBlock(x, y-1, z)
#     verstak_block = mc.getBlock(x, y-1, z)
#     if stop_block == 57:
#         break
#     elif verstak_block == 58:
#         time.sleep(10)
#     mc.setBlock(x, y, z, flowers)
#     mc.setBlock(x+1, y, z+1, flowers)
#     mc.setBlock(x-1, y, z-1, flowers)
#     mc.setBlock(x+1, y, z-1, flowers)
#     mc.setBlock(x-1, y, z+1, flowers)
#     time.sleep(0.2)














gold = 41
sand = 12
while True:
    x, y, z = mc.player.getPos()
    if mc.getBlock(x, y, z) == sand:
        break
    else:
        mc.setBlock(x, y-1, z, gold)
        mc.setBlock(x, y+2, z, gold)


        mc.setBlock(x+1, y, z, gold)
        mc.setBlock(x-1, y, z, gold)


        mc.setBlock(x+1, y+1, z, gold)
        mc.setBlock(x-1, y+1, z, gold)