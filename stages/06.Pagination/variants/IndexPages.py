AMLEO Run
# Make sure excerpts and news contain equal number of items.
if (len(NEWS_EXCERPTS) != len(NEWS)):
    raise Exception("Number of excerpts and news differ")

NEWS_EXCERPT_TEMPLATE_FILE_NAME = "news.excerpt.template.html"
INDEX_TEMPLATE_FILE_NAME = "index.template.html"
EXCERPTS_PER_PAGE = 9

INDEX_PAGES = indexPages(
    NEWS,
    NEWS_EXCERPTS,
    NEWS_EXCERPT_TEMPLATE_FILE_NAME,
    INDEX_TEMPLATE_FILE_NAME,
    EXCERPTS_PER_PAGE
)

AMLEO Impl
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
