Title: Example-driven development
Date: 2018-06-27 00:00
Category: News
Slug: example-driven-development
Lang: en

![Screenshot][screenshot]

This article explains how the third OpenSceneGraph cross-platform example opened our eyes to example-driven development.

**2018-08 EDIT**: the third example has been renamed to the fourth one due to the reasons described in the [next article][article-2018-august].

**The third OpenSceneGraph cross-platform example**

The third OpenSceneGraph cross-platform example explains how to implement [remote debugging across platforms][osgcpe-04]. This example is less about OpenSceneGraph and more about different platforms.

Remote anything nowadays assumes the use of HTTP(s) over TCP/IP. Thus, the first idea was to embed HTTP server into an application and let HTTP clients interact with the server.
However, serving HTTP across all platforms is complicated:

* desktops have firewalls
* mobiles have restrictions on background processes
* web browsers are HTTP clients by design

That's why we decided to create a mediator between debugged application and UI.  [Debug broker][debug-broker], a small Node.js application, became that mediator.  Debug broker uses no external dependencies, so it's easy to run virtually anywhere. Also, since debug broker is a server application, you can configure it once and use it for any number of applications.

Both [debug UI][debug-ui] and [debug broker][debug-broker] use JavaScript because we wanted these tools to be accessible from anywhere with no prior installation. This decision limited us to web browser solution. Providing any sort of desktop application would incur additional installation and maintenance effort, which would only complicate the tools.

**Example-driven development establishment**

Once the third example was implemented, we realized how important and beneficial it is to develop new features outside the main project:

* the main project is freed from excessive commit noise
* a new feature is publicly shared for everyone to learn, criticize, and improve

When we publicly share our knowledge:

* we must create documentation for everyone (including ourselves later) to understand what's going on
* we must not use hacks because that would break your trust in us

From now on, all new features like input handling, Mahjong layout loading, resource caching, etc. are going to be first implemented as examples.  We call this example-driven development.

That's it for explaining how the third OpenSceneGraph cross-platform example opened our eyes to example-driven development.

[screenshot]: images/2018-06-27-example-driven-development.png
[article-2018-august]: 2018-08-21-examples-and-dependencies.html

[osgcpe-04]: https://github.com/OGStudio/openscenegraph-cross-platform-examples/tree/master/04.RemoteDebugging
[debug-broker]: https://github.com/OGStudio/debug-broker
[debug-ui]: https://github.com/OGStudio/debug-ui

