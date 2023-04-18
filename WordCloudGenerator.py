import spacy
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
nlp = spacy.load("en_core_web_sm")
def word_cloud_generator(text):
    doc = nlp(text)
    
    processed_txt=[token.text for token in doc if not token.is_stop and not token.is_punct] 
    processed_text= " ".join(processed_txt)
    
    l = processed_text.split(" ")
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    words={i:l.count(i)for i in a}
    
    sorted_dict = dict(sorted(words.items(), key=lambda x:x[1],reverse=True))
    x=dict(list(sorted_dict.items())[0:30])
    
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate_from_frequencies(x)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
 
    plt.show()
