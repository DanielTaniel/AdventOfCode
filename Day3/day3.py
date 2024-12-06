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
parser.add_argument("-p", "--part", help="part 1 or 2?", type=int, default=1)
args = vars(parser.parse_args())

def read_data(test=args['test']):

    reports = []

    file = "inputs.txt"
    if test:
        file = "test.txt"

    with open(file,"r") as f:
        inputs = f.read()
    
    return inputs 

def strip_donts(text):
    return re.sub(r"don\'t\(\).*?do\(\)", "[REPLACED]", text, flags=re.DOTALL)

def calc_mults(text):

    patern = r"mul\((\d{1,3}),(\d{1,3})\)"
    mult = re.findall(patern, text)
    mult = [(int(x), int(y)) for x, y in mult ]

    return sum([(x*y) for x, y, in mult])

def main():
    pprint(args) 
    if args['part'] == 1:
        pprint(calc_mults(read_data()))
    elif args['part'] == 2:
        text = strip_donts(read_data())
        pprint(text)
        pprint(calc_mults(text))

    else:
        print("what was that? ")

main()
