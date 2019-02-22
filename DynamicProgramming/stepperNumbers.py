'''
Solution by: Dorayya Naidu Saladi
Problem Statement:  Find Stepper numbers in range N to M. 
                    Stepper Numbers can be defined as numbers with adjacent digits' difference to be 1.Ex: 123,121,345,321.

Solution Approach 1 (Recursive):
-Find the degrees of N and M. Also find the Most significant digits (MSD) of each number.
-Create an Array to store all the stepper numbers.
-Iterate between the Degrees from N to M.
-Iterate between 1 to 9 digits and assign them as 1st digit for the numbers to be added.
    -Corner case:   Assign the first digit with MSD of N when degree is of N. Iterate till 9.
                    Iterate till the first digit of number is MSD of M when degree is of M.
-Recursively calculate the remaining digits of the Number with following rules:
    -If the number has the digits with current degree and if the number is b/w N and M, add the number to Array.
    -If the prev digit is 0, just do addition (append 1 to the num). And do recursion.
    -If the prev digit is 9, just do subtraction (append 8 to the num). And do recursion.
    -Else 
        -Add 1 to the prev digit and do recursion. 
        -Add 1 to the prev digit and do recursion.
-Return Array of stepper numbers.

Solution Approach 2 (Dynamic Programming):
-Find the degrees of N and M. Also find the Most significant digits (MSD) of each number.
-Create an Array to store all the stepper numbers.
-Calculate stepper numbers upto degree(N)+1 with recursive approach suggested above.
-Create variables start-index and end-index which maintains the stepper number Array's index range in previous degree. 
    -They are initialized with indices of degree(N)+1
-Iterate between the Degrees from degree(N)+2 to degree(M).
    -Iterate between start-index and end-index. 
        -Calculate next digit (addition/subtraction (0/9 are special cases)). 
        -If the number<=M
            Add the numbers in Array. 
        -Else
            Break the loop
        -Update start-index and end-index
-Return Array of stepper numbers.
'''

#Dynamic Programming Approach

def recArrayUpdate(myStr,Arr,deg,N,M):
    #print(myStr)
    #return
    if len(myStr)==deg:
        if N<=int(myStr)<=M:
            Arr.append(myStr)
            return
        else:
            return
    
    elif myStr[-1]=='0':
        myStr=myStr+'1'
        return recArrayUpdate(myStr,Arr,deg,N,M)
    elif myStr[-1]=='9':
        myStr=myStr+'8'
        return recArrayUpdate(myStr,Arr,deg,N,M)
    else:
        temp=myStr+str(int(myStr[-1])-1)
        recArrayUpdate(temp,Arr,deg,N,M)
        myStr=myStr+str(int(myStr[-1])+1)
        recArrayUpdate(myStr,Arr,deg,N,M)
        return
    return

def getDegreeMSD(m):
    i=0
    while m>=1:
        i=i+1
        if m/10<1:
            return i,int(m)
        m=m/10
    return 0,0

def getStepperArr(N,M):
    Arr=list()
    myStr=""
    nDegree,nMSD=getDegreeMSD(N)
    mDegree,mMSD=getDegreeMSD(M)
    # print (nDegree)
    # print (mDegree)
    # print (nMSD)
    # print (mMSD)
    newNDegree=nDegree
    start_index=0
    end_index=0
    if M<N:
        return []
    if mDegree==1:
        return []
    if nDegree==1:
        newNDegree=2

    for deg in range(newNDegree,nDegree+2):
        if deg==(nDegree+1):
            start_index=len(Arr)
        if deg==nDegree and nDegree==newNDegree:
            for i in range(nMSD,10):
                myStr=str(i)
                recArrayUpdate(myStr,Arr,deg,N,M)
        else:
            for i in range(1,10):
                myStr=str(i)
                recArrayUpdate(myStr,Arr,deg,N,M)
        if deg==(nDegree+1):
            end_index=len(Arr)-1 

    for deg in range(nDegree+2,mDegree+1):
        for i in range(start_index,end_index+1):
            if i==start_index:
                start_index=len(Arr)

            if Arr[i][-1]=='0':
                myStr=Arr[i]+'1'
                if int(myStr)<=M:
                    Arr.append(myStr)
                else:
                    break
            elif Arr[i][-1]=='9':
                myStr=Arr[i]+'8'
                if int(myStr)<=M:
                    Arr.append(myStr)
                else:
                    break
            else:
                myStr=Arr[i]+str(int(Arr[i][-1])-1)
                if int(myStr)<=M:
                    Arr.append(myStr)
                else:
                    break
                myStr=Arr[i]+str(int(Arr[i][-1])+1)
                if int(myStr)<=M:
                    Arr.append(myStr)
                else:
                    break

            if i==end_index:
                end_index=len(Arr)-1
    return Arr

#Testing
    
print ("\ntest 1:")
print (getStepperArr(1,100))
print ("\ntest 2:")
print (getStepperArr(47,800))
print ("\ntest 3:")
print (getStepperArr(50,10000))
        

'''

Test Results:

test 1:
['10', '12', '21', '23', '32', '34', '43', '45', '54', '56', '65', '67', '76', '78', '87', '89', '98']

test 2:
['54', '56', '65', '67', '76', '78', '87', '89', '98', '101', '121', '123', '210', '212', '232', '234', '321', '323', '343', '345', '432', '434', '454', '456', '543', '545', '565', '567', '654', '656', '676', '678', '765', '767', '787', '789']

test 3:
['54', '56', '65', '67', '76', '78', '87', '89', '98', '101', '121', '123', '210', '212', '232', '234', '321', '323', '343', '345', '432', '434', '454', '456', '543', '545', '565', '567', '654', '656', '676', '678', '765', '767', '787', '789', '876', '878', '898', '987', '989', '1010', '1012', '1210', '1212', '1232', '1234', '2101', '2121', '2123', '2321', '2323', '2343', '2345', '3210', '3212', '3232', '3234', '3432', '3434', '3454', '3456', '4321', '4323', '4343', '4345', '4543', '4545', '4565', '4567', '5432', '5434', '5454', '5456', '5654', '5656', '5676', '5678', '6543', '6545', '6565', '6567', '6765', '6767', '6787', '6789', '7654', '7656', '7676', '7678', '7876', '7878', '7898', '8765', '8767', '8787', '8789', '8987', '8989', '9876', '9878', '9898']

'''

