import pandas as pd

df = pd.read_excel(r'C:\Users\25162\Desktop\工学院附件工参.xlsx')
print(df)

df.to_csv(r'C:\Users\25162\Desktop\工学院附件工参csv版本.csv', encoding='utf_8_sig', index=None)