#!/usr/bin/env python

"""
Generates a image of the top view of a chunk
Needs a textures folder with a block folder inside
"""
import os
import sys

# sys.path.insert(0, 'D:\Dockyard\LCServer\anvil-parser\anvil')
sys.path.insert(0, '..\\..\\anvil-parser\\anvil')
print( "CWD: ", os.getcwd() )
print( "Parent: ", os.path.dirname( os.getcwd() ) )
print( "Args: ", sys.argv )
## os.abort()

# directory = 'D:\\Dockyard\\LCWorld\\world\\region'
# directory = '..\\..\\..\\LCWorld\\world\\region'
# directory = '..\\..\\..\\FRWorld\\world\\region'
directory = sys.argv[1]
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
chunkCnt = 0

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
                        chunkCnt = chunkCnt + 1
                        tstamp = region.chunk_timestamp(chx, chz)
                        if (tstamp > 0) and (tstamp < firstDate): firstDate = tstamp
                        if tstamp > lastDate: lastDate = tstamp
                        
stopTime = datetime.now()

print( "Regions  : ", f'{regionCnt:,}' )
print( "Chunks   : ", f'{chunkCnt:,}' )
print( "Start    : ", startTime.strftime("%H:%M:%S"))
print( "Stop     : ", stopTime.strftime("%H:%M:%S"))
print( "firstDate: ", datetime.fromtimestamp( firstDate ) )
print( "lastDate : ", datetime.fromtimestamp( lastDate ) )
# print( "L: ", chunk.lastUpdate )
