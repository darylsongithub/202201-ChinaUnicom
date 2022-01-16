import pandas as pd
import numpy as np
input_file = "gzs.csv"
df = pd.read_csv(input_file)

df_column_by_index = df.iloc[:, [28]].drop_duplicates().values

hour_index = np.array(df_column_by_index).flatten()

for hour in hour_index:
    df_value = df.loc[df['wyy_gangzhongwen_res.slicetime'].values == hour, :]

    output_file = "./hour/" + str(hour)+".csv"
    df_value.to_csv(output_file, index=False)
