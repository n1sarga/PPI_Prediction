import pandas as pd

df = pd.read_csv('input_file_location')

df['Identifier A'] = df['Identifier A'].str.replace('UniProt', '')
df['Identifier B'] = df['Identifier B'].str.replace('UniProt', '')

df.to_csv('output_file_location', index=False)