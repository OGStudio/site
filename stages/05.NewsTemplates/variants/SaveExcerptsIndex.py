AMLEO Run
INDEX_FILE_NAME = "index.html"
with (open(INDEX_FILE_NAME, "w")) as f:
    f.write(INDEX.encode("utf-8"))
