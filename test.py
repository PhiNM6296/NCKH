import pandas as pd
import pyreadstat as pyr
import numpy as np
import re
    
#    CeoOwnerShipDTA_df.to_csv('CEOStuff.csv', index=False)

#Readatbility_do_df, meta = pyr.read_stata('C:\\Users\\Admin\\Downloads\\Readability 15.12.2021.do')

data_df=pd.read_csv("D:\\Documents\\NCKH\data\\Data Readability 12.2021.csv")

statistics_df=pd.read_csv("D:\\Documents\\NCKH\\data\\Statistics.csv")

#data = pd.read_csv("C:\\Users\\Admin\\Downloads\\Readability 15.12.2021.do", delimiter=' ')

################
# table 1a:
#Create a column of Years from Filename
statistics_df['Years'] = statistics_df['Filename'].str.extract(r'_(\d{4})\.txt')
# Create a freq_table
freq_table = statistics_df['Years'].value_counts().reset_index()
freq_table.columns = ['Years', 'Frequency']

freq_table['Percentage'] = (freq_table['Frequency'] / freq_table['Frequency'].sum()) * 100
# Create a cumulative frequency table of years
freq_table['Cum.'] = freq_table['Frequency'].cumsum()
#import to csv file
freq_table.to_csv('table1.csv', index=False)

################

################
# table 2a:

#Simple describe of data
testtable=data_df.describe()
#Take list of variable:
Readability_Variable = pd.read_csv("D:\\Documents\\NCKH\\data\\Variabe.csv")
Readability_Variable_list = Readability_Variable['Variable'].tolist()
#Create table with given variable
Table2a = pd.DataFrame({'Variable': Readability_Variable_list})

#Try to make it easier
Readability_Variable = pd.read_csv("D:\\Documents\\NCKH\\data\\Variabe.csv")

#Char_Easy variable
Char_Easy_List = ((data_df['so_chu_de']/data_df['so_chu'])*100).tolist()
Char_Easy_Row=pd.DataFrame({'Char_Easy':Char_Easy_List}).describe().transpose()

#Other variable:
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


#....



frames=[Char_Easy_Row, Char_Dens_Row, Char_Order_Row, Word_Easy_Row, Word_Borrow_Row, Word_1mean_Row, Word_2mean_Row, Word_3mean_Row]
result = pd.concat(frames,ignore_index=True).describe().transpose()

result.to_csv('result.csv', index=False)

#Nhanh hơn nhưng hình như đoạn này sai số lớn

Table2a_var_df=pd.read_csv("D:\\Documents\\NCKH\\data\\Book2.csv")
Ten=Table2a_var_df['Ten_bien']
x = Table2a_var_df['x']
y = Table2a_var_df['y']

datX = data_df[x]
datY = data_df[y]
datX.columns=Ten
datY.columns=Ten

Table2a = pd.DataFrame(index=datX.index, columns=datX.columns)

for i in datY.index:
  # Dividing the ith row of df1 by the values of the ith row of df2
  # and assigning it to the ith row of df3
  Table2a.loc [i] = ((datX.loc [i] / datY.loc [i].values)*100)
  
Table2a_an=Table2a.astype(float).describe().transpose()

Table2a_an.to_csv('Table2a.csv', index=False)


################

################
# table 2b:

#table2b_var_df=pd.read_csv("D:\\Documents\\NCKH\\data\\Book3.csv")
#table2b = pd.DataFrame(index=table2b_var_df['Variable'])

CEO_df=pd.read_csv("D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\CEO2.csv")
#CeoOwnerShipDTA_df= pd.read_stata("C:\\Users\\Admin\\Downloads\\Readability - BCTC - CEO - Ownership 18.7.2022.dta")
#for ons in CeoOwnerShipDTA_df['TotalAssets']:
 #CeoOwnerShipDTA=pd.DataFrame(Decimal(CeoOwnerShipDTA_df['TotalAssets']))
#CEO_df['Log_TotalAssets'] = np.log(CEO_df['TotalAssets'])
 #TA=CeoOwnerShipDTA_df['TotalAssets'].dropna()
R1=pd.DataFrame({'SIZE':np.log(CEO_df['TotalAssets'])})

R2=pd.DataFrame({'ROE':CEO_df['ProfitAfterTax']/CEO_df['Equity'] })

R3=pd.DataFrame({'ROA':CEO_df['ProfitAfterTax']/CEO_df['TotalAssets'] })

R4=pd.DataFrame({'ROS':CEO_df['ProfitAfterTax']/CEO_df['Revenue_Net']})

R5=pd.DataFrame({'LEV':CEO_df['Debt']/CEO_df['TotalAssets'] })

R6=pd.DataFrame({'FOR':CEO_df['FOR'] })

R7=pd.DataFrame({'GOV':CEO_df['GOV'] })

R8=pd.DataFrame({'CHAIR':CEO_df['CHAIR'] })

R9=pd.DataFrame({'Duality':CEO_df['Duality'] })

R10=pd.DataFrame({'CEO1':CEO_df['CEO'] })

R11=pd.DataFrame({'BSIZE':CEO_df['BoardMember'] })

frames2=[R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11]
Y=pd.concat(frames2, axis=1)
result2b = pd.concat(frames2, axis = 1).describe().transpose()

result2b.to_csv('table2.csv', index=False)

################

################
# table 4a:

df_combined = pd.concat([Table2a, Y], axis=1)

# Tính toán correlation
correlation_matrix = df_combined.corr()

################

################
# table 4b:




################

################
# table 4c:




################



import pandas as pd
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

# Create sample DataFrames
data_ABC = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 5, 4, 5], 'C': [3, 1, 4, 2, 5]}
data_DEFG = {'D': [0.1, 0.2, 0.3, 0.4, 0.5],
             'E': [0.6, 0.7, 0.8, 0.9, 1.0],
             'F': [1.1, 1.2, 1.3, 1.4, 1.5],
             'G': [1.6, 1.7, 1.8, 1.9, 2.0]}

df_ABC = pd.DataFrame(data_ABC)
df_DEFG = pd.DataFrame(data_DEFG)

# Add a constant term to the independent variables
X = sm.add_constant(df_DEFG)

# Fit OLS models for each dependent variable
model_A = sm.OLS(df_ABC['A'], X).fit()
model_B = sm.OLS(df_ABC['B'], X).fit()
model_C = sm.OLS(df_ABC['C'], X).fit()

# Create a summary table for OLS regression results
results_table = summary_col([model_A, model_B, model_C], stars=True, float_format='%0.4f',
                            model_names=['Dependent A', 'Dependent B', 'Dependent C'],
                            info_dict={'N': lambda x: "{0:d}".format(int(x.nobs)),
                                       'R2': lambda x: "{:.4f}".format(x.rsquared)})

# Print the regression results table
print(results_table)