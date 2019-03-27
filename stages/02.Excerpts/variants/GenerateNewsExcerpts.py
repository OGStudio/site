AMLEO Import
import pypandoc
import re

AMLEO Run
NEWS_EXCERPTS = newsExcerpts(NEWS)

AMLEO Debug
print("NEWS_EXCERPTS:")
for item in NEWS_EXCERPTS:
    print(item.encode("utf-8"))

AMLEO Impl
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
