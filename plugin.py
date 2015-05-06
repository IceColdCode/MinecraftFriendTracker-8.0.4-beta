# requires raspberry juice installed in same directory
import mcpi.Minecraft as minecraft
import time
# establish connection
world = minecraft.Minecraft.create()
theIds = world.getPlayerIds()
# main loop
while True:
  for id in theIds:
    name = id + "is online right now!"
    mc.postToChat(id)
  time.delay(15)
