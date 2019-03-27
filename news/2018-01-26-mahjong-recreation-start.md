Title: Mahjong recreation start
Date: 2018-01-26 00:00
Category: News
Slug: mahjong-recreation-start
Lang: en

![Screenshot][screenshot]

This article describes the start of Mahjong game recreation.

**Plan**

We started Mahjong recreation endeavour by composing a brief plan to get gameplay with minimal graphics:

* Load single layout
* Place tiles in layout positions
* Distinguish tiles
* Implement selection
* Implement matching

Just like any other plan, this one looked fine at first sight. However, once you get down to work, new details start to come out. This plan was no exception. Below are a few problems that came out during development.

**Problem №1: provide binary resources across supported platforms**

Mahjong is going to be available on desktop, mobile, and web. Each of these platforms has its constraints on accessing external files:

* Desktop can access almost any file
* Android/iOS have limited access to file system
* Web does not have any file system at all

To provide a unified way for accessing resources, we decided to include them into final executable. This decision led to the birth of **mjin-resource** and **mahjong-data** projects.

[mjin-resource][mjin-resource]:

* converts binary files to C header files with the help of **xxd** utility
* generates MJIN project that contains generated headers to be compiled into static library
* provides C++ interface for accessing generated resources

[mahjong-data][mahjong-data] is an example of such generated MJIN project that is referenced by [mahjong][mahjong] project.

**Problem №2: load PNG images across supported platforms**

To load PNG, we use corresponding OpenSceneGraph plugin. We built it for desktop with no issues. Building for web (Emscripten) turned out to be more difficult: Emscripten provides its own version of **libpng**, which OpenSceneGraph build script can't detect. We had to work around several OpenSceneGraph checks to successfully build the plugin for Emscripten.

Building the plugin for Android and iOS is still waiting for us. Once we get PNG plugin working across supported platforms, we are going to publish a new tutorial for [OpenSceneGraph cross-platform guide][osgcp_guide] to cover PNG image loading. We already got a [request to describe image loading][img_loading_issue].

**Development**

[As you know][lets-go], we published OpenSceneGraph cross-platform guide to make OpenSceneGraph community stronger. We value education, and we love to share our knowledge. That's why we decided to develop Mahjong in small reproducible chunks uniquely identified by internal versions. These versions are available in [mahjong repository][mahjong].

We also provide [version history and web releases of each internal version][web-releases] for the following reasons:

* education: show how development looks like internally
* accessibility: provide older versions for comparison

**Current Mahjong game status**

As of the time of this writing, we have implemented tile selection. [Try it in your browser!][mahjong-version-tile-selection]

Once we finish tile matching implementation, we are going to publish the intermediate result for all supported platforms.

That's it for describing the start of Mahjong game recreation.


[screenshot]: images/2018-01-26-mahjong-recreation-start.png

[mjin-resource]: https://bitbucket.org/ogstudio/mjin-resource
[mahjong]: https://bitbucket.org/ogstudio-games/mahjong
[mahjong-data]: https://bitbucket.org/ogstudio-games/mahjong-data
[osgcp_guide]: https://github.com/ogstudio/openscenegraph-cross-platform-guide
[img_loading_issue]: https://github.com/OGStudio/openscenegraph-cross-platform-guide/issues/4
[lets-go]: 2017-03-16_lets-go.html
[web-releases]: http://ogstudio.github.io/game-mahjong
[mahjong-version-tile-selection]: https://ogstudio.github.io/game-mahjong/versions/010/mjin-player.html

