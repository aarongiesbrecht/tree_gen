#
# scans neighboring tiles and
# converts water to land depending
# on how many surrounding tiles are 
# already land
# 


def darkenOne(dataMap, row, col):
    x=row
    y=col
    landCounter=0
    
    #cycle through the neighbors of the evolving tile
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            #if a tile is on the edge of the map it will have a proportionally
            #lower evolution chance
            if (0 < row <= 73 and 0 < col <= 73 and
                (row != x or col != y)): #do not count the tile being evaluated
                    if (dataMap[row][col].getData() == 0):
                        landCounter += 1
    
    #if a tile is neighbored by 50% water it floods and becomes water         
    if (landCounter > 4):
        return 0

def darkenTwo(dataMap, row, col):
    x=row
    y=col
    landCounter=0
    
    #cycle through the neighbors of the evolving tile
    for row in range(x-2, x+3):
        for col in range(y-2, y+3):
            #if a tile is on the edge of the map it will have a proportionally
            #lower evolution chance
            if (0 < row <= 73 and 0 < col <= 73 and
                (row != x or col != y)): #do not count the tile being evaluated
                    if (dataMap[row][col].getData() == 0):
                        landCounter += 1
    
    #if a tile is neighbored by 50% water it floods and becomes water         
    if (landCounter > 12):
        return 0

def darkenThree(dataMap, row, col):
    x=row
    y=col
    landCounter=0
    
    #cycle through the neighbors of the evolving tile
    for row in range(x-3, x+4):
        for col in range(y-3, y+4):
            #if a tile is on the edge of the map it will have a proportionally
            #lower evolution chance
            if (0 < row <= 73 and 0 < col <= 73 and
                (row != x or col != y)): #do not count the tile being evaluated
                    if (dataMap[row][col].getData() == 0):
                        landCounter += 1
    
    #if a tile is neighbored by 50% water it floods and becomes water         
    if (landCounter > 25):
        return 0

