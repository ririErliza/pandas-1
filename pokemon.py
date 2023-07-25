import pandas as pd
import re

''' Load data into pandas '''

df = pd.read_csv('pokemon_data.csv')

# print(df.head())

# print(df)

# print(df.tail(3))


# dfTxt = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(dfTxt)


'''  Read headers  '''
# print(df.columns)


'''  Read each column  '''
# print(df['Name'])

# print(df[['Name', 'Type 1', 'HP']])


'''  Read each row  '''
# for index, row in df.iterrows():
#     print(index, row['Name'])

# print(df.head(4))

# print(df.iloc[5])

# print(df.iloc[11:14])

#print(df.loc[df['Type 1']=='Grass'])

''' Read a specific location (R,C)'''
#print(df.iloc[2,1]) #Venusaur


''' useful methods '''
#print(df.describe())

#print(df.sort_values('Name', ascending=False))

#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


'''  Making Changes to Data Frame  '''
#print(df.head(5))

#    #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0  1              Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
# 1  2                Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
# 2  3               Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
# 3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False
# 4  4             Charmander   Fire     NaN  39      52       43       60       50     65           1      False

#df['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# the code above is the same as below
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

#print(df['Total'])

#print(df.head(5))

#    #                   Name Type 1  ... Generation  Legendary  Total
# 0  1              Bulbasaur  Grass  ...          1      False    318
# 1  2                Ivysaur  Grass  ...          1      False    405
# 2  3               Venusaur  Grass  ...          1      False    525
# 3  3  VenusaurMega Venusaur  Grass  ...          1      False    625
# 4  4             Charmander   Fire  ...          1      False    309

''' Rearranging Column '''
#deleting column
#df = df.drop(columns=['Total'])

#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

#print(df.head(5))

#    #                   Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0  1              Bulbasaur  Grass  Poison    318  45      49       49       65       65     45           1      False
# 1  2                Ivysaur  Grass  Poison    405  60      62       63       80       80     60           1      False
# 2  3               Venusaur  Grass  Poison    525  80      82       83      100      100     80           1      False
# 3  3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123      122      120     80           1      False
# 4  4             Charmander   Fire     NaN    309  39      52       43       60       50     65           1      False


'''  Saving Our Data (CSV, Excel, TXT, etc)  '''

#df.to_excel('modified.xlsx')
#df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified.txt', index=False, sep='\t')



'''  Filtering Data  '''

# df.loc[df['Type 1']== 'Grass']

#df= df.loc[(df['Type 1']=='Grass') | (df['Type 2'] == 'Poison')]

# df= df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == 'Poison')]

#df= df.loc[(df['Type 1']=='Grass') & (df['Type 2'] == 'Poison') & (df['HP']> 70)]

#print(df.head(20))

#df = df.reset_index()

#df.to_csv('filtered.csv')

#        #                   Name Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 2      3               Venusaur  Grass  Poison    525   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass  Poison    625   80     100      123      122      120     80           1      False
# 50    45              Vileplume  Grass  Poison    490   75      80       85      110       90     50           1      False
# 77    71             Victreebel  Grass  Poison    490   80     105       65      100       70     70           1      False
# 652  591              Amoonguss  Grass  Poison    464  114      85       70       85       80     30           5      False


# df = df.loc[df['Name'].str.contains('Mega')]
# print(df)


# print("No Mega")
# df = df.loc[~df['Name'].str.contains('Mega')]
# print(df)

# df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex = True)]
# print(df)

#        #                   Name Type 1  Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0      1              Bulbasaur  Grass  Poison   45      49       49       65       65     45           1      False
# 1      2                Ivysaur  Grass  Poison   60      62       63       80       80     60           1      False
# 2      3               Venusaur  Grass  Poison   80      82       83      100      100     80           1      False
# 3      3  VenusaurMega Venusaur  Grass  Poison   80     100      123      122      120     80           1      False
# 4      4             Charmander   Fire     NaN   39      52       43       60       50     65           1      False
# ..   ...                    ...    ...     ...  ...     ...      ...      ...      ...    ...         ...        ...
# 735  667                 Litleo   Fire  Normal   62      50       58       73       54     72           6      False
# 736  668                 Pyroar   Fire  Normal   86      68       72      109       66    106           6      False
# 740  672                 Skiddo  Grass     NaN   66      65       48       62       57     52           6      False
# 741  673                 Gogoat  Grass     NaN  123     100       62       97       81     68           6      False
# 799  721              Volcanion   Fire   Water   80     110      120      130       90     70           6       True

#df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)] #filter the name that start with Pi
#df = df.loc[df['Name'].str.contains('Pi', regex = True)] # this works too but 'MeloettaPirouette Forme' got included
#print(df)

'''  Conditional Changes  '''

# df.loc[df['Type 1']== 'Fire', 'Type 1'] = 'Flamer'
# changing Type 1 that is Fire to Flamer

# df.loc[df['Type 1']== 'Fire', 'Legendary'] = True
# changing the Legendary to True for all Type 1 that is Fire
print(df)

