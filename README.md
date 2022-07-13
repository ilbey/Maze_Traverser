# Maze_Traverser

This program automatically extracts nodes from the imported map file. 
And by recording their coordinates, it creates the shortest path graph 
using the A* algorithm (Manhattan Distance to determine heuristics) between 
these coordinates. This program keeps the graph as an adjency matrix. 
Distances between nodes are printed to the user. And the user is expected to 
enter an input for BFS or UCS operations. Process is carried out upon request. 
While processing BFS and UCS, I didnot use queue or priority queue. However, 
I used just adjency matrix with queue logic. And he writes the result with his 
statistics on the screen and finishes his job. If you want to do the other operation, 
you can run the program again and print the results in the other method.

Short Description Functions:
map gets globally, positioned top of my program. It can be changeable there.

main() method: this is detects exact nodes coordinates except '*' and ' '.And also,
this method calls helperFunc() method for filling weights between these nodes. After
this method prints nodes and weights, takes input from user, directs bfs() or ucs() methods.
At last, directs all variables to the stat() method.

helperFunc() method: takes initial and goal positions of nodes. It sends these positions to
AStar() method, then it takes f and pos value. It processes new position according to pos value.
Then, it controls a list for that there is any stuck condition or not. If it is a stuck condition,
it gives manual position value. Lastly, it returns counter which is usıng for distances between
one node to another.

AStar() method: It finds the heuristic of the position, right, left, up and down positions, to the 
target position using manhattan distance and adding the value to it. Then returns f and pos values 
to the helperFunc () method.   
