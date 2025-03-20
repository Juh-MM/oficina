from wordcloud import WordCloud
import matplotlib.pyplot as plt
from docx import Document

def extraindo_texto(docx_path):
    doc = Document(docx_path)
    texto = ''
    for item in doc.paragraphs:
        texto += item.text +  "\n"
    return texto

docx_path = 'nomedodocx.docx'

text = extraindo_texto(docx_path)

workcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(workcloud, interpolation='bilinear')
plt.axis("off")
plt.show()