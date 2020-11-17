
import pandas as pd
def clean_df(file):
    df = pd.read_csv(file)
    df['Education'].fillna(5.0, inplace=True)
    df['Residence']=df['Residence'].fillna(method='ffill')
    df['Weight']=df['Weight'].fillna(df['Weight'].mean())
    df['BP']=df['BP'].fillna(df['BP'].mean())
    df['HB']=df['HB'].fillna(df['HB'].mean())
    df['Delivery phase']=df['Delivery phase'].fillna(method='ffill')
    df['Age']=df['Age'].fillna(df['Age'].mean())
    return df

df=clean_df("/data/LBW_Dataset.csv")
print(df)
df.to_csv("/data/preprocessed.csv")

