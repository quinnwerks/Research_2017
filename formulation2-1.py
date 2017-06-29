# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:22:28 2017

@author: quinn
"""
import math
import matplotlib

def droneIsDone(arrmap, length, width, dX, dY, dist):
    if(any([searchFinished(arrmap, length,width), all([dX == 0, dY == 0, dist != 0])])):
        return True
    return False

def droneIsDead(batD):
    if batD > 100:
        return True
    return False



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

def getUnvistedSquaresForTwo(arrmap, width, length, x1, x2, y1, y2):
    moveX = []
    moveY = []

    for i in range(width):
        for j in range(length):
             if all([arrmap[i][j] > -1, not(all([x1 == i, x2 == i, y1 == j, y2 == j]))]):
                 moveX.append(i)
                 moveY.append(j)
    return [moveX, moveY]


def getAllPossiblePaths(oldMap, length, width, aX, aY, bX, bY, chainA, chainB,masterList, batA, batB,distA, distB):

    distConst = 1
    battConst = 25

    if not droneIsDone(oldMap, length, width, aX, aY, distA):
        batA = batA + (distConst * distA + battConst)
    if not droneIsDone(oldMap, length, width, bX, bY, distB):
        batB = batB + (distConst * distB + battConst)

    ###################################################################################################################
    if droneIsDead(batA) or droneIsDead(batB):
        return -math.inf

    elif droneIsDone(oldMap, length, width, aX, aY, distA) and droneIsDone(oldMap, length, width,bX,bY, distB):

        masterList.append([chainA,chainB])
        return 100



    elif not droneIsDone(oldMap, length, width, aX, aY, distA) and droneIsDone(oldMap, length, width,bX,bY, distB):
        possibleMoves = getUnvisitedSquares(oldMap, length, width, aX, aY)
        maxReward = -1000
        
        for index in range(len(possibleMoves[0])):
            newMap = []
            #newChainA = []
            copyList(newMap, oldMap, length,width)
            
            naX = possibleMoves[0][index]
            naY = possibleMoves[1][index]
            val = newMap[naX][naY]
            
            newChainA = []
            copyList(newChainA, chainA, 2, len(chainA))
            newChainA.append([naX,naY])
            
            
            

            newMap[naX][naY] = -1
            
            distA = math.sqrt(math.pow(aX - naX,2) + math.pow(aY - naY,2))
            
            maxReward = max(maxReward , val + getAllPossiblePaths(newMap, length, width, naX,  naY, bX, bY,newChainA, chainB,masterList, batA, batB,distA,distB))

    elif droneIsDone(oldMap, length, width, aX, aY, distA) and not droneIsDone(oldMap, length, width, bX, bY, distB):
        possibleMoves = getUnvisitedSquares(oldMap, length, width, bX, bY)
        maxReward = -1000

        for index in range(len(possibleMoves[0])):
            newMap = []
            #newChainB = []
            copyList(newMap, oldMap, length, width)

            nbX = possibleMoves[0][index]
            nbY = possibleMoves[1][index]
            val = newMap[nbX][nbY]

            newChainB = []
            copyList(newChainB, chainB, 2, len(chainB))
            newChainB.append([nbX, nbY])

            newMap[nbX][nbY] = -1

            distB = math.sqrt(math.pow(bX - nbX, 2) + math.pow(bY - nbY, 2))

            maxReward = max(maxReward,val + getAllPossiblePaths(newMap, length, width, aX, aY, nbX, nbY, chainA, newChainB, masterList, batA, batB, distA, distB))
    else:


        possibleMoves = getUnvistedSquaresForTwo(oldMap, length, width, aX, bX, aY, bY)
        maxReward = -1000

        for aIndex in range(len(possibleMoves[0])):
            for bIndex in range(len(possibleMoves[0])):

                # new map, new me
                newMap = []
                copyList(newMap, oldMap, length, width)

                # potential positions
                naX = possibleMoves[0][aIndex]
                naY = possibleMoves[1][aIndex]

                nbX = possibleMoves[0][bIndex]
                nbY = possibleMoves[1][bIndex]

                #check validity
                if not(naX == nbX and naY == nbY) or (naX == 0 and naY == 0):

                    newChainA = []
                    newChainB = []

                    copyList(newChainA, chainA, 2, len(chainA))
                    newChainA.append([naX, naY])

                    copyList(newChainB, chainB, 2, len(chainB))
                    newChainB.append([nbX, nbY])

                    valB = newMap[nbX][nbY]
                    valA = newMap[naX][naY]

                    if not(nbX == 0 and nbY == 0):
                        newMap[nbX][nbY] = -1
                    if not(naX == 0 and naY == 0):
                        newMap[naX][naY] = -1

                    distA = math.sqrt(math.pow(aX - naX, 2) + math.pow(aY - naY, 2))
                    distB = math.sqrt(math.pow(bX - nbX, 2) + math.pow(bY - nbY, 2))

                    maxReward = max(maxReward, valA + valB + getAllPossiblePaths(newMap, length, width, naX, naY, nbX, nbY, newChainA, newChainB, masterList, batA, batB, distA, distB))

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
#print(getUnvistedSquaresForTwo(arrmap,4,4,0,0,0,0))

#arrmap = [row1,row2,row3,row4]
pathChosen = []
chainA = []
chainB = []
masterList = []

chainA.append([0, 0])
chainB.append([0, 0])

length = 4
width = 4

#droneX = 0
#droneY = 0
aX = 0
aY = 0
bX = 0
bY = 0

#l = getUnvistedSquaresForTwo(arrmap, length,width, aX, aY, bX, bY)
#print(l)\
#getAllPossiblePaths(oldMap, length, width, aX, aY, bX, bY, chainA, chainB,masterList, batA, batB,distA, distB
#print(getAllPossiblePaths(arrmap,length,width,aX, aY, bX, bY, chainA, chainB, masterList,0,0,0,0))


maxVal = getAllPossiblePaths(arrmap,length,width,aX, aY, bX, bY, chainA, chainB, masterList,0,0,0,0)

for index in range(len(masterList)):
        val1 = 0
        val2 = 0
        for m in range(len(masterList[index][0])):
            val1 = val1 + arrmap[masterList[index][0][m][0]][masterList[index][0][m][1]]
        for l in range(len(masterList[index][1])):
            val2 = val2 + arrmap[masterList[index][1][l][0]][masterList[index][1][l][1]]
        masterList[index].append([0,val1+val2])

for index in range(len(masterList)):
   if maxVal -100 == masterList[index][2][1]:
       pathChosen = list(masterList[index])

#pathChosen.remove([0,maxVal -100])

print(maxVal - 100)
#print(masterList[3])
#print(masterList[4])
#print(masterList)
print(pathChosen[0])
print(pathChosen[1])
#print(pathChosen[1])








