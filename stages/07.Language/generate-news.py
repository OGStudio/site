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
def indexPages(
    news,
    excerpts,
    newsExcerptTemplateFileName,
    indexTemplateFileName,
    excerptsPerPage
):
    pages = []

    def page(news, excerpts):
        contents = newsExcerptsIndex(
            news,
            excerpts,
            newsExcerptTemplateFileName,
            indexTemplateFileName
        )
        return contents

    pageArticles = []
    pageExcerpts = []
    for i in range(len(news)):
        article = news[i]
        pageArticles.append(article)
        excerpt = excerpts[i]
        pageExcerpts.append(excerpt)

        # Paginate.
        if (len(pageArticles) == excerptsPerPage):
            pages.append(page(pageArticles, pageExcerpts))
            # Reset.
            pageArticles = []
            pageExcerpts = []

    # Create the last page if there are articles left.
    if (len(pageArticles) > 0):
        pages.append(page(pageArticles, pageExcerpts))

    return pages
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
def newsByLanguage(articles):
    d = { }
    for article in articles:
        # Create language entry with an empty array
        # if the entry does not yet exist.
        if article.lang not in d:
            d[article.lang] = []
        # Add article.
        d[article.lang].append(article)
    return d
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
def newsExcerptIndex(article, excerpt, newsExcerptTemplate):
    contents = newsExcerptTemplate

    contents = contents.replace("NEWS_EXCERPT_TITLE", article.title)
    contents = contents.replace("NEWS_EXCERPT_DATE", article.date)
    excerpt = excerpt.encode("utf-8")
    contents = contents.replace("NEWS_EXCERPT_CONTENTS", excerpt)
    # NOTE LANG_SUFFIX is taken from global space
    # NOTE This is bad, however, that's the only way to update this inner
    # NOTE function without touching other chain parts.
    # TODO All functions should be methods with shared state
    # TODO then it becomes easy to inject newer (unforseen) state
    # TODO into the older functionality parts
    url = "{0}{1}.html".format(article.slug, LANG_SUFFIX)
    contents = contents.replace("NEWS_ITEM_URL", url)
    
    return contents
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
def pagedPages(
    pages,
    paginationTemplateFileName,
    paginationNextTemplateFileName,
    paginationPrevTemplateFileName,
    indexFileNameBase
):
    items = []

    # Read pagination template.
    paginationTemplate = ""
    with (open(paginationTemplateFileName, "r")) as f:
        paginationTemplate = f.read()
    # Read pagination.next template.
    paginationNextTemplate = ""
    with (open(paginationNextTemplateFileName, "r")) as f:
        paginationNextTemplate = f.read()
    # Read pagination.prev template.
    paginationPrevTemplate = ""
    with (open(paginationPrevTemplateFileName, "r")) as f:
        paginationPrevTemplate = f.read()
    # Set pagination section.
    pagesCount = len(pages)
    for i in range(pagesCount):
        page = pages[i]
        prevPageExists = i - 1 >= 0
        nextPageExists = (i + 1 < pagesCount)
        paginationSection = ""
        if (prevPageExists and nextPageExists):
            prevURL = pageFileName(indexFileNameBase, i - 1)
            nextURL = pageFileName(indexFileNameBase, i + 1)
            paginationSection = paginationTemplate
            paginationSection = paginationSection.replace("PREV_PAGE_URL", prevURL)
            paginationSection = paginationSection.replace("NEXT_PAGE_URL", nextURL)
        elif (prevPageExists):
            prevURL = pageFileName(indexFileNameBase, i - 1)
            paginationSection = paginationPrevTemplate
            paginationSection = paginationSection.replace("PREV_PAGE_URL", prevURL)
        elif (nextPageExists):
            nextURL = pageFileName(indexFileNameBase, i + 1)
            paginationSection = paginationNextTemplate
            paginationSection = paginationSection.replace("NEXT_PAGE_URL", nextURL)

        item = page
        item = item.replace("NEWS_PAGINATION", paginationSection)
        item = item.replace("PAGE_ID", str(i + 1))
        item = item.replace("PAGES_COUNT", str(pagesCount))
        items.append(item)

    return items
