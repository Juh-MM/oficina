from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

texto = """Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, how do you feel being a girl? (Girl, girl, girl)
Girl, how do you feel being a girl, girl? (Girl, girl)
Man, I don't know, I'm just a girl (girl, girl, girl, girl)
Yeah, I don't know if you like me
Sometimes I think you might hate me
Sometimes I think I might hate you
Maybe you just wanna be me
You always say, "Let's go out"
So we go eat at a restaurant
Sometimes it feels a bit awkward
'Cause we don't have much in common
People say we're alike
They say we've got the same hair
We talk about making music
But I don't know if it's honest
Can't tell if you wanna see me
Falling over and failing
And you can't tell what you're feeling
I think I know how you feel
Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, how do you feel being a girl? (Girl, girl, girl, girl)
Girl, how do you feel being a girl? (Girl, girl)
Man, I don't know, I'm just a girl (girl, girl, girl, girl)
You're all about writing poems
But I'm about throwing parties
Think you should come to my party
And put your hands up
I think we're totally different
But opposites do attract
Maybe we're so meant to be
Just you and me
'Cause people say we're alike
They say we've got the same hair
One day we might make some music
The internet would go crazy
But you might still wanna see me
Falling over and failing
At least we're closer to being on the same page
Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, it's so confusing sometimes to be a girl (girl, girl, girl, girl)
Girl, how do you feel being a girl? (Girl, girl, girl, girl)
Girl, how do you feel being a girl? (Girl, girl)
Man, I don't know, I'm just a girl (girl, girl, girl, girl)"""

palavras = texto.lower().replace(",", "").replace(".", "").split()
contagem = Counter(palavras)

palavras_mais_comuns = contagem.most_common(10)
palavras, frequencias = zip(*palavras_mais_comuns)

plt.figure(figsize=(10, 5))
plt.bar(palavras, frequencias, color='pink')
plt.title("frequencia das palavras mais comuns", fontsize=16)
plt.xlabel("palavras", fontsize=12)
plt.ylabel("frequencia", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()