Title: OGS Mahjong 2: Demo 2
Date: 2018-10-02 00:00
Category: News
Slug: mahjong-demo2
Lang: en

![Screenshot][screenshot]

We are glad to announce the release of the second demonstration of OGS Mahjong 2.
The purposes of this release were to refine our development techniques and
build a solid cross-platform foundation.

**Release**

Run the latest version of OGS Mahjong 2 in your web browser:
[http://ogstudio.github.io/ogs-mahjong](http://ogstudio.github.io/ogs-mahjong)

You are encouraged to run the game with `seed` parameter like this:
[http://ogstudio.github.io/ogs-mahjong?seed=0](http://ogstudio.github.io/ogs-mahjong?seed=0)

This allows you to play the same layout each time you launch the game.

Each seed uniquely identifies the placement of tiles. Thus, different seeds
give you a different experience.

**Development techniques and foundation**

During the second demonstration development, we switched from standard
development to [example-driven one][article-2018-june]. This resulted in the
creation of three distinct repositories to back the development of OGS Mahjong 2:

* [OpenSceneGraph cross-platform examples][osgcpe] repository provides cross-platform foundation like resource handling, render window setup, etc.
* [OGS Mahjong components][omc] repository provides Mahjong specific functionality like parsing layout, matching tiles, etc.
* [OGS Mahjong][ogs-mahjong] repository contains snapshots of `OGS Mahjong components` features that comprise specific game version. E.g., `Demo 2` version is almost identical to [05.ColorfulStatus][omc-05] example of `OGS Mahjong components`.

**Beyond Mahjong solitaire**

In addition to `seed` parameter, you can let the game use remote layout hosted at GitHub:
[http://ogstudio.github.io/ogs-mahjong?seed=0&layout=github://OGStudio/ogs-mahjong-components/data/cat.layout](http://ogstudio.github.io/ogs-mahjong?seed=0&layout=github://OGStudio/ogs-mahjong-components/data/cat.layout)

Utilizing remote resources is an extremely powerful approach allowing anyone
to create a layout of his/her choice and see the layout in action instantly.

Our next step is to turn game logic into a resource, too.

[screenshot]: {attach}/images/2018-10-02-mahjong-demo2.png

[article-2018-june]: {filename}/articles/2018-06-27-example-driven-development.md
[osgcpe]: https://github.com/OGStudio/openscenegraph-cross-platform-examples
[omc]: https://github.com/OGStudio/ogs-mahjong-components
[ogs-mahjong]: https://bitbucket.org/ogstudio-games/ogs-mahjong
[omc-05]: https://github.com/OGStudio/ogs-mahjong-components/tree/master/05.ColorfulStatus
