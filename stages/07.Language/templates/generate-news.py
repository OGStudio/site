#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
AMLEO GenerateNewsExcerpts/Import
AMLEO ListNews/Import
AMLEO NewsItems/Import

DIR = os.path.dirname(__file__)

# FUNCTIONS.

AMLEO GenerateNewsExcerpts/Impl
AMLEO IndexPages/Impl
AMLEO ListNews/Impl
AMLEO NewsByLanguage/Impl
AMLEO NewsExcerptsIndex/Impl
AMLEO NewsExcerptsIndex.Language/Impl
AMLEO NewsItems/Impl
AMLEO NewsItems.Language/Impl
AMLEO PagedPages/Impl
AMLEO PagedPages.Language/Impl
AMLEO SaveIndexPages/Impl
AMLEO SaveNewsItems.Language/Impl
AMLEO SortNewsDescending/Impl

AMLEO pageFileName/Impl

# MAIN EXECUTION SEQUENCE.

AMLEO ListNews/Run
AMLEO NewsByLanguage/Run
    AMLEO SortNewsDescending/Run
    AMLEO GenerateNewsExcerpts/Run
    AMLEO LanguageSuffix/Run
    AMLEO NewsItems.Language/Run
    AMLEO SaveNewsItems.Language/Run
    AMLEO IndexPages.Language/Run
    AMLEO PagedPages.Language/Run
    AMLEO SaveIndexPages/Run
