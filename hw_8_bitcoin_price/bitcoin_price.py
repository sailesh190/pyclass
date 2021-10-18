"""
This is an API with the last 30 days by hour of bitcoin prices.
 
https://api.coinranking.com/v1/public/coin/1/history/30d
 
Reading that API, output data in the following schemas:
 
Schema 1:
 
 
 
{
 
    "date": "{date}",
 
    "price": "{value}",
 
    "direction": "{up/down/same}",
 
    "change": "{amount}",
 
    "dayOfWeek": "{name}",
 
    "highSinceStart": "{true/false}",
 
    "lowSinceStart": "{true/false}"
 
}
 
- one entry per day at "00:00:00" hours
 
- results ordered by oldest date first.
 
- "date" in format "2019-03-17T00:00:00"
 
- "price" in 2 decimal dollars
 
- "direction" is direction of price change since previous day in the list, first day can be "na" ({up/down/same})
 
- "change" is the price difference between current and previous day. "na" for first
 
- "dayOfWeek" is name of the day (Saturday, Tuesday, etc)
 
- "highSinceStart" true/false if highest since list start. "na" for first
 
- "highSinceStart" true/false if lowest since list start. "na" for first
 
 
 
Schema 2:
 
 
 
{
 
    "date": "{date}",
 
    "price": "{value}",
 
    "dailyAverage": "{value}",
 
    "dailyVariance": "{value}",
 
    "volatilityAlert:": "{true/false}"
 
}
 
 
 
- one entry per day
 
- results ordered by oldest date first.
 
- "date" in format "2019-03-17T00:00:00"
 
- "price" in 2 decimal dollars
 
- "dailyAverage" average of all entries for that day
 
- "dailyVariance" variance of all entries for that day
 
- "volatilityAlert:" true/false if any price that day is outside 2 standard deviations.
"""

import requests
import pandas as pd
from datetime import datetime

response = requests.get("https://api.coinranking.com/v1/public/coin/1/history/30d")

df = pd.DataFrame(response.json()["data"]["history"])

df_1 = df.copy()

df_1["price"] = round(pd.to_numeric(df_1["price"]), 2)

df_1["datetime"] = [datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%dT%H:%M:%S") for ts in df_1["timestamp"]]

df_1["dayOfWeek"] = [datetime.fromtimestamp(ts/1000).strftime("%A") for ts in df_1["timestamp"]]

df_1 = df_1.drop(columns=["timestamp"])

df_1 = df_1.loc[df_1["datetime"].str.contains("00:00:00")]

df_1 = df_1.rename(columns={"datetime": "date"})

direction = [None]

change = [None]

highSinceStart = [None]

lowSinceStart = [None]

for i in range(1, len(df_1["price"])):
    
    if df_1["price"].iloc[i] > df_1["price"].iloc[i - 1]:
        
        direction.append("up")
        
    elif df_1["price"].iloc[i] < df_1["price"].iloc[i - 1]:
        
        direction.append("down")
        
    elif df_1["price"].iloc[i] == df_1["price"].iloc[i - 1]:
        
        direction.append("same")
    
    change.append(df_1["price"].iloc[i] - df_1["price"].iloc[i - 1])
    
    if df_1["price"].iloc[i] > max(df_1["price"].iloc[:i]):
        
        highSinceStart.append(True)
        
    else:
        
        highSinceStart.append(False)
        
    if df_1["price"].iloc[i] < min(df_1["price"].iloc[:i]):
        
        lowSinceStart.append(True)
        
    else:
        
        lowSinceStart.append(False)
        
df_1["direction"] = direction

df_1["change"] = change

df_1["highSinceStart"] = highSinceStart

df_1["lowSinceStart"] = lowSinceStart

df_1= df_1.reset_index(drop=True)

df_1[["price", "change"]] = round(df_1[["price", "change"]], 2)

df_1 = df_1[["date", "price", "direction", "change", "dayOfWeek", "highSinceStart", "lowSinceStart"]]

df_1.to_csv("df_1.csv", sep=",", na_rep="NA", header = True, index = False)

dict_1 = df_1.to_dict("records")

print("Schema 1:")

print(dict_1)

df_2 = df.copy()

df_2["price"] = round(pd.to_numeric(df_2["price"]), 2)

df_2["date"] = [datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d") for ts in df_2["timestamp"]]

df_2["datetime"] = [datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%dT%H:%M:%S") for ts in df_2["timestamp"]]

df_2 = df_2.drop(columns=["timestamp"])

df_2_copy = df_2

df_2_mean = df_2.groupby(["date"]).mean()

df_2_var = df_2.groupby(["date"]).var()

df_2_std = df_2.groupby(["date"]).std()

df_2 = pd.DataFrame({"date": df_2_mean.index, "dailyAverage": df_2_mean["price"], "dailyVariance": df_2_var["price"]})

df_2 = df_2.reset_index(drop=True)

volatilityAlert = []

for i in range(len(df_2.index)):
    
    temp_df = df_2_copy[df_2_copy["date"] == df_2["date"][i]]
    
    upper_alert = (temp_df["price"].max() > df_2["dailyAverage"][i] + 2 * df_2_std["price"][i])
    
    lower_alert = (temp_df["price"].min() < df_2["dailyAverage"][i] - 2 * df_2_std["price"][i])
        
    volatilityAlert.append(upper_alert or lower_alert)
    
df_2["volatilityAlert"] = volatilityAlert

df_2["date"] = [date + "T00:00:00" for date in df_2["date"]]

df_2 = df_2.merge(df_2_copy, how="left", left_on = "date", right_on = "datetime")

df_2 = df_2.drop(columns=["date_y", "datetime"])

df_2 = df_2.rename(columns={"date_x": "date"})

df_2[["price", "dailyAverage", "dailyVariance"]] = round(df_2[["price", "dailyAverage", "dailyVariance"]], 2)

df_2 = df_2[["date", "price", "dailyAverage", "dailyVariance", "volatilityAlert"]]

df_2.to_csv("df_2.csv", sep = ",", na_rep = "NA", header = True, index = False)

dict_2 = df_2.to_dict("records")

print("Schema 2:")

print(dict_2)