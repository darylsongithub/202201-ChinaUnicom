import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import seaborn as sns

input_file = "gzs.csv"
df = pd.read_csv(input_file) 
# 非重复项index
df_nrepeat = df.drop_duplicates(
    ['wyy_gangzhongwen_res.eci', 'wyy_gangzhongwen_res.traffic_t'], keep=False)
df_nrepeat_index = df_nrepeat.index.to_list()
df_repeat = df[~df.index.isin(df_nrepeat_index)]

output_file = "./gzs_repeat.csv"
df_repeat.to_csv(output_file, index=False)