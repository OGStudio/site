Title: OpenSceneGraph cross-platform examples
Date: 2018-04-20 00:00
Category: News
Slug: openscenegraph-examples
Lang: en

![Screenshot][screenshot]

This article summarizes the work we did to produce the first two
cross-platform OpenSceneGraph examples.

By the time [the first technology demonstration of OGS Mahjong 2][tech-demo-1]
has been released, we've already had [issue request][android-image-issue]
(to explain how to load images with OpenSceneGraph on Android) hanging for some
time. We considered creating a new tutorial for
[OpenSceneGraph cross-platform guide][osgcpg] at first. However, we realized
that it's time-consuming and excessive for such a tiny topic (compared to
what an average game has) as image loading. We decided to continue sharing our
knowledge in the form of concrete examples. That's how
[OpenSceneGraph cross-platform examples][osgcpe] were born.

Each example:

* explains crucial code necessary to perform a specific task
* accents platform-specific nuances
* provides implementations to cover desktop, mobile, and web platforms
* provides a web build to showcase results

The first two examples cover the following topics:

* Embed resource into executable: this greatly simplifies resource handling across platforms
* Use PNG images with PNG plugins: this explains the requirements necessary to build and use PNG plugins

We will be adding new examples as we proceed with OGS Mahjong 2 development.

That's it for summarizing the work we did to produce the first two cross-platform OpenSceneGraph examples.


[screenshot]: {attach}/images/2018-04-20-openscenegraph-examples.png

[tech-demo-1]: {filename}/articles/2018-02-16-mahjong-techdemo1-gameplay.md
[android-image-issue]: https://github.com/OGStudio/openscenegraph-cross-platform-guide/issues/4
[osgcpg]: https://github.com/OGStudio/openscenegraph-cross-platform-guide
[osgcpe]: https://github.com/OGStudio/openscenegraph-cross-platform-examples

