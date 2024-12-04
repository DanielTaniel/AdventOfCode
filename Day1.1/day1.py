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
import argparse

parser = argparse.ArgumentParser("AoC_Day_1")

parser.add_argument("-m", "--mode", help="what mode are you using? count or freq", type=str)
parser.add_argument("-t","--test", nargs="?", help="use Test data", const=False, type=bool)
parser.add_argument("-d","--debug", nargs="?", help="show Debug data", const=False, type=bool)
args = vars(parser.parse_args())

pprint(args)

def dpprint(value):
    if args["debug"]:
        pprint(value)

def read_n_sort(test=args["test"]):

    listA, listB = [], []

    file = "inputs.txt"
    if test:
        file = "test.txt"

    with open("inputs.txt","r") as f:
        inputs = f.read()
    
    inputArr = inputs.split("\n")
    # The last item in the list is empty so chuck it
    del inputArr[-1]

    for line in inputArr:
        tmp = line.split()
        listA.append(tmp[0])
        listB.append(tmp[1])

    listA = [int(x) for x in listA]
    listB = [int(x) for x in listB]

    listA.sort()
    listB.sort()

    return listA, listB

def count_diff(listA, listB):
    totalDiff = 0
    for x in range(0, len(listA)):
        absolute = abs(listA[x] - listB[x])
        totalDiff = totalDiff + absolute
        dpprint(F"Absolute:{absolute}")
        dpprint(F"Running Total: {totalDiff}")
    dpprint(F"Total:{totalDiff}")

    return totalDiff

def count_frequency(listA, listB):
    running_total = 0
    for x in range(0, len(listA)):
        running_total =  running_total + (listB.count(listA[x]) * listA[x])
    return running_total

def main():
    print("starting Main")
    listA, listB = read_n_sort()
    if args["mode"] == "count":
        print("This Total = {}".format(count_diff(listA, listB)))
    elif args["mode"] == "freq":
        print(count_frequency(listA, listB))
    else:
        print("doing Neither")
main()
