import pandas as pd
import matplotlib.pyplot as plt
from wwo_hist import retrieve_hist_data
import os
os.chdir(".")
df = pd.read_csv('AC_Data.csv')
Power_consumption = []
for col in df.drop(['0'], axis =1 ).columns:
    Power_consumption.append(df[col].sum())
print("The Most Used AC is AC",Power_consumption.index(max(Power_consumption))+1)
print("The Least Used AC is AC",Power_consumption.index(min(Power_consumption))+1)

Ac1 = list(df.fillna(0)["AC 1"])
Ac1 = [round(num,2) for num in Ac1]
count=[]
for i in range(0,len(Ac1)):
    k = i+1
    match = 0
    for j in range(k,len(Ac1)):
        if Ac1[i] == Ac1[j] and Ac1[i] != 0:
            match = match +1
    count.append(match)
print(count)

frequency = 1
start_date = '01-AUG-2019'
end_date = '30-SEP-2019'
api_key = 'API_KEY'
location_list = ['GURGAON']
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)




