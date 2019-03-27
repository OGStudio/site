AMLEO Import
import re

AMLEO Run
fixNewsImages(NEWS)

AMLEO Impl
def fixArticleImages(article):
    lines = article.contents.splitlines(True)
    contents = ""

    regexp = re.compile("\[(.+)\]:(.+)")
    for ln in lines:
        result = regexp.match(ln)
        # Leave non-links intact.
        if (result is None):
            contents += ln + "\n"
        # Process links.
        else:
            anchor, link = result.groups()
            slink = link.strip()
            imagePrefix = "{attach}/images/"
            articlePrefix = "{filename}/articles/"
            # Image.
            if (slink.startswith(imagePrefix)):
                slink = slink.replace(imagePrefix, "images/")
            # Article.
            elif (slink.startswith(articlePrefix)):
                slink = slink.replace(articlePrefix, "")
                slink = slink.replace(".md", ".html")

            contents += "[{0}]: {1}\n".format(anchor, slink)

    article.contents = contents

def fixNewsImages(articles):
    for article in articles:
        fixArticleImages(article)
