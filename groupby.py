import pandas as pd

data = {
        'Kategori': ['gadget', 'gadget', 'aksesori', 'aksesori', 'gadget'],
        'Produk': ['HP', 'laptop', 'charger', 'casing', 'tablet'],
        'Terjual': [10, 5, 25, 40, 8]
}

df = pd.DataFrame(data)

rata_per_kategori = df.groupby('Kategori')['Terjual'].mean()

print(rata_per_kategori)
