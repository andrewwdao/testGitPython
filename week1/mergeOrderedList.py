#Python3 code to demonstrate to combine two sorted list using heapq.merge()
from heapq import merge

#initialing lists
testList1 = [1,4,6,8,9,11]
testList2 = [2,5,7,8,9,10,23]

#printing original lists
print("The 1st original list is: " + str(testList1))
print("The 2nd original list is: " + str(testList2))

#using heapq.merge() to combine two sorted lists
res = list(merge(testList1,testList2))

#printing result
print("The combined sorted list is: "+str(res))

