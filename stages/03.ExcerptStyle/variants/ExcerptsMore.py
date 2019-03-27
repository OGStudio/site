AMLEO Run
NEWS_EXCERPTS = excerptsMore(NEWS_EXCERPTS, NEWS)

AMLEO Impl
def excerptsMore(excerpts, articles):
    items = []

    end = """
</a>
</div>
"""
    for i in range(len(NEWS)):
        excerpt = excerpts[i]
        article = articles[i]

        articlePath = article.baseName + ".html"
        start = """
<div class="news_item_more">
<a href="{0}">
""".format(articlePath)

        item = excerpt + start + "More" + end
        items.append(item)

    return items
