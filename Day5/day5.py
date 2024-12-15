##########################################
# Description 
#
#
#########################################
from pprint import pprint
import argparse
import re

parser = argparse.ArgumentParser("AoC_Day_5")

parser.add_argument("-t", "--test", help="use test data", nargs="?", const=False)
parser.add_argument("-p", "--part", help="part 1 or 2?", type=int, default=1)
args = vars(parser.parse_args())

def read(test=args['test']):

    rules_file = "inputs-rules.txt"
    pages_file = "input-pages.txt"
    if test:
        rules_file = "test-rules.txt"
        pages_file = "test-pages.txt" 
    
    with open(rules_file,"r") as f:
        rules_inputs = f.read().split("\n")    
        del rules_inputs[-1]

    with open(pages_file, "r") as f:
        pages_inputs = f.read().split("\n")
        del pages_inputs[-1]
    return input_to_rules(rules_inputs), input_to_pages(pages_inputs)

def input_to_rules(rules):
    for i in range(len(rules)):
        rules[i] = rules[i].split("|")
        rules[i][0] = int(rules[i][0])
        rules[i][1] = int(rules[i][1])
    return rules

def input_to_pages(pages):
    for i in range(len(pages)):
        pages[i] = pages[i].split(",")
        pages[i] = [int(x) for x in pages[i]]
    return pages

def check_valid(rules, page):
    counter = 0
    for r in rules:
        try:
            if not page.index(r[0]) <  page.index(r[1]):
                return 0 
        except Exception as e:
            pass
    counter = counter + page[len(page)//2]
    return counter

def check_rules(rules, pages):
    counter = 0
    for p in pages:
        valid_rules = []
        t_r = rules
        for i in t_r:
            if (i[0] in p) and (i[1] in p): 
                valid_rules.append(i)
                
        # now we should have a list of all the valid rules to check them against the pages
        counter = counter + check_valid(valid_rules, p)
    return counter 

def main():
    rules, pages = read()
    if args['part'] == 1:
        pprint(check_rules(rules, pages))
        print('part1')
    if args['part'] == 2:
        print('part 2')

main()
