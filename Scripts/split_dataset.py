import os
import pandas as pd

df = pd.read_csv('D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Maize Positive Interactions.csv')

batch_size = 500
total_batches = len(df) // batch_size + 1 if len(df) % batch_size != 0 else len(df) // batch_size

output_dir = 'D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Maize_Split'
os.makedirs(output_dir, exist_ok=True)

for i in range(total_batches):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(df))
    batch = df[start_idx:end_idx]
    batch.to_csv(os.path.join(output_dir, f'Maize_{i+1}.csv'), index=False)