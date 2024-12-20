##########################################
# Description 
#
#
#########################################
from pprint import pprint
import argparse
import re

parser = argparse.ArgumentParser("AoC_Day_4")

parser.add_argument("-t", "--test", help="use test data", nargs="?", const=False)
parser.add_argument("-p", "--part", help="part 1 or 2?", type=int, default=1)
args = vars(parser.parse_args())

def main():
    pprint(args)
    search = read()
    if args['part'] == 1:
        part1(search)
    elif args['part'] == 2:
        print("Part 2")
        part2(search)

def flatten_list(nested_list):
    for x in range(nested_list):
        nested_list = str(nested_list[x])
    return nested_list

def read(test=args['test']):

    reports = []

    file = "inputs.txt"
    if test:
        file = "test.txt"

    with open(file,"r") as f:
        inputs = f.read().split("\n")    
        del inputs[-1]
    return inputs

def turn_diag(x, y, word_search):
    counter = 0
    turn45 = [[] for i in range(0, 2 * x)]
    turn225 = [[] for i in range(0, 2 * x)]
    turn90 = [[] for i in range(x)]
    while counter < 2 * x:
        for i in range(0, x):
            for j in range(0, y):
                if i + j == counter:
                    turn45[counter].append(word_search[j][i])
                    turn225[counter].append(word_search[i][(y - 1)-j])
        counter = counter + 1
    for i in range(0, x):
        for j in range(0, y):
            turn90[i].append(word_search[j][i])
    return turn45, turn225, turn90 

def collapse_array(arr):
    collapse = []
    for row in arr:
        collapse.append("".join(row))
    return collapse 
        
def part1(search):
    rightdiag, leftdiag, turn90 = turn_diag(len(search), len(search[0]), search)

    leftdiag = collapse_array(leftdiag)
    rightdiag = collapse_array(rightdiag)
    search = collapse_array(search)
    turn90 = collapse_array(turn90)

    count = 0
    count = count + sum([x.count('XMAS') for x in rightdiag])
    count = count + sum([x.count('SAMX') for x in rightdiag])
    count = count + sum([x.count('XMAS') for x in leftdiag])
    count = count + sum([x.count('SAMX') for x in leftdiag])
    count = count + sum([x.count('XMAS') for x in turn90])
    count = count + sum([x.count('SAMX') for x in turn90])
    count = count + sum([x.count('XMAS') for x in search])
    count = count + sum([x.count('SAMX') for x in search])
    print(count)

def part2(search):
    counter = 0
    for x in range(len(search)-2):
        for y in range(len(search[0])-2):
            if search[y+1][x+1] == 'A':
                if ((search[y][x] == 'M' and search[y+2][x+2] == 'S') or (search[y][x] == 'S' and search[y+2][x+2] == 'M')):
                    if ((search[y+2][x] == 'M' and search[y][x+2] == 'S') or (search[y+2][x] == 'S' and search[y][x+2] == 'M')):
                        counter = counter + 1
    print(counter)

main()
