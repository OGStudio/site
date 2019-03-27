AMLEO Run
saveCompleteNews(
    NEWS,
    COMPLETE_NEWS,
    DIR,
    DIR + "/news-header.html",
    DIR + "/news-footer.html"
)

AMLEO Impl
def saveCompleteNews(
    news,
    completeNews,
    dirName,
    headerFileName,
    footerFileName
):
    # Make sure news and complete news contain equal number of items.
    if (len(news) != len(completeNews)):
        raise Exception("saveCompleteNews: number of news and complete news differ")

    # Header.
    headerContents = ""
    with (open(headerFileName, "r")) as f:
        headerContents = f.read()

    # Footer.
    footerContents = ""
    with (open(footerFileName, "r")) as f:
        footerContents = f.read()

    # Save complete news.
    for i in range(len(news)):
        article = news[i]
        complete = completeNews[i]
        content = headerContents + complete + footerContents
        fileName = dirName + "/" + article.baseName + ".html"
        with (open(fileName, "w")) as f:
            f.write(content.encode("utf-8"))
