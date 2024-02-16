## Question Description

As a part of the route planner, the _routeExists_ method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.

The roads on the map are reasterized and produce a matrix of boolean values - _true_ if the road is present or _false_ if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the _routeExists_ method so that it returns _true_ if the destination is reachable or _false_ if it is not. The _fromRow_ and _fromColumn_ parameters are the starting row and column in the _mapMatrix_. The _toRow_ and _toColumn_ are the destination row and column in the _mapMatrix_. The _mapMatrix_ parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return _true_ since the destination is reachable:
```
boolean[][] mapMatrix = {
    {true,  false, false},
    {true,  true,  false},
    {flase, true,  true}
};

routeExists(0, 0, 2, 2, mapMatrix);
```

## Notes

This was a real toughy, rated **"Hard"** and claiming a duration of 30 minutes. It took me an hour or two to get my first result in RoutePlanner.java, which passed all the functional tests but lost 25% for not being performant. I assume this was because every time I returned adjacent coordinates to the cursor, I would construct a new SimpleEntry object to represent the coordinates. I also made a new object every time the cursor moved. I was scared of unexpected behavior with object references which was part of the reason for making new objects but it was also because I hadn't coded in a straightforward way of "getting" other coordinates.

In my second solution found in RoutePlanner2.java, I passed the performance test and also had what I feel is much more robust and readable code. There was less nested code pyramid-ing to the right, and I was able to not ever have to create new objects throughout the map traversal by abstracting the map as a custom RasterizedMap object made up of custom Coordinate objects. It was a little weird for it all to be in the same parent class and make the custom objects nested classes but it had to be that way to be run by the tester at TestDome.

The basic logic is more or less the same in both solutions:
1. Check if the _from_ coordinate or _to_ coordinate are not traversable, in which case there is no solution.
2. Set a _cursor_ to the from coordinate.
3. Get adjacent coordinates to the cursor.
4. Loop the the adjacent coordinates, and check if any of them are the destination.
5. If not, check if they are traversable or have already been traversed, and move the cursor to one of them.
- As there could be multiple tangents from the cursor, keep track of them in a Stack.
- If you run out of adjacent coordinates and tangents that are traversable and untraversed, and haven't found the destination, it is not reachable.

This is just brute forcing if there is any solution at all by potentially checking every single cell connected to the from coordinate. It does seem a little complicated and potentially overdesigned for what it's goal is and I haven't thought of a simpler way. Though I feel like there is one. Just a feeling.