Title: Examples and dependencies
Date: 2018-08-21 00:00
Category: News
Slug: examples-and-dependencies
Lang: en

![Screenshot][screenshot]

This article describes two new OpenSceneGraph cross-platform examples and the
change in handling dependencies.

**Examples of HTTP client and node selection**

Once we finished working on [the remote debugging example][osgcpe-04] and
[reported its completion][article-2018-june], we were surprised by the fact
that secure HTTP connection between a debugged application and debug broker
was only working in the web version of the example. Desktop and mobile versions
only worked with insecure HTTP.

Since current debug scheme has no authentication, insecure debugging over HTTP
doesn't really hurt. However, if we want to access resources located at popular
sites like GitHub and BitBucket, we have to support secure HTTP.

The need to support HTTPS on each platform spurred us to create
[HTTP client example][osgcpe-03]. Turned out, each platform had its own
preferred way of doing secure HTTP:

* web (Emscripten) provides Fetch API
* desktop is fine with Mongoose and OpenSSL
* Android provides HttpUrlConnection in Java
* iOS provides NSURLSession in Objective-C

The need to support different languages on different platforms resulted
in the creation of so-called 'host-guest' pattern:

* guest (platform agnostic)
    * provides networking representation
    * used by cross-platform C++ code
* host (specific platform)
    * polls guest for pending requests
    * processes them
    * reports results back to the guest

[Node selection example][osgcpe-05] was straightforward and caused no troubles.

**The change in handling dependencies**

For over a year we had to deal with the following
[shortcomings][osg-shortcomings] when building OpenSceneGraph across platforms
using conventional methods:

* macOS builds failing due to certain compile flags we use
* hacking PNG plugin safety guards to have PNG support under Android
* iOS simulator and device builds of the same example being in separate Xcode projects
* OpenSceneGraph taking 20-30 minutes to build

These shortcomings were slowing us down and complicating the development of
new examples. Upon hitting these problems ten more times this month we decided
it was time to solve them once and for all. Now OpenSceneGraph is built as part
of each example in 2-3 minutes, and there's no more dependency magic involved.
We took the same approach of building dependencies as part of each example to
other external libraries like Mongoose and libpng-android, too.

With these obstacles out of the way, we can now iterate faster. Just in time
for the next technical demonstration of Mahjong 2!

That's it for describing two new OpenSceneGraph cross-platform examples and
the change in handling dependencies.

[screenshot]: {attach}/images/2018-08-21-examples-and-dependencies.png

[article-2018-june]: {filename}/articles/2018-06-27-example-driven-development.md

[osgcpe-03]: https://github.com/OGStudio/openscenegraph-cross-platform-examples/tree/master/03.HTTPClient
[osgcpe-04]: https://github.com/OGStudio/openscenegraph-cross-platform-examples/tree/master/04.RemoteDebugging
[osgcpe-05]: https://github.com/OGStudio/openscenegraph-cross-platform-examples/tree/master/05.NodeSelection

[osg-shortcomings]: http://forum.openscenegraph.org/viewtopic.php?t=17443
