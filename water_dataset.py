import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

water = pd.read_csv('waterquality.csv')

water = water.dropna(subset=['Salinity (ppt)','DissolvedOxygen (mg/L)','SecchiDepth (m)','WaterTemp (C)','AirTemp (C)'])

water['Date'] = pd.to_datetime(water['Date'])

plt.figure(figsize=(10,10))

def water_param_over_time(parameter, subplot_index):
    print(f"Plotting {parameter.name}...")
    plt.subplot(3,2,subplot_index)
    sns.lineplot(x='Date', y=parameter.name,data=water)
    plt.xlabel('Date')
    plt.ylabel(parameter.name)
    plt.title(f'{parameter.name} over Time')
    plt.xticks(rotation=45)

water_param_over_time(water['Salinity (ppt)'],1)
water_param_over_time(water['DissolvedOxygen (mg/L)'],2)
water_param_over_time(water['SecchiDepth (m)'],3)
water_param_over_time(water['WaterTemp (C)'],4)
water_param_over_time(water['AirTemp (C)'],5)

plt.tight_layout()
plt.show()
