package routeplanner;

import java.util.*;
import java.util.AbstractMap.SimpleEntry;
import java.util.Map.Entry;

public class RoutePlanner {

    /* This answer got all the right answers but I lost 25% because it wasn't performant on a large map.
     * I actually don't know for sure that it worked correctly on the large map, it just says it exceeded the time limit for that
     * test case, which functions explicitly as a performance test. So I assume the possible edge cases to test a 'correct'
     * algorithm were covered by the smaller map tests.
     * 
     * I'd like to start improving this by making it more object oriented.
     * I'd like to make a nested class describing a RasterizedMap
     * and another describing a Coordinate that the map is made up of.
     * A rasterizedMap should have a getter for x,y range and getter for Coordinate at x,y location.
     * Each Coordinate should have x,y position and flag for whether they've been traversed,
     * getter/setters for all these values. Should also override .equals to check equality.
     */

    public static boolean routeExists(int fromRow, int fromColumn, int toRow, int toColumn, boolean[][] mapMatrix) {
        if (mapMatrix[fromRow][fromColumn] == false || mapMatrix[toRow][toColumn] == false) return false;
        //we need to track which coordinates we've already been at
        ArrayList<Entry<Integer, Integer>> traversedCoordinates = new ArrayList<>();
        traversedCoordinates.add(new SimpleEntry<>(fromRow, fromColumn));
        //while loop until the 'to' coordinates are found,
        //   or until there are no adjacent coordinates that are both true and not already traversed
        boolean validCursor = true;
        ArrayList<Entry<Integer, Integer>> adjacentCoordinates;
        Stack<Entry<Integer, Integer>> tangentCursors = new Stack<>();
        Entry<Integer, Integer> cursor = new SimpleEntry<>(fromRow, fromColumn);
        final int xRange = mapMatrix[0].length;
        final int yRange = mapMatrix.length;
        while(validCursor) {
            validCursor = false;
            adjacentCoordinates = getAdjacentCoordinates(cursor.getKey(), cursor.getValue(), xRange, yRange);
            for(Entry<Integer, Integer> option: adjacentCoordinates) {
                if (option.getKey().equals(toRow) && option.getValue().equals(toColumn)) {
                    //reached destination
                    return true;
                } else if (!traversedCoordinates.contains(option) && mapMatrix[option.getKey()][option.getValue()] == true) {
                    //not already traversed and traversable
                    if (!validCursor) {
                        traversedCoordinates.add(new SimpleEntry<>(cursor));
                        cursor = new SimpleEntry<>(option);
                        validCursor = true;
                        //I'm not sure if it's necessary for me to instantiate a new entry but it feels weird to not do it here
                        //now that the cursor's moved, continue the for loop and backlog any additional paths
                        continue;
                    } else {
                        //in this case we are backlogging a tangential path option
                        tangentCursors.add(option);
                    }
                }
            }
            //at this line, either there are no more paths and validCursor is false, or the cursor was moved and it's true
            if(!validCursor && !tangentCursors.isEmpty()) {
                traversedCoordinates.add(new SimpleEntry<>(cursor));
                cursor = new SimpleEntry<>(tangentCursors.pop());
                validCursor = true;
                //This allows the algorithm to whittle down the tangential paths
            }
        }
        return false;
    }

    //simple helper to find adjacent coordinates
    private static ArrayList<Entry<Integer, Integer>> getAdjacentCoordinates(int fromRow, int fromColumn, int xRange, int yRange) {
        ArrayList<Entry<Integer, Integer>> adjacentCoordinates = new ArrayList<>();
        if (fromRow > 0) {
            Entry<Integer, Integer> above = new SimpleEntry<>(fromRow - 1, fromColumn);
            adjacentCoordinates.add(above);
        }
        if (fromRow < yRange - 1) {
            Entry<Integer, Integer> below = new SimpleEntry<>(fromRow + 1, fromColumn);
            adjacentCoordinates.add(below);
        }
        if (fromColumn > 0) {
            Entry<Integer, Integer> left = new SimpleEntry<>(fromRow, fromColumn - 1);
            adjacentCoordinates.add(left);
        }
        if (fromColumn < xRange - 1) {
            Entry<Integer, Integer> right = new SimpleEntry<>(fromRow, fromColumn + 1);
            adjacentCoordinates.add(right);
        }
        return adjacentCoordinates;
    }
        
    public static void main(String[] args) {
        boolean[][] mapMatrix = {
            {true,  false, false},
            {true,  true,  false},
            {false, true,  true}
        };
        
        System.out.println(routeExists(0, 0, 2, 2, mapMatrix));
    }
}