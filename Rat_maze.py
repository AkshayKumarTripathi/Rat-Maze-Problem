def play():
    # Takes the dimensions of the grid you want to make
    run=int(input("enter the dimentions of the grid   (For a 7X7 grid type 7)   "))

    #creates and empty grid for the solution
    solution=[[0 for x in range(run)] for x in  range(run)]
    
    givenmatrix=[]

    # for running without giving input un-comment the below line and comment the for part
    # givenmatrix=[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,1,1],[1,0,1,0,0,0,0],[1,0,1,1,1,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1]]
    
    for x in range(run):
        givenmatrix.append(list(map(int,input("Enter the numbers with space in between   ").split())))

    solution[0][0]=1
    
    if proceed(solution,givenmatrix,0,0,run):
        printoi(solution,run)
    
    else:   print("NO SOLUTION AVAILABLE!!! PLEASE CHECK THE ")


#starting point is (0,0) and ending point is (run-1,run-1)

def proceed(solution,givenmatrix,x,y,run):
    #Base case 
    if x==run-1 and y==run-1:
        return True

    #recursive case
    else:
        dirx=[1,-1,0,0]
        diry=[0,0,1,-1]         #do not use x here because of the parameter x you are passing!
        for num in range(4):
            xmove=x+dirx[num]
            ymove=y+diry[num]
            if isvalid(solution,givenmatrix,xmove,ymove,run):
                solution[xmove][ymove]=1
                if proceed(solution,givenmatrix,xmove,ymove,run):   #CONDITION TO GO FURTHER IN THE MATRIX (without if condition if the function returns False all the functions will return false and the backtraking wont happen)
                    return True
                
                solution[xmove][ymove]=0                            #HERE BACKTRAKING HAPPENS

        return False                                                #THIS RETURN's FALSE TO THE FUNCTION AND THE POINT WHERE WE WERE BECOMES 0 (as we reached the deadend)
        


def isvalid(solution,givenmatrix,x,y,run):                          #FUNCTION TO CHECK IF THE POINT IS IN THE MATRIX AND SATISFIES THE PROVIDED PATH
    if x>=0 and y>=0 and x<run and y<run and givenmatrix[x][y]==1 and solution[x][y]==0:
        return True
    return False

def printoi(sol,run):                                               #A normal function to print the solution matrix
    for x in range(run):
        print(sol[x])

play()    
        
        