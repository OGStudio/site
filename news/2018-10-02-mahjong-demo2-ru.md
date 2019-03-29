Title: OGS Mahjong 2: Demo 2
Date: 2018-10-02 00:00
Category: News
Slug: mahjong-demo2
Lang: ru

![Screenshot][screenshot]

Мы рады сообщить о выпуске второй демонстрации OGS Mahjong 2. Её целью были улучшение техники разработки и создание надёжной основы кроссплатформенной разработки.

**Выпуск**

Запустите последний выпуск OGS Mahjong 2 в вашем браузере: [http://ogstudio.github.io/ogs-mahjong](http://ogstudio.github.io/ogs-mahjong)

Рекомендуем запускать игру с параметром `seed` следующим образом: [http://ogstudio.github.io/ogs-mahjong?seed=0](http://ogstudio.github.io/ogs-mahjong?seed=0)

Это позволяет вам играть в ту же самую раскладку после перезапуска.

Каждое значение зерна (seed) однозначно задаёт расположение фишек, так что разные значения зерна дают разнообразие партий.

**Техника разработки и основа**

Во время разработки второй демонстрации мы перешли с обычной разработки на [разработку через создание примеров][article-2018-june]. Это привело к появлению трёх различных хранилищ для обеспечения разработки OGS Mahjong 2:

* Хранилище [кроссплатформенных примеров OpenSceneGraph][osgcpe] содержит основу вроде работы с ресурсами, создание графического окна и т.д.
* Хранилище [компонент OGS Mahjong][omc] содержит специфичную для Маджонга функциональность вроде разбора раскладки, сопоставления фишек и т.д.
* Хранилище [OGS Mahjong][ogs-mahjong] содержит снимок набора функциональностей `компонент OGS Mahjong`, которые определяют версию игры. Например, версия `Demo 2` почти полностью повторяет пример [05.ColorfulStatus][omc-05] из `компонент OGS Mahjong`.

**За пределами пасьянса Маджонг**

В дополнение к параметру `seed` вы можете указать игре использовать удалённую раскладку, расположенную на GitHub: [http://ogstudio.github.io/ogs-mahjong?seed=0&layout=github://OGStudio/ogs-mahjong-components/data/cat.layout](http://ogstudio.github.io/ogs-mahjong?seed=0&layout=github://OGStudio/ogs-mahjong-components/data/cat.layout)

Использование удалённых ресурсов открывает огромные возможности, т.к. позволяет любому желающему создать раскладку на свой вкус и моментально её проверить.

Наш следующий шаг - это выделение игровой логики в виде ресурса.


[screenshot]: images/2018-10-02-mahjong-demo2.png

[article-2018-june]: 2018-06-27-example-driven-development.html
[osgcpe]: https://github.com/OGStudio/openscenegraph-cross-platform-examples
[omc]: https://github.com/OGStudio/ogs-mahjong-components
[ogs-mahjong]: https://bitbucket.org/ogstudio-games/ogs-mahjong
[omc-05]: https://github.com/OGStudio/ogs-mahjong-components/tree/master/05.ColorfulStatus
