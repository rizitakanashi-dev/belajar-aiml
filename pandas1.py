import pandas as pd

data = {
        'Nama': ['budi', 'siti', 'joko'],
        'Matematika': [80, 90, 60],
        'Bahasa Inggris': [85, 75, 95]
}

df = pd.DataFrame(data)

df['Lulus'] = df['Matematika'] >= 75

print(df)
