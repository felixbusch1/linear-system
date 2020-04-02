import numpy as np

#Setup matrix
matrix = np.matrix('1 -2 4; 4 3 -4; 1 5 6')

#Set dimension of the matrix
n = 3

#Setup solution vector for the matrix
svector = [7, -1, -5]

#In this case we have the following equations:
#-----------------------
# -- 1x -2y + 4z = 7  --
# -- 4x +3y -4z = -1  --
# -- 1x +5y + 6z = -5 --
#-----------------------


# Function name: det()
#
# Description: Algorithm of the Laplace expansion to calculate the determinant of a NxN matrix.
#	       Recursive implementation.
#	       
# Parameters: matrix, n
#
#	      matrix := The input matrix in numpy format (e.g 2x2 numpy.matrix('1 2; 3 4'))
#	      n	     := The dimension of the input matrix. In this example abolve n=2
#
# Return value: The determinant of the input matrix

def det(matrix, n):
    if n == 1:
        return matrix.item(0)
       
    #In case the dimension of the input matrix is n=2 
    if n == 2:
        return matrix.item(0) * matrix.item(3) - matrix.item(1) * matrix.item(2)
    else:

        #Set return value of the function to zero
        res = 0

        #Every second iteration the sign switches, we use a simple lambda function for this.
        #That means, sign(1) = 1, sign(3) = 1... sign(2*k+1) = 1 and sign(2*k) = -1
        sign = lambda x: 1 if x & 1 else -1

        #We use always the first column of the matrix.
        vec = matrix[:,[0]]

        #We have to calculate n- subdeterminants
        for i in range(n):
            
            #Delete the column with the most number of zeros in it
            temp = np.delete(matrix, 0, axis=1)
            
            #Get the value of the sub determinant recursively
            submatrix = np.delete(temp, i, axis=0)
            
            #Calculate sub determinant
            x = det(submatrix, n-1)

            #Calculate the value of the determinant
            res += vec.item(i) * x * sign(i+1)            

        return res

#Apply Cramer's rule to solve the LGS
#First calculate the "main determinant" for which the solution vector is not yet contained in the matrix
hdet = det(matrix, n)

#In case hdet = 0, no solution
if hdet == 0:
    print("No solutions!")
    exit(0)


#By having n variables, we can have n solutions
for i in range(n):

    #Temporarily save the i-th column vector
    temp = matrix[:,[i]]

    for j in range(n):
        #The solution vector comes once in each column
        matrix.itemset((j, i), svector[j])
    
    #print result
    print("x" + str(i+1) + " = " + str(det(matrix, n) / hdet))

    #Reinsert the original column vector
    for j in range(n):
        matrix.itemset((j,i), temp.item(j))
