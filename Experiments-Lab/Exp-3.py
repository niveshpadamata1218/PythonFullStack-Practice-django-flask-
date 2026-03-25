import pandas as pd
df = pd.DataFrame({
    'S.no': [1, 2, 3],
    'rno': [100, 200, 300],
    'name': ["nivesh", "nivesh", "nivesh"]
})
pf=pd.read_csv("canada_per_capita_income.csv")
print(pf)
print(df)
