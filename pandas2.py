import pandas as pd

data = {
        'Produk': ['laptop', 'mouse', 'keyboard', 'monitor', 'headset'],
        'Harga': [10000000, 150000, 300000, 2000000, 450000],
        'Terjual': [5, 50, 25, 10, 15]
}

df = pd.DataFrame(data)

df['Total_pendapatan'] = df['Harga'] * df['Terjual']

df_filtered = df[df['Total_pendapatan'] > 5000000]

print(df_filtered)
