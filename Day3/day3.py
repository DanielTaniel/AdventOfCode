##########################################
# Description 
#
#
#########################################
from pprint import pprint
import argparse
import re

parser = argparse.ArgumentParser("AoC_Day_2")

parser.add_argument("-t", "--test", help="use test data", nargs="?", const=False)
args = vars(parser.parse_args())


def read_and_split(test=args['test']):

    reports = []

    file = "inputs.txt"
    if test:
        file = "test.txt"

    with open(file,"r") as f:
        inputs = f.read()
    
    return inputs 


    #pprint(reports)
#pprint(read_and_split())
patern = r"mul\((\d{1,3}),(\d{1,3})\)"
mult = re.findall(patern, read_and_split())
mult = [(int(x), int(y)) for x, y in mult ]
pprint(mult)

total = sum([(x*y) for x, y, in mult])

pprint(total)
