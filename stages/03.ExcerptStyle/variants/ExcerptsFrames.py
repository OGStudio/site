AMLEO Run
NEWS_EXCERPTS = excerptsFrames(NEWS_EXCERPTS)

AMLEO Impl
def excerptsFrames(items):
    updatedItems = []

    start = "<div class=\"news_item\">\n"
    end = "\n</div>"
    for item in items:
        updatedItems.append(start + item + end)

    return updatedItems
