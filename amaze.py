#!/usr/bin/env python.

# global variables
positions = [0]*12 # for specifying the column for the queen in the ith row
count=0 #for the number of solutions that can be obtained for this case

# function for verifying if queen can be placed in row k and column i 
def place(k,i):
    # j denotes the queens which have already been placed to compare their positions
    # with the current queen considered
    for j in range (0,k):
    	# condition for being in the same column 
        if ((positions[j]==i) or
       	# condition for the being in the same diagonal
             (abs(positions[j]-i)==abs(j-k)) or
        # condition for being at a step's reach of a knight (L shape step) 
                ((abs(positions[j]-i)==1 and abs(j-k)==2) or (abs(positions[j]-i)==2 and abs(j-k)==1))):
             return False 
    return True

# nAmazes function
# k is the row to place the amaze
# n is the number of amazes
def nAmazes(k,n):
    global count
    for i in range(0,n):
        print('k=',k+1,' i=',i+1 )
        if place(k,i):
        # placing (i+1)th queen in (k+1)th row
        # since index values start at 0, we include the +1
            print('Placing piece ',k+1,'at ',i+1)
            positions[k] = i
            # solution is found when all the amazes are placed on the board
            if k==n-1 :
                count+=1
                print('\nSOLUTION',count,'FOUND!')
                for j in range(0, n):
                    print(positions[j]+1,end=' ')
                print('\n\n')
            # else call the function again recursively to place the next amaze 
            #  on the board
            else :
                print('Calling Amaze Again')
                nAmazes(k+1,n)
        # once a solution is obtained
        # or a dead node is reached tree (recursive tree for the execution) 
        # backtrack to previous recursive function call
        print('Ended for k=',k+1,' i=',i+1)
    print('BackTracking...')        
    return None

##################
nAmazes(0,12)
print('\nTotal Number of Solutions')
print(count,'\n')
    

     





