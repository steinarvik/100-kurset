import pandas as pd
import os

directory = 'excel_files'

filenames = os.listdir(directory)
filepaths = [os.path.join(directory, filename) for filename in filenames]

dataframes = []

for filepath in filepaths:
    df = pd.read_excel(filepath)
    dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index = True)
print(merged_df)
merged_df.to_excel('merged.xlsx', index=False)