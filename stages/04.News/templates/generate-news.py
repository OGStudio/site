#!/usr/bin/python
# This script generates articles from markdown files located in news/ directory.

import os
AMLEO FixNewsLinks/Import
AMLEO GenerateCompleteNews/Import
AMLEO GenerateNewsExcerpts/Import
AMLEO ListNews/Import

DIR = os.path.dirname(__file__)

# FUNCTIONS.

AMLEO ListNews/Impl
AMLEO SortNewsDescending/Impl
AMLEO GenerateNewsExcerpts/Impl
AMLEO ExcerptsContents/Impl
AMLEO ExcerptsDates/Impl
AMLEO ExcerptsTitles/Impl
AMLEO ExcerptsMore/Impl
AMLEO ExcerptsFrames/Impl
AMLEO CombineIndexExcerpts/Impl
AMLEO GenerateCompleteNews/Impl
AMLEO SaveCompleteNews/Impl
AMLEO FixNewsLinks/Impl

# MAIN EXECUTION SEQUENCE.

AMLEO ListNews/Run
AMLEO SortNewsDescending/Run
AMLEO FixNewsLinks/Run
AMLEO ListNews/Debug
AMLEO GenerateNewsExcerpts/Run
AMLEO ExcerptsNewsEqualNumber/Run
AMLEO ExcerptsContents/Run
AMLEO ExcerptsDates/Run
AMLEO ExcerptsTitles/Run
AMLEO ExcerptsMore/Run
AMLEO ExcerptsFrames/Run
AMLEO CombineIndexExcerpts/Run
AMLEO GenerateCompleteNews/Run
AMLEO SaveCompleteNews/Run
