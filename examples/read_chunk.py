"""
Generates a image of the top view of a chunk
Needs a textures folder with a block folder inside
"""
import sys

# sys.path.insert(0, 'D:\Dockyard\LCServer\anvil-parser\anvil')
sys.path.insert(0, '..\\..\\anvil-parser\\anvil')

# directory = 'D:\\Dockyard\\LCWorld\\world\\region'
directory = '..\\..\\..\\LCWorld\\world\\region'
## region = 'D:\\Dockyard\\LCWorld\\world\\region\\r.0.0.mca'
chx = 0
chz = 0

import os
import _path
import anvil
from datetime import datetime

firstDate = sys.maxsize
lastDate = 0
regionCnt = 0

startTime = datetime.now()

for filename in os.scandir( directory ):
    if filename.is_file():
        filenamePath = "D:\\Dockyard\\LCWorld\\world\\region\\r.60.67.mca"
        #print("fn:", filename.path)
        region = anvil.Region.from_file(filename.path)
        if len( region.data ) > 0:
            regionCnt = regionCnt + 1
            for chx in range( 0, 31 ):
                for chz in range( 0, 31 ):
                        # nbt_data = region.chunk_data(chx, chz)
                        # if nbt_data is not None:
                        #     chunk = anvil.Chunk(nbt_data)
                        #     if chunk.lastUpdate < firstDate: firstDate = chunk.lastUpdate
                        #     if chunk.lastUpdate > lastDate: lastDate = chunk.lastUpdate
                        tstamp = region.chunk_timestamp(chx, chz)
                        if (tstamp > 0) and (tstamp < firstDate): firstDate = tstamp
                        if tstamp > lastDate: lastDate = tstamp
                        
stopTime = datetime.now()

print( "Regions: ", regionCnt )
print( "Start: ", startTime.strftime("%H:%M:%S"))
print( "Stop : ", stopTime.strftime("%H:%M:%S"))
print( "firstDate: ", firstDate )
print( "lastDate : ", lastDate )
# print( "L: ", chunk.lastUpdate )
