import pandas as pd
import numpy as np

data_df=pd.read_csv("D:/Documents/NCKH/data/Readability_BCTC_CEO_Ownership.csv")

# Count the number of observations
#count = df.shape[0]
#print("Number of observations:", count)

# Drop rows with missing values in the 'so_chu_de' column
#data_df = data_df.dropna(subset=['so_chu_de'])
data_df = data_df[~data_df['so_chu_de'].isnull()]
# Exclude rows where 'Year' is missing
data_df = data_df[~data_df['Year'].isnull()]


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

#CEO_df=pd.read_csv("D:\\Documents\\NCKH\\data\\VeryCool2.csv")

# Extract a specific column into a new DataFrame
#column_to_extract = 'Column2'
#CEO_df_extracted = CEO_df['TotalAssets'].copy()
# Remove null rows in each column independently
#CEO_df_cleaned = CEO_df['TotalAssets'].copy().dropna()
#data_df['TotalAssets'] = data_df['TotalAssets'].astype(float)
data_df['TotalAssets'] = pd.to_numeric(data_df['TotalAssets'], errors='coerce')
data_df['ProfitAfterTax'] = pd.to_numeric(data_df['ProfitAfterTax'], errors='coerce')
data_df['Revenue_Net'] = pd.to_numeric(data_df['Revenue_Net'], errors='coerce')
data_df['Debt'] = pd.to_numeric(data_df['Debt'], errors='coerce')
data_df['Equity'] = pd.to_numeric(data_df['Equity'], errors='coerce')
data_df['FOR'] = pd.to_numeric(data_df['FOR'], errors='coerce')
data_df['GOV'] = pd.to_numeric(data_df['GOV'], errors='coerce')
data_df['CEO'] = pd.to_numeric(data_df['CEO'], errors='coerce')

R1=pd.DataFrame({'SIZE':np.log(data_df['TotalAssets'])})

#R1=pd.DataFrame({'SIZE':np.log(np.array(CEO_df['TotalAssets']))})

R2=pd.DataFrame({'ROE':data_df['ProfitAfterTax']/data_df['Equity']})

R3=pd.DataFrame({'ROA':data_df['ProfitAfterTax']/data_df['TotalAssets']})

R4=pd.DataFrame({'ROS':data_df['ProfitAfterTax']/data_df['Revenue_Net']})

R5=pd.DataFrame({'LEV':data_df['Debt']/data_df['TotalAssets']})

R6=pd.DataFrame({'FOR':data_df['FOR']})

R7=pd.DataFrame({'GOV':data_df['GOV']})

#R8=pd.DataFrame({'CHAIR':data_df['CHAIR']})

#R9=pd.DataFrame({'Duality':data_df['Duality']})

R10=pd.DataFrame({'CEO':data_df['CEO']})

#R11=pd.DataFrame({'BSIZE':data_df['BSIZE']})

frames2=[R1,R2,R3,R4,R5,R6,R7,R10]
Y=pd.concat(frames2, axis=1)
result2b = pd.concat(frames2, axis = 1).describe().transpose()

result2b.to_csv('table2.csv', index=False)


#Colleration:

df_combined = pd.concat([Table2a, Y], axis=1)

# Tính toán correlation
correlation_matrix = df_combined.corr()

# Create a mask to hide the upper triangle (including the diagonal)
mask = np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)

# Apply the mask to hide duplicate values
correlation_matrix_no_duplicates = correlation_matrix.mask(mask)

correlation_matrix_no_duplicates.to_csv('correlationMat.csv', index=False)


#Regression:

test_df=pd.read_csv("D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\output_file.csv").dropna(subset=['TotalAssets','CEO1','Duality','CHAIR','FOR','Debt','Equity', 'ProfitAfterTax', 'Revenue_Net','GOV'])

test_df.to_csv('Testdf.csv', index=False)
# Extract a specific column into a new DataFrame
#column_to_extract = 'Column2'
#CEO_df_extracted = CEO_df['TotalAssets'].copy()
# Remove null rows in each column independently
#CEO_df_cleaned = CEO_df['TotalAssets'].copy().dropna()

#CleanDat = pd.read_csv("D:\\Downloads\\VSCode\\Python\\Test\\NCKH\\ResTable.csv")
################################################
CleanDat = data_df
N1=pd.DataFrame({'SIZE':np.log(CleanDat['TotalAssets'])})
#R1=pd.DataFrame({'SIZE':np.log(np.array(CEO_df['TotalAssets']))})

N2=pd.DataFrame({'ROE':CleanDat['ROE']})

N3=pd.DataFrame({'ROA':CleanDat['ROA']})

N4=pd.DataFrame({'ROS':CleanDat['ROS']})

N5=pd.DataFrame({'LEV':CleanDat['LEV']})

N6=pd.DataFrame({'FOR':CleanDat['FOR']})

N7=pd.DataFrame({'GOV':CleanDat['GOV']})

N8=pd.DataFrame({'CHAIR':CleanDat['CHAIR']})

N9=pd.DataFrame({'Duality':CleanDat['Duality']})

N10=pd.DataFrame({'CEO1':CleanDat['CEO1']})

N11=pd.DataFrame({'BSIZE':CleanDat['BSIZE']})

frames2=[N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11]
Z=pd.concat(frames2, axis=1).astype(float).dropna()

Z.to_csv('Z.csv', index=False)
############################

#)))))))))))))))))))))))))))))))))))))))))))
for i in range (437,474): 
    Z.drop(i, inplace=True)

