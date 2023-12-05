import pandas as pd
import statsmodels.api as sm

# Read the Stata file into a Pandas DataFrame
df = pd.read_stata("D:\\Documents\\NCKH\\data\\Readability_BCTC_CEO_Ownership.csv")

# Count the number of observations
count = df.shape[0]
print("Number of observations:", count)

# Drop rows with missing values in the 'so_chu_de' column
df = df.dropna(subset=['so_chu_de'])

# Exclude rows where 'Year' is missing
df_annual_report = df[~df['Year'].isnull()]

# Describe annual report
annual_report_stats = df_annual_report.describe()
print(annual_report_stats)

# Describe TT200
tt200_stats = df[~df['Year'].notnull()].describe()
print(tt200_stats)

# Scaled variables
df['WORD_Easy'] = df['so_tu_de'] / df['so_tu']
# ... repeat for other scaled variables

# Describe annual report scaled
scaled_stats = df_annual_report[['CHAR_Easy', 'CHAR_Dens', 'CHAR_Order', 'WORD_Easy', 'WORD_Borrow', 'WORD_1mean', 'WORD_2mean', 'WORD_3mean', 'WORD_mmean', 'WORD_1pos', 'WORD_2pos', 'WORD_3pos', 'WORD_mpos', 'WORD_totaltype', 'WORD_Dens', 'WORD_Order', 'WORD_Local', 'WORD_Chinese', 'WORD_Chinese1', 'WORD_Chinese2', 'WORD_Chinese3', 'WORD_Chinese_m', 'WORD_1char', 'WORD_2char', 'WORD_3char', 'WORD_mchar', 'SENT_less10', 'SENT_less13']].describe()
print(scaled_stats)

# Correlation
correlation_matrix = df.corr()
print(correlation_matrix)

# Regression
independent_vars = ['wSIZE', 'wROE', 'wROA', 'wROS', 'wLEV', 'wFOR', 'wFOR_Ind', 'wFOR_Org', 'wDOM_Ind', 'wDOM_Org', 'wGOV', 'CHAIR', 'Duality', 'CEO1', 'BSIZE']
dependent_var = 'wCHAR_Easy'
model = sm.OLS(df[dependent_var], sm.add_constant(df[independent_vars])).fit()
print(model.summary())
# ... repeat for other dependent variables

# Winsorize non-scaled variables
non_scaled_vars = ['so_chu_de', 'so_chu_de_phan_biet', 'so_tu_de', 'so_tu_de_phan_biet', 'so_tu_muon', 'so_tu_muon_phan_biet', 'so_tu_co_1_nghia', 'so_tu_co_1_pos', 'so_tu_co_2_nghia', 'so_tu_co_2_pos', 'so_tu_co_3_nghia', 'so_tu_co_3_pos', 'so_tu_co_nhieu_pos', 'so_tu_da_nghia', 'tong_so_tu_loai_cua_tat_ca_cac_t', 'tong_tan_suat_chu', 'tong_tan_suat_chu_phan_biet', 'tong_tan_suat_tu', 'tong_tan_suat_tu_phan_biet', 'tong_thu_hang_chu', 'tong_thu_hang_chu_phan_biet', 'tong_thu_hang_tu', 'tong_thu_hang_tu_phan_biet', 'so_tu_dia_phuong', 'so_tu_dia_phuong_phan_biet', 'so_tu_han_viet', 'so_tu_han_viet_1_chu', 'so_tu_han_viet_2_chu', 'so_tu_han_viet_3_chu', 'so_tu_han_viet_nhieu_chu', 'so_tu_han_viet_phan_biet', 'so_cau', 'so_cau_duoi_10_tu', 'so_cau_duoi_13_chu', 'so_cau_tu_10_tu', 'so_cau_tu_13_chu', 'so_chu', 'so_chu_phan_biet', 'so_ky_tu', 'so_tu', 'so_tu_1_chu', 'so_tu_2_chu', 'so_tu_3_chu', 'so_tu_nhieu_chu', 'so_tu_phan_biet']
df[non_scaled_vars]
s