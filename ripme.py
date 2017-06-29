# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:22:28 2017

@author: quinn
"""
import math
import matplotlib





def copyList(A,B,length, width):
#copies a 2d array to another 2d array
    for x in range(width):
        temp = []
        for y in range(length):
            temp.append(B[x][y])
        A.append(temp)
    
def searchFinished(aMap,length,width):
#boolean. returns true if there are no more unsearched areas on the map
    for x in range(width):
        for y in range(length):
            if(aMap[x][y] != -1):
                return False
    return True
    
def printGrid(area,length,width): 
#prints the map out nicely
    for x in range(width):
        for y in range(length):
            print(area[x][y], end=" ")
            
        print()
    print()       
    
    
def getUnvisitedSquares(arrmap,width,length, curX, curY):
#generates a list of unvisited coordinates for the agent
    moveX = []
    moveY = []
    for x in range(width):
        for y in range(length):
            if all([arrmap[x][y] >  -1, not(all([curX == x , curY == y]))]):
                moveX.append(x)
                moveY.append(y)
    
    return [moveX,moveY] 

   

def getAllPossiblePaths(oldMap, length, width, droneX, droneY,moveListChain, masterList, batteryLife,dist):
    
    possibleMoves = getUnvisitedSquares(oldMap, length,width, droneX, droneY)
    batteryLife = batteryLife + (dist + 20)
    
    if any([searchFinished(oldMap, length,width), all([droneX == 0, droneY == 0, dist != 0])]):
        masterList.append(moveListChain)
        return 100
    #now make 2 cases 1 for sucess, 1 for failure, also make battery life less simplistic
    elif batteryLife > 100:
        return -math.inf
    else:
        maxReward = -1000
        
        for index in range(len(possibleMoves[0])):
            newMap = []
            newChain = []
            copyList(newMap, oldMap, length,width)
            
            newDroneX = possibleMoves[0][index]
            newDroneY = possibleMoves[1][index]
            val = newMap[newDroneX][newDroneY]
            
            newChain = []
            copyList(newChain, moveListChain, 2, len(moveListChain))
            newChain.append([newDroneX,newDroneY])
            
            
            
            
            newMap[newDroneX][newDroneY] = -1
            
            dist = math.sqrt(math.pow(droneX - newDroneX,2) + math.pow(droneY - newDroneY,2))
            
            maxReward = max(maxReward , val + getAllPossiblePaths(newMap, length, width, newDroneX,  newDroneY, newChain, masterList, batteryLife,dist))
            
            
            
            
    
    return maxReward    
    
        
 ###########################################################################################
   
"""
 0   19   23   88   57   70   43   20   33   13
 68   80   99   77   71   62   52   69    2   42
 39   28    7   34   67   51   49   41   96   59
 25   81   92   44   37   85   61   12   75   83
 15   46   94    4   72   17    3   45    9   58
  6   79   78   53   29   65   84    1   18   27
 24   60   36   21   11   74   50   54   14    8
 26   87   31   86   93   97   30   95   91   89
 56   35   76   55   98   63    5   73   64   40
 10   38   66   90   82   48  100   16   47   22
"""


arrmap =  [[0,19,23,88,57,70,43,20,33,13],[68,80,99,77,71,62,52,69,2,42],[39,28,7,34,67,51,49,41,96,59],[25,81,92,44,37,85,61,12,75,83],[15,46,94,4,72,17,3,45,9,58],[6,79,78,53,29,65,84,1,18,27],[24,60,36,21,11,74,50,54,14,8],[26,87,31,86,93,97,30,95,91,89],[56,35,76,55,98,63,5,73,64,40],[10,38,66,90,82,48,100,16,47,22]]


#arrmap = [row1,row2,row3,row4]
pathChosen = []
moveListChain = []
masterList = []

moveListChain.append([0,0])

length = 4
width = 4

droneX = 0
droneY = 0


maxVal = getAllPossiblePaths(arrmap,length,width,droneX, droneY, moveListChain, masterList,0,0)
for index in range(len(masterList)):
        val = 0
        for m in range(len(masterList[index])):
            val = val + arrmap[masterList[index][m][0]][masterList[index][m][1]]
        masterList[index].append([0, val])
        
for index in range(len(masterList)): 
        if maxVal - 100 == masterList[index][len(masterList[index])-1][1]:
            pathChosen = list(masterList[index])
            

pathChosen.remove([0,maxVal-100])

print(pathChosen)
print("Maximum Value: ", end = "")
print(maxVal-100)


