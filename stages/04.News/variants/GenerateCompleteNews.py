AMLEO Import
import markdown2
import re

AMLEO Run
COMPLETE_NEWS = completeNews(NEWS)

AMLEO Impl
def singleCompleteNews(article):
    contents = ""

    # Title.
    articlePath = article.baseName + ".html"
    start = """
<h2 class="news_item_title">
<a href="{0}">
""".format(articlePath)
    end = """
</a>
</h2>
"""
    contents += start + article.title + end

    # Date.
    start = "\n<p class=\"news_item_date\">\n"
    end = "\n</p>\n"
    contents += start + article.date + end

    # Article.
    start = """
<div class="news_item_contents">
"""
    end = """
</div>
"""
    #html = pypandoc.convert_text(article.contents, "html", format = "md")
    html = markdown2.markdown(article.contents)
    contents += start + html + end

    return contents

def completeNews(articles):
    items = []
    for article in articles:
        items.append(singleCompleteNews(article))
    return items
