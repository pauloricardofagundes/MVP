import pandas as pd

## Lista de datasets a serem utilizados para consolidar o arquivo final
Databases = {'https://raw.githubusercontent.com/pauloricardofagundes/MVP/main/credit_card_transactions_1.csv',
             'https://raw.githubusercontent.com/pauloricardofagundes/MVP/main/credit_card_transactions_2.csv',
             'https://raw.githubusercontent.com/pauloricardofagundes/MVP/main/credit_card_transactions_3.csv'}

## Leitura dos datasets da lista e consolida todos em um único dataset

df_list = []
for filename in sorted(Databases):
    df_list.append(pd.read_csv(filename, dtype='str',header=None).set_index(0))
full_df = pd.concat(df_list)

print(full_df.columns)
full_df = full_df.rename(columns=full_df.iloc[0]).drop(full_df.index[0])
print (full_df)
full_df.to_csv(r'D:\Documentos\iCloud\iCloudDrive\Dev\teste.csv', sep='|', index=False)