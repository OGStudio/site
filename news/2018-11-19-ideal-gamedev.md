Title: Ideal games and game development tools
Date: 2018-11-19 00:00
Category: News
Slug: ideal-gamedev
Lang: en

![Screenshot][screenshot]

In this article, we discuss how ideal video game and video game development tool look like, in our opinion.

**Questions**

As you know, the [goals of Opensource Game Studio][ogs-goals] are:

* creation of free video game development tools
* making video games with those tools
* preparing video game development tutorials

This time we asked ourselves two simple questions:

* What is an ideal video game?
* What is an ideal video game development tool?

The best answers we could think of are below.

**Answer 1: A video game is ideal if it delivers maximum pleasure possible**

While content is probably the most important aspect to keep a player invested into the game, the technical side is the transport to deliver that content. There are quite a few technical problems that may damage otherwise excellent content of a game:

* insufficient accessibility: the game does not run on your hardware
* insufficient optimization: the game is slow
* critical bugs: the game crashes from time to time

We work hard to make sure the games we create are accessible everywhere. That's why we released
[the second demonstration of OGS Mahjong 2][mahjong-demo2] only for the web: because you can run web version virtually anywhere.

**Answer 2: A video game development tool is ideal if it lets you create a video game of your dream in the shortest time possible**

Even though we put a lot of effort into sharing our knowledge through [guides][osgcpg] and [tutorials][osgcpe], we understand that those take a lot of time to study. One can't possibly make even a simple video game like [Memory][concentration] without performing the following steps:

* configure the development environment
* write code
* build an application
* debug the application
* repeat `write-build-debug` steps as many times as necessary

Writing code and debugging are probably the ultimate forms of input and output of any software, so we can't escape those. However, there are ways to completely remove (or at least significantly decrease) the need for `development environment setup` and `build` steps. And this is what we are going to do in the coming months.

Our goal for the coming months is to create a video game development tool that would allow any programmer (or sufficiently skilled person) to create the [Memory][concentration] video game from scratch in an hour.

That's it for discussing how ideal video game and video game development tool look like, in our opinion.


[screenshot]: images/2018-11-19-ideal-gamedev.png

[ogs-goals]: about.html
[mahjong-demo2]: 2018-10-02-mahjong-demo2.html
[osgcpg]: https://github.com/OGStudio/openscenegraph-cross-platform-guide
[osgcpe]: https://github.com/OGStudio/openscenegraph-cross-platform-examples
[concentration]: https://en.wikipedia.org/wiki/Concentration_(game)
