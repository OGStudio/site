AMLEO Run
combineIndexExcerpts(
    NEWS_EXCERPTS,
    DIR + "/index-header.html",
    DIR + "/index-footer.html",
    DIR + "/index.html"
)

AMLEO Impl
def combineIndexExcerpts(
    items,
    headerFileName,
    footerFileName,
    resultFileName
):
    # Header.
    headerContents = ""
    with (open(headerFileName, "r")) as f:
        headerContents = f.read()

    # Footer.
    footerContents = ""
    with (open(footerFileName, "r")) as f:
        footerContents = f.read()

    # Excerpts.
    excerptsContents = "\n".join(items)

    # Save combination.
    combination = headerContents + excerptsContents + footerContents
    with (open(resultFileName, "w")) as f:
        f.write(combination.encode("utf-8"))
