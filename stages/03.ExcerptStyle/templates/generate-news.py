#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
AMLEO GenerateNewsExcerpts/Import
AMLEO ListNews/Import

DIR = os.path.dirname(__file__)

AMLEO ListNews/Impl
AMLEO SortNewsDescending/Impl
AMLEO GenerateNewsExcerpts/Impl
AMLEO ExcerptsContents/Impl
AMLEO ExcerptsDates/Impl
AMLEO ExcerptsTitles/Impl
AMLEO ExcerptsMore/Impl
AMLEO ExcerptsFrames/Impl
AMLEO CombineIndexExcerpts/Impl

AMLEO ListNews/Run
AMLEO SortNewsDescending/Run
AMLEO ListNews/Debug
AMLEO GenerateNewsExcerpts/Run
AMLEO ExcerptsNewsEqualNumber/Run
AMLEO ExcerptsContents/Run
AMLEO ExcerptsDates/Run
AMLEO ExcerptsTitles/Run
AMLEO ExcerptsMore/Run
AMLEO ExcerptsFrames/Run
AMLEO CombineIndexExcerpts/Run
