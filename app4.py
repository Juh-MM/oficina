from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from docx import Document

def extraindo_texto(docx_path):
    doc = Document(docx_path)
    texto = ''
    for itme in doc.paragraphs:
        texto += item.text +  "\n"
    return texto

docx_path = 'nomedodocx.docx'

text = extraindo_texto(docx_path)

stopwords = set(STOPWORDS)
novas_palavras = []
with open ("caminho/do/arquivo", 'r', encoding="utf8") as item:
    [novas_palavras.append(word) for linha in item for word in linha.split()]

new_stopwords = stopwords.union(novas_palavras)

workcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(workcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

