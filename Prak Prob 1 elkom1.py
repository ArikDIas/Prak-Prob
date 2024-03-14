import pandas as pd
# Membuat dataframe dari data yang disalin ke clipboard
df = pd.read_clipboard()
print(df)

#untuk menghitung rata-rata tinggi badan
rata_tinggi = df["tinggi badan"].mean() 
print(rata_tinggi)

#untuk merubah tipe data dari integer ke string
df["angkatan"] = df["angkatan"].astype(str) 
print(df.dtypes)