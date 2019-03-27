AMLEO Run
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

AMLEO Debug
print("INDEX: '{0}'".format(INDEX.encode("utf-8")))

AMLEO Impl
def newsExcerptIndex(article, excerpt, newsExcerptTemplate):
    contents = newsExcerptTemplate

    contents = contents.replace("NEWS_EXCERPT_TITLE", article.title)
    contents = contents.replace("NEWS_EXCERPT_DATE", article.date)
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
