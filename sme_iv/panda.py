import os
import csv
current_path1 = os.getcwd()
csv_1 = "data.csv"
absolute_path_csv_1 = os.path.join(current_path1, 'IVQA', 'Py_Dee', csv_1)

import pandas as pd 
df =pd.read_csv(absolute_path_csv_1)
print(df.head())