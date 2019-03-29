AMLEO Run
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

AMLEO Impl
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
