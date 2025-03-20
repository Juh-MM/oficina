import matplotlib.pyplot as plt

categorias = ["alimentação", "educação", "transporte", "lazer"]
valores = [500, 700, 300, 400]

plt.figure(figsize=(7,7))
plt.pie(valores, labels=categorias, autopct="%1.1f%%", colors=["gold","pink","red","green"])
plt.title("Gastos mensais")
plt.show()