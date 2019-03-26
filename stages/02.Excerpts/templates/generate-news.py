#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
AMLEO GenerateNewsExcerpts/Import
AMLEO ListNews/Import

DIR = os.path.dirname(__file__)

AMLEO ListNews/Impl
AMLEO SortNewsDescending/Impl
AMLEO GenerateNewsExcerpts/Impl
AMLEO SaveExcerpts/Impl

AMLEO ListNews/Run
AMLEO SortNewsDescending/Run
AMLEO ListNews/Debug
AMLEO GenerateNewsExcerpts/Run
AMLEO GenerateNewsExcerpts/Debug
AMLEO SaveExcerpts/Run
