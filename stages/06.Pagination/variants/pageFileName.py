AMLEO Impl
def pageFileName(fileNameBase, id):
    # Do not provide id for the first page.
    sid = id + 1 if id > 0 else ""
    return "{0}{1}.html".format(fileNameBase, sid)
