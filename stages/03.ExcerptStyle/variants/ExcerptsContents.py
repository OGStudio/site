AMLEO Run
NEWS_EXCERPTS = excerptsContents(NEWS_EXCERPTS)

AMLEO Impl
def excerptsContents(excerpts):
    items = []

    start = """
<div class="news_item_contents">
"""
    end = """
</div>
"""
    for excerpt in excerpts:
        items.append(start + excerpt + end)

    return items
