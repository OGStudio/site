AMLEO Run
LANG_NEWS = newsByLanguage(NEWS)
for lang in LANG_NEWS:
    print("\nLanguage: '{0}'".format(lang))
    NEWS = LANG_NEWS[lang]

AMLEO Debug
for item in NEWS:
    print(str(item))

AMLEO Impl
def newsByLanguage(articles):
    d = { }
    for article in articles:
        # Create language entry with an empty array
        # if the entry does not yet exist.
        if article.lang not in d:
            d[article.lang] = []
        # Add article.
        d[article.lang].append(article)
    return d
