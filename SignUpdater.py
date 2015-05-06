###################################################################################################
# this program is a beta version of a plugin designed for use with bukkit API and raspberry juice #
# USAGE:  update sign text                                                                        #
###################################################################################################
# imports
from mcpi import mcpi.Minecraft as minecraft
from mcpi import mcpi.Block as block
#initalize minecraft
world = minecraft.Minecraft.create()
# SignUpdater class definition
class SignUpdater(Object):
  """ this class can deleteSign(x,y,z), createSign(x,y,z), and updateText(x,y,z,str)"""
  # create sign and set it's text:
  def createSign(x, y, z, text):
    string = [text]
    world.setBlock(x, y, z, block.SIGN.id, string)
  
  
