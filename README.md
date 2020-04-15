# charlie-checkers

This AI python program allows you to play checkers against Charlie who is a bright intelligent agent. Charlie uses the min max algorithms to calculate his moves.

We implemented the min max algorithm with a heuristic function that calculates the difference of safe spaces between Charlie (AI) and the human player. Kings are worth 2 for their value.

Heuristic Equation = Charlie's Safe Spaces - Human Player's Space Spaces

Charlie, the artificial intelligent agent is represented as Red and the human player is represented as Black. 
We use r and b to represent the checker pieces of Charlie and the player respectively.  
We will also use R and B to represent the king pieces of Charlie and the player respectively. 

The game runs by the standard checker rules. The only exception is that if you jump into the last row, you become a king and have the ability to jump backwards!

When starting the game, you will be prompted to enter your move:
To make a move, you need to enter 4 parameters onto the command screen: type of move, x coordinate, y coordinate, and direction. 

Examples of a valid input would be "move 1 5 upright" and "jump 2 4 upleft"

The move commands are: "move" and "jump"

The next two commands for x and y positions are integers within the range:
0, 1, 2, 3, 4, 5, 6, 7

The direction commands are: "upleft", "upright", "downleft", "downright"

The link to our demo video:

https://youtu.be/XgbqjpFmHDA

Made with my friend Ryder Roedel! 