Ten=Table2a_var_df['Ten_bien']
x = Table2a_var_df['x']
y = Table2a_var_df['y']
datX = CleanDat[x]
datY = CleanDat[y]
datX.columns=Ten
datY.columns=Ten

TableX = pd.DataFrame(index=datX.index, columns=datX.columns)

for i in datY.index:
  # Dividing the ith row of df1 by the values of the ith row of df2
  # and assigning it to the ith row of df3
  TableX.loc [i] = ((datX.loc [i] / datY.loc [i].values)*100)
  
TableX_an=TableX.astype(float).describe().transpose()



#)))))))))))))))))))))))))))))))))))))

for i, df_dependent in enumerate(df_dependent_list):
    # Combine the independent and dependent variables into a single DataFrame
    df_combined = pd.concat([df_independent, df_dependent], axis=1)

    # Extract X (independent variable) and y (dependent variable)
    X = df_combined[df_independent.columns]
    y = df_combined[df_dependent.columns[0]]  # Assuming only one dependent variable in each DataFrame

    # Add a constant term to the independent variable (X) for the intercept
    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X).fit()
#NewOLS:

#CER=pd.DataFrame({'Char_Easy':((test_df['so_chu_de']/data_df['so_chu'])*100)}).dropna()


#)))))))))))))))))))))))))))))))))))))))

import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col

# Add a constant term to the independent variables
X = sm.add_constant(Y)

X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.fillna(9999, inplace=True)  # Replace NaN with a large finite number

# Fit OLS models for each dependent variable
# Loop qua từng biến độc lập
#for col in X.columns[1:]:  # Bỏ qua cột 'const'
#    A = X[['const', col]]
#   B = TableX['CHAR_Easy']
    
 #       model = sm.OLS(B, A).fit()

#for i, ten in enumerate(Ten,1):
#   Model{'i'} = sm.OLS(Table2a['{ten}'], X).fit()


TableX = Table2a

Model_1 = sm.OLS(TableX['CHAR_Easy'].astype(float), X).fit()
Model_2 = sm.OLS(TableX['CHAR_Dens'].astype(float), X).fit()
Model_3 = sm.OLS(TableX['CHAR_Order'].astype(float), X).fit()
Model_4 = sm.OLS(TableX['WORD_Easy'].astype(float), X).fit()
Model_5 = sm.OLS(TableX['WORD_Borrow'].astype(float), X).fit()
Model_6 = sm.OLS(TableX['WORD_1mean'].astype(float), X).fit()
Model_7 = sm.OLS(TableX['WORD_2mean'].astype(float), X).fit()
Model_8 = sm.OLS(TableX['WORD_3mean'].astype(float), X).fit()
Model_9 = sm.OLS(TableX['WORD_mmean'].astype(float), X).fit()
Model_10 = sm.OLS(TableX['WORD_1pos'].astype(float), X).fit()
Model_11 = sm.OLS(TableX['WORD_2pos'].astype(float), X).fit()
Model_12 = sm.OLS(TableX['WORD_3pos'].astype(float), X).fit()
Model_13 = sm.OLS(TableX['WORD_mpos'].astype(float), X).fit()
Model_14 = sm.OLS(TableX['WORD_totaltype'].astype(float), X).fit()
Model_15 = sm.OLS(TableX['WORD_Dens'].astype(float), X).fit()
Model_16 = sm.OLS(TableX['WORD_Order'].astype(float), X).fit()
Model_17 = sm.OLS(TableX['WORD_Local'].astype(float), X).fit()
Model_18 = sm.OLS(TableX['WORD_Chinese'].astype(float), X).fit()
Model_19 = sm.OLS(TableX['WORD_Chinese1'].astype(float), X).fit()
Model_20 = sm.OLS(TableX['WORD_Chinese2'].astype(float), X).fit()
Model_21 = sm.OLS(TableX['WORD_Chinese3'].astype(float), X).fit()
Model_22 = sm.OLS(TableX['WORD_Chinese_m'].astype(float), X).fit()
Model_23 = sm.OLS(TableX['WORD_1char'].astype(float), X).fit()
Model_24 = sm.OLS(TableX['WORD_2char'].astype(float), X).fit()
Model_25 = sm.OLS(TableX['WORD_3char'].astype(float), X).fit()
Model_26 = sm.OLS(TableX['WORD_mchar'].astype(float), X).fit()
Model_27 = sm.OLS(TableX['SENT_less10'].astype(float), X).fit()
Model_28 = sm.OLS(TableX['SENT_less13'].astype(float), X).fit()

summary_col([Model_1,Model_2,Model_3])
# Create a summary table for OLS regression results
results_table = summary_col([Model_1,
Model_2,
Model_3,
Model_4,
Model_5,
Model_6,
Model_7,
Model_8,
Model_9,
Model_10,
Model_11,
Model_12,
Model_13,
Model_14,
Model_15,
Model_16,
Model_17,
Model_18,
Model_19,
Model_20,
Model_21,
Model_22,
Model_23,
Model_24,
Model_25,
Model_26,
Model_27,
Model_28,
], stars=True) #, float_format='%0.4f',
                #            model_names=Ten,
                 #           info_dict={'N': lambda x: "{0:d}".format(int(x.nobs)),
                  #                     'R2': lambda x: "{:.4f}".format(x.rsquared)})




#)))))))))))))))))))))))))))))))))))))))))
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
