Title: The birth of MJIN world
Date: 2017-09-10 00:00
Category: News
Slug: mjin-world-birth
Lang: en

![The birth of MJIN world](images/2017-09-mjin-world-birth.png)

This article describes the birth of MJIN world in August 2017.

**mjin-player**

As you know, [we spent July to research scripting]({filename}/articles/2017-08-scripting-research.md). We found a solution that satisfies the following criteria. Scripts should:

0. run unchanged on all supported platforms
0. allow extending C++ code

We have verified the second criterion by writing a sample application. The first criterion was taken for granted because it SHOULD be true.

At the time, we saw two ways to verify the first criterion:

0. create one sample application for each platform to verify scripting only
0. create a single cross-platform application, which can run any code

We chose the second approach because it is more beneficial in the long run. As you might have guessed, [mjin-player](https://bitbucket.org/ogstudio/mjin-player) is that application.

mjin-player serves as a base for the rest of MJIN projects to make them run on all supported platforms. However, there's no magic trick to hide the projects from the platform, and there was no such intention. Instead, mjin-player provides a consistent set of rules how other MJIN projects should be structured to be able to run on all supported platforms.

**mjin-application**

This set of rules for MJIN projects is packaged into [mjin-application](https://bitbucket.org/ogstudio/mjin-application). mjin-application is a library that provides basic functionality every MJIN project would need and nothing more. For instance, mjin-application does not and will not contain scripting or any other specific functionality.

**MJIN world**

So what is [MJIN world](https://bitbucket.org/ogstudio/mjin)? It's a set of projects that constitute our game development tools. mjin-player and mjin-application are the first bricks of the newly born MJIN world. A lot more to come. Stay tuned for the brighter MJIN future.

That's it for describing the birth of MJIN world in August 2017.

