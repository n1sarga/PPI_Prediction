import numpy as np
import pandas as pd
from scipy.fftpack import dst
import os

def apply_dst(pssm):
    # Column-wise DST
    dst_col = np.apply_along_axis(dst, axis=0, arr=pssm)
    # Row-wise DST on column-wise DST
    dst_full = np.apply_along_axis(dst, axis=1, arr=dst_col)
    return dst_full

def transform_and_save_pssm(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    pssm_files = [f for f in os.listdir(input_folder) if f.endswith('.parquet')]
    
    for pssm_file in pssm_files:
        pssm_path = os.path.join(input_folder, pssm_file)
        pssm = pd.read_parquet(pssm_path)
        pssm_array = pssm.values
        dst_transformed = apply_dst(pssm_array)
        dst_df = pd.DataFrame(dst_transformed, columns=pssm.columns)

        output_path = os.path.join(output_folder, pssm_file)
        dst_df.to_parquet(output_path)

input_folder = 'C:\\Users\\nextn\\Downloads\\400\\pssm_profiles'
output_folder = 'C:\\Users\\nextn\\Downloads\\400\\DST\\DST_Profiles'
transform_and_save_pssm(input_folder, output_folder)