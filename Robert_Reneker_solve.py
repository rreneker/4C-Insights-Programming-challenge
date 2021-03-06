def initialize_visited_grid(height,width):
    #initializes a grid that tells us if a spot in the actual grid has been visited yet
    result = list()
    for i in range(0,height):
        result.append([False]*width) 
    return result

def move(direction,currX,currY,path,grid,visited_grid):
    #takes care of the steps needed to move from one spot to the next
    if direction == "Up":
        currX = currX-1
        #print("Up")
    elif direction == "Right":
        currY = currY+1
        #print("Right")
    elif direction == "Left":
        currY = currY-1
        #print("Left")
    elif direction == "Down":
        currX = currX+1
        #print("Down")
    else:
        #print("OOPS")
        return
    path.append((currX,currY))
    visited_grid[currX][currY] = True
    return currX,currY
def go_back(path):
    #Moves back one space 
    path.pop()
    if(len(path) == 0):
        return -1,-1
    else:
        currX = path[-1][0]
        currY = path[-1][1]
        #print("No New nodes")
        return currX, currY

def path_exists(grid, queries):
    result = list()
    for i in range(0,len(queries),2):
        startX = queries[i][0]
        startY = queries[i][1]
        endX = queries[i+1][0]
        endY = queries[i+1][1]
        startVal = grid[startX][startY]
        endVal = grid[endX][endY]
        if startVal != endVal:
            result.append(False)
        else:
            visited_grid = initialize_visited_grid(len(grid),len(grid[0]))
            #print(visited_grid)
            currX = startX
            currY = startY
            path = list()
            path.append((currX,currY))
            visited_grid[startX][startY] = True
            while (currX != endX or currY != endY) and len(path) > 0:
                diffX = currX - endX
                diffY = currY - endY
                if diffX >= 0 and diffY >= 0:
                    if diffX >= diffY:
                        if (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)
                    else:
                        if (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)

                elif diffX < 0 and diffY >= 0:
                    if abs(diffX) >= abs(diffY):
                        if (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)
                    else:
                        
                        if (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)
                elif diffX < 0 and diffY < 0:
                    if abs(diffX) >= abs(diffY):
                        if (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)
                    else:
                        if (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        else:
                           currX,currY = go_back(path)

                elif diffX >= 0 and diffY < 0:
                    if diffX >= abs(diffY):
                        if (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        else:
                            currX,currY = go_back(path)
                    else:
                        if (currY+1) < len(grid[0]) and grid[currX][currY+1] == startVal and visited_grid[currX][currY+1] == False:
                            currX,currY = move("Right",currX,currY,path,grid,visited_grid)
                        elif (currX-1) > -1 and grid[currX-1][currY] == startVal and visited_grid[currX-1][currY] == False:
                            currX,currY = move("Up",currX,currY,path,grid,visited_grid)
                        elif (currX+1) < len(grid) and grid[currX+1][currY] == startVal and visited_grid[currX+1][currY] == False:
                            currX,currY = move("Down",currX,currY,path,grid,visited_grid)
                        elif (currY-1) > -1 and grid[currX][currY-1] == startVal and visited_grid[currX][currY-1] == False:
                            currX,currY = move("Left",currX,currY,path,grid,visited_grid)
                        else:
                           currX,currY = go_back(path)
            #print(path)
            if(len(path) == 0):
                result.append(False)
            else:    
                result.append(True)
    return result