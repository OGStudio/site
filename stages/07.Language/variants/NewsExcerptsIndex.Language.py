AMLEO Impl
def newsExcerptIndex(article, excerpt, newsExcerptTemplate):
    contents = newsExcerptTemplate

    contents = contents.replace("NEWS_EXCERPT_TITLE", article.title)
    contents = contents.replace("NEWS_EXCERPT_DATE", article.date)
    excerpt = excerpt.encode("utf-8")
    contents = contents.replace("NEWS_EXCERPT_CONTENTS", excerpt)
    # NOTE LANG_SUFFIX is taken from global space
    # NOTE This is bad, however, that's the only way to update this inner
    # NOTE function without touching other chain parts.
    # TODO All functions should be methods with shared state
    # TODO then it becomes easy to inject newer (unforseen) state
    # TODO into the older functionality parts
    url = "{0}{1}.html".format(article.slug, LANG_SUFFIX)
    contents = contents.replace("NEWS_ITEM_URL", url)
    
    return contents
