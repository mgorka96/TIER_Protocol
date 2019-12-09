import pandas as pd

df=pd.read_csv("C:/Users/Michał/Desktop/S7/AiBD/TIER Protocol Documentation/Original Data/drinks.csv")
print(df)
df = pd.melt(df, id_vars=["country"], value_name="amount", var_name="alcohol")
print(df)
df = df.sort_values(ascending=True,by=["country", "alcohol", "amount"])
print(df)
df.to_csv("C:/Users/Michał/Desktop/S7/AiBD/TIER Protocol Documentation/Analysis Data/mod_drinks.csv", index=None)