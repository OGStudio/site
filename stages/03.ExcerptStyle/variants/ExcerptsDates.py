AMLEO Run
NEWS_EXCERPTS = excerptsDates(NEWS_EXCERPTS, NEWS)

AMLEO Impl
def excerptsDates(excerpts, articles):
    items = []

    start = "\n<p class=\"news_item_date\">\n"
    end = "\n</p>\n"
    for i in range(len(NEWS)):
        excerpt = excerpts[i]
        article = articles[i]
        item = start + article.date + end + excerpt
        items.append(item)

    return items
