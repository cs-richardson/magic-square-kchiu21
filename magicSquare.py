"""
Kolton Chiu
In this program, the user inputs a magic square, and the program will
determine if its a true magic square.
https://stackoverflow.com/questions/45116587/create-2d-array-with-the-same-size-as-another-array-and-initialize-with-zero-in/45116669
"""
def fillSquare(n, sqArr):
    '''
    This procedure prompts the user for n^2 inputs to populate a
    2D square array which has alreay been declared
    precondition:  sqArr has been declared with a size of nxn
    '''

    #note: I could have used len(sqArr) instead of passing n in as a parameter
    # but I thought it would be easier for you to understand if it was passed...
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    

def printSquare(n, sqArr):
    '''
    This procedure "pretty" prints a 2D square array of size n
    '''
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")
    
def checkRow(n, sqArr, mNum):
    for row in range (n):
        row_sum = 0
        for col in range(n):
            row_sum = row_sum + sqArr[row][col]
        if not row_sum == mNum:
            return False
    return True

def checkCol(n, sqArr, mNum):
    for row in range (n):
        row_sum = 0
        for col in range(n):
            row_sum = row_sum + sqArr[col][row]
        if not row_sum == mNum:
            return False
    return True

def checkDiag1(n, sqArr, mNum):
    row_sum = 0
    for row in range (n):
        row_sum = sqArr[row][row] + row_sum
    if not row_sum == mNum:
        return False
    return True

def checkDiag2(n, sqArr, mNum):
    row_sum = 0
    for row in range (n):
        row_sum = sqArr[row][n - 1 - row] + row_sum
    if not row_sum == mNum:
        return False
    return True

def checkUnique(n, sqArr):
    check_arr = []
    for row in range(n):
        for col in range(n):
            check_arr.append(sqArr[row][col])
            count_appear = 0
            for pos in range(len(check_arr)):
                if sqArr[row][col] == check_arr[pos]:
                    count_appear = count_appear + 1
                    if count_appear == 2:
                        return False
    return True

def checkSquare(size, square):
    '''
    Returns True if inputed square is magic, and False if not.
    '''
    magicNum = size * ((size**2 + 1) / 2)
    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
       return True
    else:
       return False



# ---MAIN---
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

'''
if you get tired of typing in the square multiple times,
for testing purposes, you may want to comment out the 3 lines above and
uncomment the 2 lines below.  It will make your testing life *much* easier :)
'''
#s = 3
#sq = [[2,7,6], [9,5,1], [4,3,8]]

printSquare(s, sq)
print(checkSquare(s, sq))
   

