AMLEO Run
INDEX_FILE_NAME_BASE = "index"
PAGINATION_TEMPLATE_FILE_NAME = "news.pagination.template.html"
PAGINATION_NEXT_TEMPLATE_FILE_NAME = "news.pagination.next.template.html"
PAGINATION_PREV_TEMPLATE_FILE_NAME = "news.pagination.prev.template.html"
INDEX_PAGES = pagedPages(
    INDEX_PAGES,
    PAGINATION_TEMPLATE_FILE_NAME,
    PAGINATION_NEXT_TEMPLATE_FILE_NAME,
    PAGINATION_PREV_TEMPLATE_FILE_NAME,
    INDEX_FILE_NAME_BASE
)

AMLEO Impl
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

        item = page.encode("utf-8")
        item = item.replace("NEWS_PAGINATION", paginationSection)
        item = item.replace("PAGE_ID", str(i + 1))
        item = item.replace("PAGES_COUNT", str(pagesCount))
        items.append(item)

    return items
