import feedparser
import pandas as pd
from IPython.display import display
from datetime import date

liste_rss = ["https://www.lemonde.fr/rss/en_continu.xml", "https://www.courrierinternational.com/feed/category/6260/rss.xml"
            ,"https://www.bfmtv.com/rss/news-24-7/", "https://partner-feeds.20min.ch/rss/20minutes", "https://www.marianne.net/rss.xml"
            , "https://www.lavoixdunord.fr/destinations/2/cible_principale/rss"
            ]
len_rss = len(liste_rss)
cpt = 0
elem = {}
df = pd.DataFrame(elem, columns=['title', 'pubDate', 'link'])
while (cpt < len_rss):
    f = feedparser.parse(liste_rss[cpt])
    cpt = cpt + 1
    x = 0
    while (x < len(f.entries)):
        data0 = f.entries[x].link
        data = f.entries[x].title
        elem["title"] = data
        data2 = f.entries[x].published
        elem["pubdate"] = data2
        df = df.append({"title" : data, "pubDate" : data2, "link": data0}, ignore_index=True)
        x = x + 1

#display(df)
today = date.today()
d1 = today.strftime("%d/%m/%Y")
df.to_csv('./octonews.csv', index=False)
