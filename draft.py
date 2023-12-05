import pandas as pd

data_df=pd.read_csv("D:\\Documents\\NCKH\data\\Data Readability 12.2021.csv")

Readability_Variable = pd.read_csv("D:\\Documents\\NCKH\\data\\Variabe.csv")


df=pd.read_csv("D:\\Documents\\NCKH\\data\\Book2.csv")
Ten=df['Ten_bien']
#Char_Easy variable
Char_Easy_Row=pd.DataFrame({'Char_Easy':((data_df['so_chu_de']/data_df['so_chu'])*100)})

#Other variable:
Char_Dens_Row=pd.DataFrame({'Char_Dens':((data_df['tong_tan_suat_chu']/data_df['so_chu'])*100)})

Char_Order_Row=pd.DataFrame({'Char_Order':((data_df['tong_thu_hang_chu']/data_df['so_chu'])*100)})

Word_Easy_Row=pd.DataFrame({'Word_Easy':((data_df['so_tu_de']/data_df['so_tu'])*100)})

Word_Borrow_Row=pd.DataFrame({'Word_Borrow':((data_df['so_tu_muon']/data_df['so_tu'])*100)})

Word_1mean_Row=pd.DataFrame({'Word_1mean':((data_df['so_tu_co_1_nghia']/data_df['so_tu'])*100)})

Word_2mean_Row=pd.DataFrame({'Word_2mean':((data_df['so_tu_co_2_nghia']/data_df['so_tu'])*100)})

Word_3mean_Row=pd.DataFrame({'Word_3mean':((data_df['so_tu_co_3_nghia']/data_df['so_tu'])*100)})

Word_3mean_Row=pd.DataFrame({'Word_3mean':((data_df['so_tu_co_3_nghia']/data_df['so_tu'])*100)})

frames=[Char_Easy_Row, Char_Dens_Row, Char_Order_Row, Word_Easy_Row, Word_Borrow_Row, Word_1mean_Row, Word_2mean_Row, Word_3mean_Row]
result = pd.concat(frames).describe().transpose()

#{1:{2:3}} dictionary     

#col_list = list(data_df.columns)
#dfs = [data_df[col_name].tolist() for col_name in col_list]

#for ten in Ten:
    #ten = pd.DataFrame({'ten':((data_df['B']/data_df['C'])*100)})
    #B= df.loc[:,'B']
    #C= df.loc[:,'C']


#easy stuff???
x = df['x']
y = df['y']

datX = data_df[x]
datY = data_df[y]
datX.columns=Ten
datY.columns=Ten

Res = pd.DataFrame(index=datX.index, columns=datX.columns)

for i in datY.index:
  # Dividing the ith row of df1 by the values of the ith row of df2
  # and assigning it to the ith row of df3
  Res.loc [i] = ((datX.loc [i] / datY.loc [i].values)*100)
  
Res.astype(int).describe().transpose()
  
  
for col in Res.columns:
  # Applying the describe method on each column and printing the result
  resList=[Res[col]]
  
  
result = pd.concat(resList).describe().transpose()


#col_list = list(data_df.columns)
#result = [data_df[col_name].tolist() for col_name in col_list]

#or col_name in x:
 #   for index, row in data_df.iterrows():
  #      print(row[col_name])

#row.to_csv('row.csv', index=False)

#x = df['x'][0]
#y = df['y'][0]

#for variable in x: datX = data_df[x]

#for variable in y: datX = data_df[x]

#z = df['Ten_bien'][0]

#Some_List = [([x]/[y])*100]
#Some_Row=pd.DataFrame({z:Some_List}).describe().transpose()

#Char_Easy_List = ((data_df['so_chu_de']/data_df['so_chu'])*100)
#Char_Easy_Row=pd.DataFrame({'Char_Easy':Char_Easy_List}).describe().transpose()