import pandas as pd 
#df=pd.read_csv("disney_princess_popularity_dataset_300_rows.csv")
#creating a data frame
data = { "name": ['rahma', 'hayaa', 'engy','sara'],"age": [21, 20, 19,21] } 
df= pd.DataFrame(data)
print(df)
print(" ")
#creating a df with specifying a columns names:
data = [['rahma',21],['hayaa',20],['engy',19],['sara',21]] 
# load data into a DataFrame object:
df2= pd.DataFrame(data,columns=['name','age']) 
print(df2)
print(" ")
#printing a specific numbers of rows 
df3=pd.read_csv("disney_princess_popularity_dataset_300_rows.csv") print(df3.head(15))
print(" ")
#printing a specific numbers of columns(one column): 
df4=pd.read_csv("disney_princess_popularity_dataset_300_rows.csv") 
print(df4['RottenTomatoesScore'])
print(" ")
#printing a specific numbers of columns(multiple column): 
df5=pd.read_csv("disney_princess_popularity_dataset_300_rows.csv") 
print(df5[['RottenTomatoesScore','FirstMovieYear']])
print(" ")