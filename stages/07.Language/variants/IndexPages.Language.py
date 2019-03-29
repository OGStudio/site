AMLEO Run
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
