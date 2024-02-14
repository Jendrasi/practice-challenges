package routeplanner;

import java.util.Stack;

/* I consider this answer to be much more object oriented and readable. It passed the functional tests as well as the performance test, for a 100%. */

public class RoutePlanner2 {

    private static class Coordinate {
        private final int xPos;
        private final int yPos;
        private final boolean traversable;
        private boolean traversed = false;

        public Coordinate(int x, int y, boolean traversable) {
            this.xPos = x;
            this.yPos = y;
            this.traversable = traversable;
        }

        public int getXPosition() {
            return this.xPos;
        }

        public int getYPosition() {
            return this.yPos;
        }

        public boolean isTraversable() {
            return this.traversable;
        }

        public boolean isTraversed() {
            return this.traversed;
        }

        public void markAsTraversed() {
            this.traversed = true;
        }

        public boolean equals(Coordinate coord) {
            return (coord.getXPosition() == this.xPos 
                    && coord.getYPosition() == this.yPos
                    && coord.isTraversable() == this.traversable);
        }
    }

    private static class RasterizedMap {
        private final Coordinate[][] mapData;

        public RasterizedMap(boolean[][] mapMatrix) {
            this.mapData = new Coordinate[mapMatrix.length][mapMatrix[0].length];
            for (int y = 0; y < mapMatrix.length; y++) {
                Coordinate[] row = new Coordinate[mapMatrix[0].length];
                for (int x = 0; x < mapMatrix[0].length; x++) {
                    row[x] = new Coordinate(x, y, mapMatrix[y][x]);
                }
                this.mapData[y] = row;
            }
        }

        public int xRange() {
            return this.mapData[0].length;
        }

        public int yRange() {
            return this.mapData.length;
        }

        public Coordinate getCoordinate(int x, int y) {
            return this.mapData[y][x];
        }

        public Stack<Coordinate> validAdjacentCoordinates(Coordinate cursor) {
            Stack<Coordinate> adjacentCoordinates = new Stack<>();
            int cursorX = cursor.getXPosition();
            int cursorY = cursor.getYPosition();
            Coordinate checkCoordinate;
            if (cursorY > 0) {
                checkCoordinate = this.getCoordinate(cursorX, cursorY - 1);
                if (checkCoordinate.isTraversable() && !checkCoordinate.isTraversed()) {
                    adjacentCoordinates.push(checkCoordinate);
                }
            }
            if (cursorY < this.yRange() - 1) {
                checkCoordinate = this.getCoordinate(cursorX, cursorY + 1);
                if (checkCoordinate.isTraversable() && !checkCoordinate.isTraversed()) {
                    adjacentCoordinates.push(checkCoordinate);
                }
            }
            if (cursorX > 0) {
                checkCoordinate = this.getCoordinate(cursorX - 1, cursorY);
                if (checkCoordinate.isTraversable() && !checkCoordinate.isTraversed()) {
                    adjacentCoordinates.push(checkCoordinate);
                }
            }
            if (cursorX < this.xRange() - 1) {
                checkCoordinate = this.getCoordinate(cursorX + 1, cursorY);
                if (checkCoordinate.isTraversable() && !checkCoordinate.isTraversed()) {
                    adjacentCoordinates.push(checkCoordinate);
                }
            }
            return adjacentCoordinates;
        }
    }

    private static RasterizedMap routeMap;

    public static boolean routeExists(int fromRow, int fromColumn, int toRow, int toColumn, boolean[][] mapMatrix) {
        routeMap = new RasterizedMap(mapMatrix);
        Coordinate cursor = routeMap.getCoordinate(fromColumn, fromRow);
        cursor.markAsTraversed();
        Coordinate destination = routeMap.getCoordinate(toColumn, toRow);
        if (!cursor.traversable || !destination.traversable) {
            return false;
        }
        Stack<Coordinate> tangents = routeMap.validAdjacentCoordinates(cursor);
        while (!tangents.empty()) {
            cursor = tangents.pop();
            cursor.markAsTraversed();
            if (cursor.equals(destination)) return true;
            Stack<Coordinate> newTangents = routeMap.validAdjacentCoordinates(cursor);
            while (!newTangents.empty()) tangents.push(newTangents.pop());
        }
        return false;
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
