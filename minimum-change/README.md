This challenge will tackle the [change-making problem](https://en.wikipedia.org/wiki/Change-making_problem). The goal is to make minimum change for a given amount, assuming a separate given set of denominations. This should work for any arbitrary denomination set that consists only of positive integers, and includes a coin of denomination **1**.

### Understanding The Problem

This problem initially baffled me. The initial intuitive approach was subtract as many of the largest denomination possible from the total amount, until the amount becomes zero. This, as it turns out, is called the "greedy" method.

##### Example 1:
```
amount = 36
denominations = [1,5,10]
36 - 10 = 26
26 - 10 = 16
16 - 10 = 6
6 - 5 = 1
1 - 1 = 0
```

This solution gets 5 coins to make 36 (10,10,10,5,1) which would be accurate. In the United States coin system, this very simple solution should always work. However it would not work for all coin systems.

##### Example 2:
```
amount = 6
denominations = [1,3,4]
6 - 4 = 2
2 - 1 = 1
1 - 1 = 0
```

That gets 3 coins to make 6 (4,1,1) which is not accurate. The minimum change would be 3 + 3 = 6. I then thought, the only solution must be to try every possible permutation of the coins, keep them in memory, and then get the combination(s) of coins which are minimal. It was hard to imagine any way to do this, much less the best way. After some pondering I imagined a top-down tree beginning with the total amount at the top.

##### Example 3:
```
amount = 6
denominations = [1,3,4]
       6
     / | \
    5  3  2
  / | \
 4  2  1
```

Like that, but fully filled out... Take the left-most bottom child, get the depth, and then save the location of that child as the *current* minimal answer. Then iterate right and do the same thing, only replacing the *current* minimal answer if it has a lower depth in the tree. I will be writing a function which does exactly this in this exercise.

Before getting to it I found a different solution that seems a little easier to implement, and gets rid of some duplicated calculations. However I never could have come up with it on my own. It takes the principles of dynamic programming and uses a bottom-up iterative approach. It is described in [this video](https://www.youtube.com/watch?v=jgiZlGzXMBw) from 7:43 onward, and I will write a separate function that solves the problem using this method. Look at the one dimensional list he illustrates while iterating through and finding the minimal amount of coins. Instead of storing just the *minimal amount* of coins in the indexes of the list, I will store a nested list of the specific coins which make up that minimal amount. The logic behind the solution, however, will be basically the same.

If you are trying to understand this problem, I highly suggest you read and watch the links I have provided. They were very helpful for me.

### Usage

You can run change.py directly with the python3 interpreter.

Ex: python change.py amountInteger denomList [topDown|bottomUp]<br/>
*amountInteger*: Amount to make in change as an int, like 6<br/>
*denomList*: Denominations as a list, like [1,3,4]<br/>
*topDown|bottomUp*: Mutually exclusive arg to determine algorithm used. Optional. Default to bottomUp.

You can also execute change-test.py with no arguments to try the script against known inputs and answers.