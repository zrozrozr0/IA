# Artificial Intelligence 8-puzzle MATLAB project

## Authors: 
Olivia Whitman (.68) 
<br>
Jae Lee (.4810)

## Randomly generated states:
The 100 states were generated using the pgenerator function which accepts an integer value.
The value passed to the function indicates the number of random moves to make (avoiding previously visited states) starting with an initial state that is the goal.
 - Due to this random movement it is not guarenteed that the returned state is the same depth as the number of moves taken to get there.
 - Since we begin with the goal state and randomly move the blank space around it is safe to assume that any generated state exists in the set of solvable initial states for the 8-puzzle.

#### Note:
The generated state is an integer where each digit is a tile number where the ordering is the current arrangement of the tiles.
In addition, the digit ```9``` is used to denote the blank space.
Thus the goal state can be stated as ```123456789```.

## Running the program:

#### Running algorithms individually

To run an algorithm individually, begin by taking an initial state and creating an initial puzzle state which can be done using the puzzle class.
Then feed this puzzle object to your desired algorithm.
This method will print out the running time and path to goal state from the initial state.
<br>
Below is an example of running solely BFS for an initial state of ```123465789```.
<br>
``` 
initial_state = puzzle(123465789);
BFS(initial_state)
```

#### Running all algorithms for 100 generated states

To run all 100 generated states for every algorithm and generate the histogram plots, run the ((main program)).

