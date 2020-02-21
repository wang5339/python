import sys
import csv

input_file=sys.argv[1]
output_file=sys.argv[2]
i=0
row_list = []

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=" ")
        filewriter = csv.writer(csv_out_file,delimiter=" ")
        for row in filereader:
            i=i+1
            row_list.append(row)
            if i==20:
                filewriter.writerow(row_list)
                i=0
                row_list = []
