import newspaper
from newspaper import Article
import requests
from newsapi import NewsApiClient
import fastText
import re
from nltk.corpus import stopwords
import pandas as pd

# newsapi_key = 
api = NewsApiClient(api_key=newsapi_key)

def get_articles(query, 
                 sources='bloomberg,cnbc,the-economist,the-wall-street-journal,financial-times',
                 from_date = None,
                 to_date = None,
                 sort_by = 'popularity'):
    result = []
    response = api.get_everything(q = query, sources = sources, from_parameter=from_date, 
                                      to = to_date, sort_by = sort_by)
    # print(response['totalResults'])
    for a in response['articles']:
            article = Article(a['url'])
            article.download()
            article.parse()
            # article.nlp()
            # print(article.text)
            result.append(clean(article.text, stop=False))
    return result

def clean(text, stop=True):
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    if stop:
        for w in stopwords.words('english'):
            text.replace("w", "")
    return text

def compute_sentiment(texts, model):
    senti = []
    for t in texts:
        score = model.predict(t)
        senti.append(score)
    return senti

def translate_label(label, type='full'):
    if type == 'full':
        key = {'__label__1' : -2, 
               '__label__2' : -1,
               '__label__3' : 0,
               '__label__4' : 1,
               '__label__5' : 2}

    elif type == 'polarity':
        key = {'__label__1': -1, 
               '__label__2': 1}

    return key[label]

def avg_sentiment(q, type='full', 
                  sources='bloomberg,cnbc,the-economist,the-wall-street-journal,financial-times',
                  from_date=None, to_date=None,
                  sort_by = 'popularity'):
    model = fastText.load_model("amazon_review_"+type+".ftz")
    articles = get_articles(q,sources,from_date,to_date,sort_by)
    sentiment = compute_sentiment(articles, model)
    df = pd.DataFrame({'articles': articles, 'sentiment': sentiment})
    avg = 0
    for s in sentiment:
        avg += translate_label(s[0][0], type=type)

    # avg = 1.0*(avg / len(sentiment))
    print(df)
    print(avg)
    return avg, df


