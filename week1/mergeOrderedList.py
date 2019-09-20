#Python3 code to demonstrate to combine two sorted list using heapq.merge()
from heapq import merge

#initialing lists
testList1 = [1,4,6,8,9,11]
testList2 = [2,5,7,8,9,10,23]

#printing original lists
print("The 1st original list is: " + str(testList1))
print("The 2nd original list is: " + str(testList2))

#--------------------------------------------------------------------------
#FIRST METHOD:
# using naive method  
# to combine two sorted lists 
size_1 = len(testList1) 
size_2 = len(testList2) 
  
res = [] 
i, j = 0, 0
  
while i < size_1 and j < size_2: 
    if testList1[i] < testList2[j]: 
      res.append(testList1[i]) 
      i += 1
  
    else: 
      res.append(testList2[j]) 
      j += 1
  
res = res + testList1[i:] + testList2[j:] 
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#SECOND METHOD:
#using heapq.merge() to combine two sorted lists
res = list(merge(testList1,testList2))
#--------------------------------------------------------------------------

#printing result
print("The combined sorted list is: "+str(res))

