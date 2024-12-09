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
parser.add_argument("-e", "--error", help="what is the tolerance level of the reactor", nargs="?", type=int, const=0, default=0)
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

    #pprint(reports)
    return reports 

def main():
    #pprint(args)
    reports = read_and_split()
    print("total safe rows: ", check_report(reports)
)


def check_report(reports):
    #pprint(type(reports[0][0]))
    running_total = 0
    for x in range(0, len(reports)):
        #running_total = running_total + row_is_safe(reports[x])
        temp = reports[x][::-1]
        if(any([
            recursive_row_safe(reports[x]), 
            recursive_row_safe(temp)
        ])):
            print("----")
            print("success")
            pprint(reports[x])
            print("----")
            running_total = running_total + 1
                                                    
    return running_total

def row_is_safe(report_row):
    temp = report_row[0]
    # use list comp to find if there are more values less than or greater than the first value in the list 
    if(len([i for i in report_row if i > report_row[0]]) > len([i for i in report_row if i < report_row[0]]) ): 
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

#The issue with this code is that any result could be removed, not just the ones after the first
def recursive_row_safe(report_row, tolerance=1):
    error_count = 0
    temp = report_row[0]
    if(len([i for i in report_row if i > report_row[0]]) > len([i for i in report_row if i < report_row[0]]) ): 
        asc = True
    else:
        asc = False

    for x in range(1, len(report_row)):
        if error_count > tolerance:
            pprint("failed with ")
            pprint(report_row)
            return 0;
        elif asc:
            if temp < report_row[x] and ((report_row[x] - temp ) < 4):
                temp = report_row[x]
            else:
                error_count = error_count + 1
        elif not asc:
            if temp > report_row[x] and ((temp - report_row[x]) < 4):
                temp = report_row[x]
            else:
                error_count = error_count + 1
    return 1





main()
