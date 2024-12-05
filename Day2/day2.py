##########################################
# Description 
#
#
#########################################
from pprint import pprint
import argparse

parser = argparse.ArgumentParser("AoC_Day_2")

parser.add_argument("-t", "--test", help="use test data", nargs="?", const=False)
parser.add_argument("-d", "--debug", help="enable debug stuff", nargs="?", const=False)
parser.add_argument("-m", "--mode", help="what mode are you using? count or freq", type=str)
args = vars(parser.parse_args())

def read_and_split(test=args['test']):

    reports = []

    file = "inputs.txt"
    if test:
        file = "test.txt"

    with open(file,"r") as f:
        inputs = f.read()
    
    inputArr = inputs.split("\n")
    # The last item in the list is empty so chuck it
    del inputArr[-1]
    #pprint(inputArr)

    for x in inputArr:
        reports.append(x.split())

    reports = [[int(x) for x in group] for group in reports]

    pprint(reports)
    return reports 

def main():
    reports = read_and_split()
    print("total safe rows: ", check_report(reports))


def check_report(reports):
    pprint(type(reports[0][0]))
    running_total = 0
    for x in range(0, len(reports)):
        running_total = running_total + row_is_safe(reports[x])
                                                    
    return running_total

def row_is_safe(report_row):
    temp = report_row[0]
    # if the next value in the list i asc then set to an asc test
    # otherwise set to a desc test
    if(report_row[0] < report_row[1]): 
        asc = True
    else:
        asc = False
    
    for x in range(1, len(report_row)):
        if asc:
            if temp < report_row[x] and (report_row[x] - temp ) < 4:
                temp = report_row[x]
            else:
                return 0
        else:
            if temp > report_row[x] and (temp - report_row[x]) < 4:
                temp = report_row[x]
            else:
                return 0
    return 1

main()
