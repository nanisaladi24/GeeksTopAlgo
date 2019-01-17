# Dynamic Programming implementation of LCS problem 
#subSeqStr="" #global 
def lcs(X , Y): 
    # find the length of the strings 
    #global subSeqStr
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[[0,""]for i in xrange(n+1)] for i in xrange(m+1)] 
    #print L
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j][0] = 0
                L[i][j][1] = ""
            elif X[i-1] == Y[j-1]:
                L[i][j][1] = L[i-1][j-1][1]+X[i-1]
                L[i][j][0] = L[i-1][j-1][0]+1
            else: 
                if L[i-1][j][0] > L[i][j-1][0]:
                    L[i][j][0] = L[i-1][j][0]
                    L[i][j][1] = L[i-1][j][1]
                else:
                    L[i][j][0] = L[i][j-1][0]
                    L[i][j][1] = L[i][j-1][1]
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs 
  
  
# Driver program to test the above function 
X = "ABCDGH"
Y = "AEDFHR"
# X = "AGGTAB"
# Y = "GXTXAYB"

print "Given sequences: "
print X
print Y
print "\nSolution:"
res = lcs(X, Y)
print "Length of LCS: ", res[0]
print "Sequence: ", res[1]