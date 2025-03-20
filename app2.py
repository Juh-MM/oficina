#palavras que mais apareceram 
#nao funciona no codespace

from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = "lorem ipslum. python sei la oq python eu gosto e e e e e e e ela ele de salava azul azul azul azul azul azul azul elas elas elas elas elas elas elas elas elas elas elas"

nuvem = WordCloud(width=800, height=400, background_color='white').generate(texto)

plt.figure(figsize=(10, 5))

plt.imshow(nuvem, interpolation='bilinear')

plt.axis("off")

plt.show()

