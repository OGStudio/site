Title: Teaching kids to program
Date: 2019-02-04 00:00
Category: News
Slug: teaching-kids-to-program
Lang: en

![Screenshot][screenshot]

In this article, Michael shares his experience of teaching kids to program.

Here's what he covers:

- organization of the learning process
- learning plan
- memory game
- development tools
- lessons
- results and plans

**Organization of the learning process**

The learning process is conducted as part of corporate social responsibility: a company provides a room with equipment and connects employees that want to try themselves in the role of teachers with employees that want their kids educated. All this is done voluntarily.

Potential teachers are divided into groups so that each group contains three teachers: experienced one and two novice ones. Such a group of three teachers leads a group of students. Students are divided into groups by age and skills.

I participated in the program as a teacher for the second time in 2018. The kids were around ten years old. Our group was active from October to December of 2018 each Saturday, 10:00-12:00. Using my position as a teacher, I've also brought my wife in as a student.

**Learning plan**

The first time I participated in the program, our group taught kids rather mindlessly: we were coming up with simple tasks to explain different operators. By the end of the course we had nothing concrete to evaluate, analyze, and share.

This second time I decided we are going to create a memory game with kids. I decided to consider the course successful if by the end of the course each kid would be able to create a simple memory game from scratch in an hour.

To achieve that, we were recreating the same game from scratch each lesson. I'd like to stress that we did not use personal accounts to save progress. Our task was to save the skill of game creation in the head, not a PC.

**Memory game**

Let's see what the memory game is.

**1)** In the simplest case we have 16 cards, only 8 of them are unique, the rest 8 are duplicates of the unique ones.

![Screenshot][all-cards-face-up]

As you can see, we only have two cards with a cat, only two cards with a dog, etc..

**2)** At the start we shuffle the cards and place them with their faces down.

![Screenshot][all-cards-face-down]

**3)** The first game player turns a pair of cards.

![Screenshot][first-pair]

**4)** If the cards differ they are once again turned face down.

![Screenshot][all-cards-face-down]

**5)** The next player turns another pair of cards.

![Screenshot][second-pair]

**6)** If the cards are the same, they are removed from the field.

![Screenshot][remove-pair]

The goal of the game is to remove all cards from the field. There's no competition here so the game can be played alone.

From one hand, the memory game is rather simple. From the other hand, the game implementation requires essential functionality each more or less complex game has:

- creation of items
- arrangement of items
- selection of items
- comparison of items
- removal of matching items

**Development tools**

We used Scratch as our development tool. [Scratch][scratch] is a great tool to teach kids to program because each action, each operation is represented graphically.

For example, you can rotate a cat 360 degrees in 1 second using the following script:

![Screenshot][cat-script]

Here's how it looks like in action:

![Animation][cat-animation]

I'd like to stress that Scratch is a rather successful solution to represent code graphically. For example, a paid solution by SAP uses similar concept of cubes to program logic:

![Screenshot][sap-ui]

Users can only input values into predefined fields. If users want more functionality they have to resort to scripts.

Personally, I have never witnessed any slowdown in Scratch, and there were many in SAP's solution.

**The first lesson**

The first lesson was introductory, we didn't use PCs.

The plan was to:

1.  Meet
2.  Play the memory game with cards
3.  Learn the concept of algorithm
4.  Detail the game's algorithm
5.  Analyze the lesson

**1)** Meeting

Both teachers and students stand in a circle. This equalizes everyone and makes everyone a team member.

The first team member tells his name and why he decided to take the course. The second team member and the rest first repeat the name and the story of each previous team member before telling their own names and stories.

Here's how it looks like:

1. John: "My name is John, I am going to study Scratch because my father forces me to"
2. Alex: "This is John, he's doing Scratch because his father wants him to do it. My name is Alex, and this is my fourth year with Scratch"
3. Ann: "That's John, his parents force him to do Scratch. This is Alex, he's a Scratch veteran. And I'm Ann, a novice teacher, so I'm going to learn together with you all"

Such a format of meeting has the following objectives:

- Getting to know each other
    - Each team member should know other team members by name
- Common space
    - Everyone is in the circle, not at a working desk, this prevents distraction of kids by PC games
- Equality
    - Both teachers and students are in the same circle, this equalizes everyone as a team member without hierarchy
- Attention
    - Each team member should listen carefully to be able to correctly repeat what others said
- Feedback
    - Each team member should be as clear as possible when expressing thoughts, otherwise nobody would be able to repeat them
- Fun
    - Memorization problems produce lots of laughter

**2)** Memory game with cards

1. Take 8 pairs of the same cards from two decks of cards
2. Place the cards in 4 x 4 grid, faces down
3. Students stand up around single table
4. Each student, one by one, turns a pair of cards
    - If cards match, they are taken off the field
    - If cards differ, they are once again turned face down

