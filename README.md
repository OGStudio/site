# Overview

This is a static Opensource Game Studio site generator created with AMLEO.

This was the first attempt to verify AMLEO can serve as a tool to create
a small system to manage static site content. AMLEO performed very well.

However, since this was the first attempt the approach to AMLEO usage taken
is now seen as suboptimal. That's why this repository is now obsolete
and only kept for historical reasons.

# Site generation prerequisites

* AMLEO
* Pandoc
* pypandoc Python module

    ```pip install pypandoc```

# Site generation

* Place news in markdown format into news/
* Run `generate-news.py` to generate html files and index files

# Restrictions

* Pages (from markdown) are not yet supported
