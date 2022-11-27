"""
Generates a image of the top view of a chunk
Needs a textures folder with a block folder inside
"""
import sys

region = "D:\Dockyard\LCWorld\world\region\r.0.0.mca"
chx = 0
chz = 0

import os
import _path
#import anvil

chunk = anvil.Chunk.from_region(region, chx, chz)

print("read chunk")