Students are eager to play tabletop games. During the game party teachers say out loud each step in the game's algorithm.

After a couple of parties it's time to find out what algorithm is.

**3)** The concept of algorithm

1. Ask students first, hear them out to find out their level
2. Correct what students say if they were close to an expected answer
3. Ask students to write an algorithm to move a man from "stands outside a room" state into "sits and works at a PC" one

Students like to go to blackboard and write, so we ask each student to come and write a single step of the algorithm at a time. The most active student should execute the algorithm by following it strictly.

**4)** The algorithm of the game

Ask students to compose the game's algorithm. Again, let students come to the blackboard and add one step of the algorithm at a time. Once the algorithm is ready, play the game with cards once again. Now, each student should say the algorithm's step he executes.

Here's how it looks like:

1. John: "Place 16 cards faces down"
2. Alex: "Turn a pair of cards"
3. Paul: "If the cards differ, turn them faces down again"
4. Dan: "Turn another pair of cards"
5. Mike: "If the cards match, take them off the field"

**5)** Analyze the lesson

That's it for the first lesson. Teachers finally have time to discuss the lesson: discuss the kids, approaches to shy and active kids, plan next lessons.

We had the following decisions:

1. Arrange students so that active ones sit next to shy ones as "active-shy-active-shy-etc" so that we don't end up with two groups of shy and active students at different sides of a room, which would hamper productivity.
2. Only accept accurate answers from students because active students like to wriggle, which hampers discipline.

**The second and the third lessons**

We were beginning each lesson with the same meeting: we would stand up in a circle, tell our names and what we did. Those who did nothing should have said why. Just as before, everyone should first repeat what previous team members said.

We spent the second lesson to create requirements for an item of the playfield and then create the item in Scratch. This was moderately successful.

We spent the third lesson trying to create 16 items and arrange them in 4x4 grid. We failed miserably because we could not explain coordinate system to students. It became apparent that lesson plans were only plans, reality had its own demands.

We saw two ways to approach the problem:

1. Keep on studying the coordinate system risking not to get the game done by the end of the course
2. Change the game requirements so that coordinate system is not necessary

We went the second way because, after all, we're not a school, our goal was to teach kids to create the game, i.e., use skills in practice, not theory. That's why we replaced 4x4 grid with a circle of 16 items.

This solution sparkled a few thoughts in my head:

1. One can often find a simpler path to solve an issue
2. This path is simpler to understand, albeit less flexible
3. One can go the harder path to increase flexibility much later when it becomes absolutely necessary
4. Simplification moves one closer to the goal, complexification moves one in the opposite direction

**The fourth and the rest of the lessons**

The fourth lesson marked the end of coming up with requirements in class because doing so started to take too much time. We chose practice over theory once again to meet the deadline. This time all requirements were conducted before the lesson. Still, nobody read them.

We spent the fourth and the fifth lessons to create 16 items in circle, select a pair of items and match them.

We started recreating complete game from scratch on the sixth lesson. Each time students were recreating complete game faster and faster. On the eighth lesson we introduced a leaderboard to track how fast each student recreates a specific part of the game.

**The last lesson**

When the last lesson approached everyone was able to create the memory game from scratch more or less independently in two hours.

Here's the leaderboard of the last lesson (names are hidden):

![Screenshot][leaderboard]

The leaderboard is in Russian, here are the captions translated:

- Name
- Circle of items
- Selection of pairs
- Hide all
- Hide a pair

Here you can witness the creation of the memory game from scratch by the fastest student: in just half an hour.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WlA193S3SPY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br/>

**Results and plans**

The results surpassed my expectations:

- three students made it in an hour or faster
- two students made it in an hour and a half or faster

This year I plan on doing another round of the memory game recreation. However, I'm going to replace Scratch with Opensource Game Studio tools: the students will use Lua, Git, and GitHub Pages.

That's it for sharing Michael's experience of teaching kids to program.

[screenshot]: images/2019-02-04_teaching-kids-to-program-team.png

[all-cards-face-up]: images/2019-02-04_teaching-kids-to-program-all-cards-face-up.png
[all-cards-face-down]: images/2019-02-04_teaching-kids-to-program-all-cards-face-down.png
[first-pair]: images/2019-02-04_teaching-kids-to-program-first-pair.png
[second-pair]: images/2019-02-04_teaching-kids-to-program-second-pair.png
[remove-pair]: images/2019-02-04_teaching-kids-to-program-remove-pair.png
[scratch]: https://scratch.mit.edu/
[cat-script]: images/2019-02-04_teaching-kids-to-program-cat-script.png
[cat-animation]: images/2019-02-04_teaching-kids-to-program-cat-animation.gif
[sap-ui]: images/2019-02-04_teaching-kids-to-program-sap-ui.png
[leaderboard]: images/2019-02-04_teaching-kids-to-program-leaderboard.png
