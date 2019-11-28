import sys
import ast

def __replaceLowestDups(stones):
    replaced = []
    for i, s in enumerate(stones):
        # If the current index has a duplicate in the next index of the sorted list...
        if s == stones[i+1]:
            # Assuming there may be more duplicates, what is the number?
            dupNum = stones.count(s)
            # Add earlier indexes to the answer.
            replaced += stones[:i]
            # If there is an odd number of duplicate values...
            if dupNum%2 == 1:
                # First add one entry of s
                replaced.append(s)
            # Now add half of the remaining duplicates, at level +1
            addition = [s+1] * int(dupNum/2)
            # Now add the remainder of the list
            replaced += addition + stones[(i+dupNum):]
            # The lowest duplicate values have been replaced. Now return the solution.
            return replaced
        # If there weren't duplicates here, move on in for loop

def magic(stones):
    solution = stones
    solution.sort()

    # We know the solution is ready when it is effectively a set
    # WHILE there are still duplicates anywhere in the list
    while solution != list(dict.fromkeys(solution)):
        solution = __replaceLowestDups(solution)
        # NOTE If there are no duplicates after this operation, the while loop will close

    return solution

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Provide integer list as argument.")
    else:
        input = sys.argv[1]
        input = ast.literal_eval(input)
        # input = [1,2,3,1]
        solution = magic(input)
        print("Minimized stones:")
        print(*solution, sep=", ")
        print("Amount is",len(solution))