import csv
import sys

input_file=sys.argv[1]
output_file=sys.argv[2]

values_cnt={}

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        for row in filereader:
            values_cnt[row[1]]=values_cnt.get(row[1],0)+1
        print(values_cnt)
        for row_key in values_cnt.keys():
            values_cnt[row_key]=values_cnt[row_key]//100*100
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        for row in filereader:
            if(values_cnt[row[1]]!=0):
                filewriter.writerow(row)
                values_cnt[row[1]]=values_cnt[row[1]]-1