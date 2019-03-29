AMLEO Run
NEWS_ITEM_TEMPLATE_FILE_NAME = "news.item.template{0}.html".format(LANG_SUFFIX)
NEWS_ITEMS = newsItems(NEWS, NEWS_ITEM_TEMPLATE_FILE_NAME)
NEWS_ITEMS = newsItemsWithLangSwitcher(NEWS, NEWS_ITEMS)

AMLEO Impl
def newsItemsWithLangSwitcher(articles, newsItems):
    items = []

    for i in range(len(articles)):
        article = articles[i]
        newsItem = newsItems[i]

        contents = newsItem
        # English.
        url = "{0}.html".format(article.slug)
        contents = contents.replace("LANG_EN", url)
        # Russian.
        url = "{0}-ru.html".format(article.slug)
        contents = contents.replace("LANG_RU", url)

        items.append(contents)

    return items
