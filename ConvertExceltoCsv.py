import pandas

df = pandas.read_excel("europe.xlsx")

###  df.to_csv("europe.csv")
df.to_csv('europe.csv', index=False)

