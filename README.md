# dynamic-programming
Following along with the freecodecamp Dynamic programming course

## Source

For reference, the course in question can be found [here](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12153s&ab_channel=freeCodeCamp.org)
I definitely suggest you watch the videos as they will explain what's happening a lot better than someone who just looks at the code.

## Structure

- The course content is structured into two parts, part one discusses [memoization](https://en.wikipedia.org/wiki/Memoization), and part two discusses tabulation. I've split the files to reflect this, where file `1-Memoization` refers to part one, and `2-Tabulation` refers to part two.
- If you'd like a brief difference between tabulation and memoization, [Geeks for geeks](https://www.geeksforgeeks.org/tabulation-vs-memoization/link) has a good brief write-up on it.


## Alivin's Memoization Recipe
(Note Alivin is the course presenter and creator)

1. Make it work.
  - Visualize the problem as a tree
  - Implement the tree using recursion
    - Thing of the end nodes as the base case for your recursion
  - test it, it may take a long time to run, i.e. brute force.

2. Make it efficient.
  - add a memo object.
    - Make sure the object is shared.
  - Add a base case to return memo values ( memo fetching logic )
  - Store values into the memo, i.e. pass along the values to future calls

For progression sake, you can view the brute force solutions for problems, and then the memoization versions of the functions that make use of the memo objects to store processed calls in the files I've provided.

### Note

Please note, the course is created in nodejs, and as such all the code is written in JavaScript. Whereas my code is in python.