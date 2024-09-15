import pandas as pd


Databases = {}

df = pd.read_csv('https://raw.githubusercontent.com/pauloricardofagundes/MVP/c85a753b69764764c7d605d8c61b3bd5f2eeade2/car_insurance_claim.csv',sep=',')
resumo = df.head()
print(resumo)