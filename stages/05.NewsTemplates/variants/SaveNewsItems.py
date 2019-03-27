AMLEO Run
# Make sure news items and news contain equal number of items.
if (len(NEWS_ITEMS) != len(NEWS)):
    raise Exception("Number of news items and news differ")
saveNewsItems(NEWS_ITEMS, NEWS, DIR)

AMLEO Impl
def saveNewsItems(newsItems, news, dirName):
    for i in range(len(news)):
        article = news[i]
        item = newsItems[i]
        fileName = "{0}/{1}.html".format(dirName, article.baseName)
        with (open(fileName, "w")) as f:
            f.write(item.encode("utf-8"))
