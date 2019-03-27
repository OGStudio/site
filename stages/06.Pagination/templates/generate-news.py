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
AMLEO NewsExcerptsIndex/Impl
AMLEO NewsItems/Impl
AMLEO PagedPages/Impl
AMLEO SaveIndexPages/Impl
AMLEO SaveNewsItems/Impl
AMLEO SortNewsDescending/Impl

AMLEO pageFileName/Impl

# MAIN EXECUTION SEQUENCE.

AMLEO ListNews/Run
AMLEO SortNewsDescending/Run
AMLEO GenerateNewsExcerpts/Run
AMLEO NewsItems/Run
AMLEO SaveNewsItems/Run
AMLEO IndexPages/Run
AMLEO PagedPages/Run
AMLEO SaveIndexPages/Run
