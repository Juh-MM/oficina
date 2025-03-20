import pandas as pd
import matplotlib.pyplot as plt 
arquivo_exel = "nomearquivo.xlsx"
df = pd.read_excel(arquivo_exel, sheet_name="Planilha")

x = df['ano']
y = df['vendas']

plt.figure(figsize=(8,5))
plt.plot(x, y, marker="o", linestyle="-", color="pink", label="Vendas")
plt.xlabel("Ano")
plt.ylabel("Vendas")
plt.title("Vendas por ano")
plt.legend()
plt.grid(True)

plt.show()