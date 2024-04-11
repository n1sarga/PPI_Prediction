import pandas as pd

df = pd.read_csv('D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Maize Positive Interactions.csv')

df['Positive interaction'] = df['Positive interaction'].replace('✔️', '1')

df.to_csv('D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Updated.csv', index=False)
