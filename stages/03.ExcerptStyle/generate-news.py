#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
import pypandoc
import re
import glob

DIR = os.path.dirname(__file__)

class Article(object):
    def __init__(self, fileName):
        self.fileName = fileName
        (name, ext) = os.path.splitext(os.path.basename(fileName))
        self.baseName = name
        self.title = None
        self.date = None
        self.category = None
        self.slug = None
        self.lang = None
        self.contents = ""
    def __str__(self):
        return (
            "Article( " +
            "fileName: '{0}' ".format(self.fileName) +
            "baseName: '{0}' ".format(self.baseName) +
            "title: '{0}' ".format(self.title) +
            "date: '{0}' ".format(self.date) +
            "category: '{0}' ".format(self.category) +
            "slug: '{0}' ".format(self.slug) +
            "lang: '{0}' ".format(self.lang) +
            ") contents length: '{0}'".format(len(self.contents))
        )

def parseArticle(article):
    with (open(article.fileName, "r")) as f:
        lines = f.read().splitlines()
        for ln in lines:
            # Technical information.
            if (ln.startswith("Title:")):
                article.title = ln.replace("Title:", "").strip()
            elif (ln.startswith("Date:")):
                article.date = ln.replace("Date:", "").strip()
            elif (ln.startswith("Category:")):
                article.category = ln.replace("Category:", "").strip()
            elif (ln.startswith("Slug:")):
                article.slug = ln.replace("Slug:", "").strip()
            elif (ln.startswith("Lang:")):
                article.lang = ln.replace("Lang:", "").strip()
            # Contents.
            else:
                article.contents += ln + "\n"

def articles(dirName):
    items = []

    fileNames = glob.glob(dirName + "/*.md")
    for fileName in fileNames:
        article = Article(fileName)
        parseArticle(article)
        items.append(article)

    return items
def sortNewsDescending(news):
    # Topic: How do I sort this list in Python, if my date is in a String?
    # Source: https://stackoverflow.com/a/2589662
    ascending = sorted(news, key = lambda x: x.date)
    # Return reversed list.
    return ascending[::-1]
def newsExcerpt(article):
    # 1. Get first lines from markdown content that almost fit 400 characters.
    # 2. Append `...` at the end to signify `more`
    # 3. Append links section of markdown content
    # 4. Convert resulting content to HTML, this is an excerpt
    charsLimit = 250
    lines = article.contents.splitlines(True)
    # Compose excerpt section.
    excerpt = ""
    for ln in lines:
        excerpt += ln
        if (len(excerpt) >= charsLimit):
            break
    excerpt += "..."
    # Compose links section.
    links = ""
    for ln in lines:
        if re.match("\[.+\]:.+", ln):
            links += ln

    content = excerpt + "\n\n\n" + links
    html = pypandoc.convert_text(content, "html", format = "md")
    return html

def newsExcerpts(articles):
    items = []
    for article in articles:
        items.append(newsExcerpt(article))
    return items
def excerptsContents(excerpts):
    items = []

    start = """
<div class="news_item_contents">
"""
    end = """
</div>
"""
    for excerpt in excerpts:
        items.append(start + excerpt + end)

    return items
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
def excerptsFrames(items):
    updatedItems = []

    start = "<div class=\"news_item\">\n"
    end = "\n</div>"
    for item in items:
        updatedItems.append(start + item + end)

    return updatedItems
def combineIndexExcerpts(
    items,
    headerFileName,
    footerFileName,
    resultFileName
):
    # Header.
    headerContents = ""
    with (open(headerFileName, "r")) as f:
        headerContents = f.read()

    # Footer.
    footerContents = ""
    with (open(footerFileName, "r")) as f:
        footerContents = f.read()

    # Excerpts.
    excerptsContents = "\n".join(items)

    # Save combination.
    combination = headerContents + excerptsContents + footerContents
    with (open(resultFileName, "w")) as f:
        f.write(combination.encode("utf-8"))

NEWS = articles(DIR + "/news")
NEWS = sortNewsDescending(NEWS)
print("NEWS:")
for item in NEWS:
    print(str(item))
NEWS_EXCERPTS = newsExcerpts(NEWS)
# Make sure excerpts and news contain equal number of items.
if (len(NEWS_EXCERPTS) != len(NEWS)):
    raise Exception("Number of excerpts and news differ")
NEWS_EXCERPTS = excerptsContents(NEWS_EXCERPTS)
NEWS_EXCERPTS = excerptsDates(NEWS_EXCERPTS, NEWS)
NEWS_EXCERPTS = excerptsTitles(NEWS_EXCERPTS, NEWS)
NEWS_EXCERPTS = excerptsMore(NEWS_EXCERPTS, NEWS)
NEWS_EXCERPTS = excerptsFrames(NEWS_EXCERPTS)
combineIndexExcerpts(
    NEWS_EXCERPTS,
    DIR + "/index-header.html",
    DIR + "/index-footer.html",
    DIR + "/index.html"
)