def pagedPagesWithLangSwitcher(pages, indexFileNameFormat):
    items = []

    id = 0
    for page in pages:
        fileName = pageFileName(indexFileNameFormat, id)
        id += 1

        contents = page
        # English.
        url = fileName.format("")
        contents = contents.replace("LANG_EN", url)
        # Russian.
        url = fileName.format("-ru")
        contents = contents.replace("LANG_RU", url)

        items.append(contents)

    return items
def saveIndexPages(pages, dirName, indexFileNameBase):
    id = 0
    for page in pages:
        fileName = dirName + "/" + pageFileName(indexFileNameBase, id)
        id += 1
        with (open(fileName, "w")) as f:
            f.write(page)
def saveNewsItems(newsItems, news, dirName, langSuffix):
    for i in range(len(news)):
        article = news[i]
        item = newsItems[i]
        fileName = "{0}/{1}{2}.html".format(dirName, article.slug, langSuffix)
        with (open(fileName, "w")) as f:
            f.write(item)
def sortNewsDescending(news):
    # Topic: How do I sort this list in Python, if my date is in a String?
    # Source: https://stackoverflow.com/a/2589662
    ascending = sorted(news, key = lambda x: x.date)
    # Return reversed list.
    return ascending[::-1]

def pageFileName(fileNameBase, id):
    # Do not provide id for the first page.
    sid = id + 1 if id > 0 else ""
    return "{0}{1}.html".format(fileNameBase, sid)

# MAIN EXECUTION SEQUENCE.

NEWS = articles(DIR + "/news")
LANG_NEWS = newsByLanguage(NEWS)
for lang in LANG_NEWS:
    print("\nLanguage: '{0}'".format(lang))
    NEWS = LANG_NEWS[lang]
    NEWS = sortNewsDescending(NEWS)
    NEWS_EXCERPTS = newsExcerpts(NEWS)
    LANG_SUFFIX = ""
    if (lang != "en"):
        LANG_SUFFIX = "-{0}".format(lang)
    NEWS_ITEM_TEMPLATE_FILE_NAME = "news.item.template{0}.html".format(LANG_SUFFIX)
    NEWS_ITEMS = newsItems(NEWS, NEWS_ITEM_TEMPLATE_FILE_NAME)
    NEWS_ITEMS = newsItemsWithLangSwitcher(NEWS, NEWS_ITEMS)
    saveNewsItems(NEWS_ITEMS, NEWS, DIR, LANG_SUFFIX)
    # Make sure excerpts and news contain equal number of items.
    if (len(NEWS_EXCERPTS) != len(NEWS)):
        raise Exception("Number of excerpts and news differ")
    
    NEWS_EXCERPT_TEMPLATE_FILE_NAME = "news.excerpt.template{0}.html".format(LANG_SUFFIX)
    INDEX_TEMPLATE_FILE_NAME = "index.template{0}.html".format(LANG_SUFFIX)
    EXCERPTS_PER_PAGE = 9
    
    INDEX_PAGES = indexPages(
        NEWS,
        NEWS_EXCERPTS,
        NEWS_EXCERPT_TEMPLATE_FILE_NAME,
        INDEX_TEMPLATE_FILE_NAME,
        EXCERPTS_PER_PAGE
    )
    INDEX_FILE_NAME_FORMAT = "index{0}"
    INDEX_FILE_NAME_BASE = INDEX_FILE_NAME_FORMAT.format(LANG_SUFFIX)
    PAGINATION_TEMPLATE_FILE_NAME = "news.pagination.template{0}.html".format(LANG_SUFFIX)
    PAGINATION_NEXT_TEMPLATE_FILE_NAME = "news.pagination.next.template{0}.html".format(LANG_SUFFIX)
    PAGINATION_PREV_TEMPLATE_FILE_NAME = "news.pagination.prev.template{0}.html".format(LANG_SUFFIX)
    INDEX_PAGES = pagedPages(
        INDEX_PAGES,
        PAGINATION_TEMPLATE_FILE_NAME,
        PAGINATION_NEXT_TEMPLATE_FILE_NAME,
        PAGINATION_PREV_TEMPLATE_FILE_NAME,
        INDEX_FILE_NAME_BASE
    )
    INDEX_PAGES = pagedPagesWithLangSwitcher(INDEX_PAGES, INDEX_FILE_NAME_FORMAT)
    saveIndexPages(INDEX_PAGES, DIR, INDEX_FILE_NAME_BASE)
