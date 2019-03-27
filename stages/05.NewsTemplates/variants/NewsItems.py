AMLEO Import
import pypandoc

AMLEO Run
NEWS_ITEM_TEMPLATE_FILE_NAME = "news.item.template.html"
NEWS_ITEMS = newsItems(NEWS, NEWS_ITEM_TEMPLATE_FILE_NAME)

AMLEO Debug
for item in NEWS_ITEMS:
    print(item.encode("utf-8"))

AMLEO Impl
def newsItem(article, newsItemTemplate):
    contents = newsItemTemplate

    contents = contents.replace("NEWS_ITEM_TITLE", article.title)
    contents = contents.replace("NEWS_ITEM_DATE", article.date)
    html = pypandoc.convert_text(article.contents, "html", format = "md")
    contents = contents.replace("NEWS_ITEM_CONTENTS", html)
    url = article.baseName + ".html"
    contents = contents.replace("NEWS_ITEM_URL", url)
    
    return contents

def newsItems(news, newsItemTemplateFileName):
    items = []

    # Read news item template.
    newsItemTemplate = ""
    with (open(newsItemTemplateFileName, "r")) as f:
        newsItemTemplate = f.read()
    # Compose news items.
    for i in range(len(news)):
        article = news[i]
        items.append(newsItem(article, newsItemTemplate))

    return items
