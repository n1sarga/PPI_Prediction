import pandas as pd
import os

directory = 'D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Positive_Negative_Interactions'

dfs = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.drop_duplicates(inplace=True)

merged_df.to_csv('D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Maize_All_Interactions.csv', index=False)