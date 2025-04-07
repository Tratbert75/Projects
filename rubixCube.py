import copy
# This is a 3D array representing a Rubik's cube
#Everything is from the perspective of the white center facing forward with red on the top
#cube 1 is white
#cube 2 is green
#cube 3 is yellow
#cube 4 is blue
#cube 5 is red
#cube 6 is orange
def turnRightUp(cube):
    oldCube = copy.deepcopy(cube)
    #white face
    for i in range(3):
        cube[0][i][2] = oldCube[5][i][2]
    #green face
    for i in range(3):
        cube[1][0][i] = oldCube[1][2-i][0]
        cube[1][1][i] = oldCube[1][2-i][1]
        cube[1][2][i] = oldCube[1][2-i][2]
    #yellow face
    
    print("old cube", oldCube)
    print("new cube",  cube)
rubixCube = [[[[2], [3], [2]],
              [[5],[1],[3],],
              [[4],[4],[5],]], 
             [[[1], [2], [5]],
              [[4],[2],[2],],
              [[4],[5],[3],]],
             [[[1], [6], [3]],
              [[6],[3],[4],],
              [[2],[1],[5],]],
             [[[6], [1], [3]],
              [[6],[4],[1],],
              [[1],[5],[6],]],
             [[[4], [3], [2]],
              [[6],[5],[1],],
              [[6],[2],[6],]],
             [[[1], [5], [3]],
              [[3],[6],[2],],
              [[4],[4],[5],]]]
amountRed = 0
amountGreen = 0
amountYellow = 0
amountBlue = 0
amountWhite = 0
amountOrange = 0
for i in range(len(rubixCube)):
    for j in range(len(rubixCube[i])):
        for k in range(len(rubixCube[i][j])):
            for l in range(len(rubixCube[i][j][k])):
                if rubixCube[i][j][k][l] == 1:
                    amountWhite += 1
                elif rubixCube[i][j][k][l] == 2:
                    amountGreen += 1
                elif rubixCube[i][j][k][l] == 3:
                    amountYellow += 1
                elif rubixCube[i][j][k][l] == 4:
                    amountBlue += 1
                elif rubixCube[i][j][k][l] == 5:
                    amountRed += 1
                elif rubixCube[i][j][k][l] == 6:
                    amountOrange += 1
print("Amount of white cubes: ", amountWhite)
print("Amount of green cubes: ", amountGreen)
print("Amount of yellow cubes: ", amountYellow)
print("Amount of blue cubes: ", amountBlue)
print("Amount of red cubes: ", amountRed)
print("Amount of orange cubes: ", amountOrange)
print("Total amount of cubes: ", amountWhite + amountGreen + amountYellow + amountBlue + amountRed + amountOrange)
turnRightUp(rubixCube)