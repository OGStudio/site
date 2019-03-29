AMLEO Run
saveNewsItems(NEWS_ITEMS, NEWS, DIR, LANG_SUFFIX)

AMLEO Impl
def saveNewsItems(newsItems, news, dirName, langSuffix):
    for i in range(len(news)):
        article = news[i]
        item = newsItems[i]
        fileName = "{0}/{1}{2}.html".format(dirName, article.slug, langSuffix)
        with (open(fileName, "w")) as f:
            f.write(item)
