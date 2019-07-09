#
# commits evolution data for tiles that
# meet requirements based on neighboring
# tiles data
#

def evoOne(map, tile):
    tile.getData()
    x=tile.getX()
    y=tile.getY()
    evolveCounter=0
    
    #cycle through the neighbors of the evolving tile
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            #if a tile is on the edge of the map it will have a proportionally
            #lower evolution chance
            if (0 < row <= 29 and 0 < col <= 29 and
                (row != x or col != y)): #do not count the tile being evaluated
                    if (map.getData(row, col) == 1):
                        evolveCounter += 1
            
    
    #if a tile is neighbored by 50% water it floods and becomes water         
    if (evolveCounter > 5):
        tile.dataCommit(1)   

#imported after to avoid import loop that took me 10 long minutes to realize    
from tree_gen import Tile, Map