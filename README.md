I was messing around on the Minecraft 20w14∞ update (April Fools 2020) and ultimately went to the ant dimension. There, you've got the 'An Ant' block, which simulates [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) when placed on top of white or black concrete.

I thought that was pretty cool, and decided to make it in Python, so here it is.

There are two versions here. The first one I made, which is just text in a terminal, is a bit different from the original. That is because it wraps around when the ant eventually wants to go outside of the finite 'map' you give to it. That breaks the usual deterministic pattern. 
However, it shouldn't be an issue if you choose a big enough size, as the ant eventually gets in an infinite loop, creating a 'highway' in one direction.

The second version requires Pygame, and has a bit more features.
You can:
- speed up/slow down the simulation
- pause it
- save a screenshot of the current frame
and I guess you can add infinitely more features in the code itself.

Enjoy? I surely did while making it :]
