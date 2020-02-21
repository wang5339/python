import  sys
import csv

input_file=sys.argv[1]
output_file=sys.argv[2]

with open(input_file,'r',newline=',') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        for row in filereader:
            ass=[]
            ass.append(row[3])
            ass.append(row[4])
            ass.append(row[5])
            filewriter.writerow(row)
