import pandas as pd
import sys
input_file=sys.arge[1]
output_file=sys.arge[2]
data_frame=pd.read_csv(input_file)
data_frame['Cost']=data_frame['Cost'].str.strip('$').astype(float)
