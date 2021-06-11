import feedparser
import pandas as pd
from IPython.display import display
from datetime import date

#elem = get_feed("https://www.lemonde.fr/rss/en_continu.xml")
liste_rss = ["https://www.lemonde.fr/rss/en_continu.xml", "https://www.courrierinternational.com/feed/category/6260/rss.xml"
            ,"https://www.bfmtv.com/rss/news-24-7/", "https://partner-feeds.20min.ch/rss/20minutes", "https://www.marianne.net/rss.xml"
            , "https://www.lavoixdunord.fr/destinations/2/cible_principale/rss"
            ]
len_rss = len(liste_rss)
#print(len_rss)
#exit(0)
cpt = 0
elem = {}
df = pd.DataFrame(elem, columns=['title', 'pubDate', 'link'])
while (cpt < len_rss):
    f = feedparser.parse(liste_rss[cpt])
    cpt = cpt + 1
    #monde https://www.lemonde.fr/rss/en_continu.xml
    x = 0
    #elem = []
    #print(df)
    while (x < len(f.entries)):
        #print (len(f.entries))
        data0 = f.entries[x].link
        #print(data0)
        data = f.entries[x].title
        elem["title"] = data
        #elem.append(data)
        data2 = f.entries[x].published
        elem["pubdate"] = data2
        #data3 = f.title
        #print(data3)
        df = df.append({"title" : data, "pubDate" : data2, "link": data0}, ignore_index=True)
        x = x + 1
        #display(df)

#df = pd.DataFrame(elem, columns=['titre'])
#print(df)
display(df)
today = date.today()
d1 = today.strftime("%d/%m/%Y")
df.to_csv('./octonews.csv', index=False)
