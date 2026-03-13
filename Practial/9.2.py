import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

avg = df["age"].mean()
print("\nAverage age of students:", avg)
