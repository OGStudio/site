#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
import pypandoc
import re
import glob
import pypandoc

DIR = os.path.dirname(__file__)

# FUNCTIONS.

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
def newsExcerptIndex(article, excerpt, newsExcerptTemplate):
    contents = newsExcerptTemplate

    contents = contents.replace("NEWS_EXCERPT_TITLE", article.title)
    contents = contents.replace("NEWS_EXCERPT_DATE", article.date)
    excerpt = excerpt.encode("utf-8")
    contents = contents.replace("NEWS_EXCERPT_CONTENTS", excerpt)
    url = article.baseName + ".html"
    contents = contents.replace("NEWS_ITEM_URL", url)
    
    return contents

def newsExcerptsIndex(
    news,
    excerpts,
    newsExcerptTemplateFileName,
    indexTemplateFileName
):
    contents = ""

    # Read news excerpt template.
    newsExcerptTemplate = ""
    with (open(newsExcerptTemplateFileName, "r")) as f:
        newsExcerptTemplate = f.read()
    # Compose news excerpts.
    excerptsContents = ""
    for i in range(len(news)):
        article = news[i]
        excerpt = excerpts[i]
        excerptsContents += newsExcerptIndex(article, excerpt, newsExcerptTemplate)
    # Read index template.
    indexTemplate = ""
    with (open(indexTemplateFileName, "r")) as f:
        indexTemplate = f.read()

    return indexTemplate.replace("NEWS_EXCERPTS", excerptsContents)
def newsItem(article, newsItemTemplate):
    contents = newsItemTemplate

    contents = contents.replace("NEWS_ITEM_TITLE", article.title)
    contents = contents.replace("NEWS_ITEM_DATE", article.date)
    html = pypandoc.convert_text(article.contents, "html", format = "md")
    html = html.encode("utf-8")
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
def saveNewsItems(newsItems, news, dirName):
    for i in range(len(news)):
        article = news[i]
        item = newsItems[i]
        fileName = "{0}/{1}.html".format(dirName, article.baseName)
        with (open(fileName, "w")) as f:
            f.write(item)
def sortNewsDescending(news):
    # Topic: How do I sort this list in Python, if my date is in a String?
    # Source: https://stackoverflow.com/a/2589662
    ascending = sorted(news, key = lambda x: x.date)
    # Return reversed list.
    return ascending[::-1]

# MAIN EXECUTION SEQUENCE.

NEWS = articles(DIR + "/news")
NEWS = sortNewsDescending(NEWS)
print("NEWS:")
for item in NEWS:
    print(str(item))
NEWS_EXCERPTS = newsExcerpts(NEWS)
# Make sure excerpts and news contain equal number of items.
if (len(NEWS_EXCERPTS) != len(NEWS)):
    raise Exception("Number of excerpts and news differ")
NEWS_EXCERPT_TEMPLATE_FILE_NAME = "news.excerpt.template.html"
INDEX_TEMPLATE_FILE_NAME = "index.template.html"
INDEX = newsExcerptsIndex(
    NEWS,
    NEWS_EXCERPTS,
    NEWS_EXCERPT_TEMPLATE_FILE_NAME,
    INDEX_TEMPLATE_FILE_NAME
)
INDEX_FILE_NAME = "index.html"
with (open(INDEX_FILE_NAME, "w")) as f:
    f.write(INDEX.encode("utf-8"))
NEWS_ITEM_TEMPLATE_FILE_NAME = "news.item.template.html"
NEWS_ITEMS = newsItems(NEWS, NEWS_ITEM_TEMPLATE_FILE_NAME)
saveNewsItems(NEWS_ITEMS, NEWS, DIR)
