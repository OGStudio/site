Title: OpenSceneGraph sample
Date: 2017-05-12 00:00
Category: News
Slug: osg-sample
Lang: en

![OSG sample][screenshot]


This article describes creation of the tutorials for building sample OpenSceneGraph application under Linux, macOS, Windows, and Android in April 2017.

Previous tutorials described how to install OpenSceneGraph under Linux, macOS, Windows and render a model using the standard **osgviewer** tool. This time we worked on a [sample OpenSceneGraph application](https://github.com/OGStudio/openscenegraph-cross-platform-guide-application) that would run under Linux, macOS, Windows, and Android.

The application is very basic and has the following features:

0. Render window creation
0. Model loading
0. Model rendering with simple GLSL shaders
0. Model motion with a mouse under Linux, macOS, Windows and a finger under Android



Creating the tutorials for Linux, macOS, Windows was so easy and straightforward, that it only took us half a month. We spent the second half of the month creating Android tutorial.

Our [first successful Android build][oct16_article] last year included hacks and non-obvious steps to make OpenSceneGraph run under Android. This time we wanted a cleaner, faster, and cheaper approach.

The approach we ended up with requires just a few files and a few changes to the original Android Studio project (with C++ support) to make sample OpenSceneGraph application run under Android.

Here's a quick rundown of the files:

0. GLES2 surface
0. Render activity to render to the surface
0. Native library Java interface
0. Native library C++ implementation
0. CMake file to build native library
0. Render activity layout
0. Model to display



Here's a quick rundown of the project changes:

0. Update Android manifest to use GLES2 and render activity
0. Reference native library's CMake file in the project's CMake file



OpenSceneGraph documentation suggests building OpenSceneGraph outside Android Studio with CMake. However, this approach has the following limitations:

0. You have to build OpenSceneGraph for each target architecture
0. You have to manually copy/reference built OpenSceneGraph libraries into Android Studio project



Our approach includes building OpenSceneGraph for those target architectures that Android Studio project is built for. Also, OpenSceneGraph is already referenced, so no extra work is required: you just need to rebuild the project, and you're done.

That's it for describing the creation of the tutorials for building sample OpenSceneGraph application under Linux, macOS, Windows, and Android in April 2017.

[screenshot]: images/2017-05_osg-sample.png
[oct16_article]: 2016-11-19_2016-october-recap.html
