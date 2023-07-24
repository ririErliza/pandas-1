import pandas as pd

''' Load data into pandas '''

df = pd.read_csv('pokemon_data.csv')

print(df.head())

print(df)

print(df.tail(3))


# dfTxt = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(dfTxt)


#'''  Read headers  '''
print(df.columns)


#'''  Read each column  '''
print(df['Name'])

print(df[['Name', 'Type 1', 'HP']])


#'''  Read each row  '''
print(df.head(4))

print(df.iloc[5])

print(df.iloc[11:14])

for index, row in df.iterrows():
    print(index, row['Name'])

print(df.loc)

#''' Read a specific location (R,C)'''
print(df.iloc[2,1]) #Venusaur

