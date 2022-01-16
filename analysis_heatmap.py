import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import seaborn as sns
import folium
import webbrowser
from folium.plugins import HeatMap

#hour = 2021061704
input_file = "gzs.csv"
df0 = pd.read_csv(input_file) 
df_column_by_index = df0.iloc[:,[28]].drop_duplicates().values

hour_index = np.array(df_column_by_index).flatten()

for hour in hour_index:
    input_file = "./hour/" +str(hour)+".csv"
    df = pd.read_csv(input_file)

    df_cell_index = df.iloc[:,[0]].drop_duplicates().values
    cell_num = np.array(df_cell_index).flatten()
    data = pd.DataFrame()
    
    for cell in cell_num:     
        df_temp = df.loc[df['wyy_gangzhongwen_res.eci'].values == cell, :]
        df_traff_sum = df_temp['wyy_gangzhongwen_res.eci_traff'].sum()
        new = pd.DataFrame({\
        'Lat':df.loc[df['wyy_gangzhongwen_res.eci'].values == cell, 'wyy_gangzhongwen_res.lat'],\
        'Long':df.loc[df['wyy_gangzhongwen_res.eci'].values == cell, 'wyy_gangzhongwen_res.lon'],\
        'Traff':df_traff_sum})
        data=data.append(new,ignore_index=True)
    data = data.drop_duplicates().reset_index(drop=True)
    normal = (data['Traff']-data['Traff'].min())/(data['Traff'].max()-data['Traff'].min())
    data2 = data.drop(['Traff'],axis=1)
    data2['Traff'] = normal
    data2 = data2.values.tolist()
    m = folium.Map([22.69,114.20], zoom_start=16)
    HeatMap(data2).add_to(m)
    output_file = "./Heatmap/Cell_HeatMap_"+str(hour)[4:8]+"_"+str(hour)[8:10]+".html"
    m.save(output_file)

