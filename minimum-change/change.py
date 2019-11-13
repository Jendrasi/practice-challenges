import sys
import ast

def __topDown(amt, denom):
    return 0

def __bottomUp(amt, denom):
    return 0

def minimumChange(amt, denom, strat):
    return 0

def printSolution(solution):
    return 0

if __name__ == "__main__":
    # Input validation
    args = sys.argv
    argErr = "Bad arguments\nUsage: python change.py amountInteger denomList [topDown|bottomUp]"
    # ...check min number of args
    if len(args) < 3:
        sys.exit(argErr)
    # ...get amount
    a = args[1]
    if not a.isnumeric():
        sys.exit("Amount is not an integer.")
    a = int(a)
    # ...get denominations
    d = args[2]
    try:
        d = ast.literal_eval(d)
    except:
        sys.exit("Couldn't parse denominations.")
    if isinstance(d, list):
        d = set(d)
    else:
        sys.exit("Denominations are not recognized as a list.")
    # ...get algorithm strategy
    strategy = 0
    if len(args) > 3:
        if args[3] == "topDown":
            strategy = 1
        elif args[3] != "bottomUp":
            sys.exit("Optional algorithm strategy not recognized.")

    # Pre-run user validation of input
    if strategy:
        print("Algorithm strategy is top down recursive.")
    else:
        print("Algorithm strategy is bottom up iterative.")
    print("Amount is",a)
    print("Denominations are:")
    print(*d,sep=', ')

    # Execute
    # solution = minimumChange(a,d,strategy)

    # Final Solution
    # printSolution(solution)