##########################################
# Description 
# pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
#
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
# Example Data
#
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   2
#
#
#########################################
from pprint import pprint

listA, listB = [], []
totalDiff = 0

with open("inputs.txt","r") as f:
    inputs = f.read()


#pprint(inputs)
inputArr = inputs.split("\n")
# The last item in the list is empty so chuck it
del inputArr[-1]

# 
for line in inputArr:
    tmp = line.split()
    listA.append(tmp[0])
    listB.append(tmp[1])

listA = [int(x) for x in listA]
listB = [int(x) for x in listB]

listA.sort()
listB.sort()


pprint(listA)
pprint(listB)
for x in range(0, len(listA)):
    absolute = abs(listA[x] - listB[x])
    totalDiff = totalDiff + absolute
    print("Absolute: {}", absolute)
    #print("Running Total: {}", totalDiff)

print("Total: {}", totalDiff)
