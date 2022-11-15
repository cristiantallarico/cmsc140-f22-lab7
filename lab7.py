import pandas as pd 

df = pd.read_csv("city_temperature.csv")

regions = df.groupby(by = "Region")

idx_max = regions["AvgTemperature"].idxmax()

city = df.groupby(by = "City")

max_temps = df.loc[idx_max]

#print(city.head(2))

print(idx_max)
print(max_temps)

max_temps.to_csv("temps_edited.csv")



