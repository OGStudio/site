AMLEO Run
saveExcerpts(NEWS_EXCERPTS, DIR + "/news.html")

AMLEO Impl
def saveExcerpts(items, fileName):
    content = ""
    start = "<div class=\"menu_item\">"
    end = "</div>"
    for item in items:
        content += start + item + end
    with (open(fileName, "w")) as f:
        f.write(content.encode("utf-8"))
