# FirstPygame

Runs out of learn.py

1v1 and 3v3 are operational, 2v2 does not work right now (I haven't written the computer movement algo)

Plays a season built off of college basketball. Reg season is round robin of ur conference though you have option to do that multiple times.

Then conference playoffs: Half the teams in the conference qualify (6 from 12 teamers, 5 from 10, 4 from the Ivy League)
Single Elimination - If you get to the championship you auto-qualify for the main tournament. 
Conference semi-finals get you to a play-in round for the tournament (though maybe an auto qual if ur reg season was good)

Tournament is 32 teams in 4 regions, single elim series as usual.

In the actual game:

- At the top of the game screen, you can see the teams playing, what competition/stage it is, and the length of the series.

- Controls are arrow keys, if you do 2-player then the other is wasd, but default to arrow keys.

- Walls are all 1-directional (for reasons we can talk about if you want). Obv the outer walls will bounce you towards the field,
goal walls are a little trickier. Back of the goal has two walls. The back back one bounces back, the one more forward bounces forward.

- Here's the big one: The posts only bounce away from the goal. This might get changed later if I can figure it out,
but that means if you're sitting in the goal you can go through the post to the outside. SO CAN THE BALL. 
So that nobody scores by hitting the posts, there has to be a little buffer before the scoring area, and since the ball can escape,
it is possible to put the ball between the posts and not score. 
- To help out with the visual of this, the scoring area is colored in blue. If the center of the ball is in there,
a goal is scored. 
- It's RL overtimes, just first goal wins that game.

Any other questions of course let me know!!
 
