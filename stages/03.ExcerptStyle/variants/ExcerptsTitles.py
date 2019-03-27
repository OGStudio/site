AMLEO Run
NEWS_EXCERPTS = excerptsTitles(NEWS_EXCERPTS, NEWS)

AMLEO Impl
def excerptsTitles(excerpts, articles):
    items = []

    end = """
</a>
</h2>
"""
    for i in range(len(NEWS)):
        excerpt = excerpts[i]
        article = articles[i]

        articlePath = article.baseName + ".html"
        start = """
<h2 class="news_item_title">
<a href="{0}">
""".format(articlePath)

        item = start + article.title + end + excerpt
        items.append(item)

    return items
