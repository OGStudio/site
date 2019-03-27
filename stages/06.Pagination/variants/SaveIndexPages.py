AMLEO Run
saveIndexPages(INDEX_PAGES, DIR, INDEX_FILE_NAME_BASE)

AMLEO Impl
def saveIndexPages(pages, dirName, indexFileNameBase):
    id = 0
    for page in pages:
        fileName = dirName + "/" + pageFileName(indexFileNameBase, id)
        id += 1
        with (open(fileName, "w")) as f:
            f.write(page)
