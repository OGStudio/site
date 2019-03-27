#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
AMLEO GenerateNewsExcerpts/Import
AMLEO ListNews/Import
AMLEO NewsItems/Import

DIR = os.path.dirname(__file__)

# FUNCTIONS.

AMLEO GenerateNewsExcerpts/Impl
AMLEO ListNews/Impl
AMLEO NewsExcerptsIndex/Impl
AMLEO NewsItems/Impl
AMLEO SaveNewsItems/Impl
AMLEO SortNewsDescending/Impl

# MAIN EXECUTION SEQUENCE.

AMLEO ListNews/Run
AMLEO SortNewsDescending/Run
AMLEO ListNews/Debug
AMLEO GenerateNewsExcerpts/Run
AMLEO NewsExcerptsIndex/Run
AMLEO SaveExcerptsIndex/Run
AMLEO NewsItems/Run
AMLEO SaveNewsItems/Run
