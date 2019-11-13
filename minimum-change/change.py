import sys
import ast

def __topDown(amt, denom):
    return 0

def __bottomUp(amt, denom):
    # This base combination for each table index represents a worst possible solution
    absMaxCoins = [1]*(amt + 1)
    table = [[]] + [absMaxCoins]*amt
    
    # Each index in this one dimensional table represents a combination of coins that adds up to the value of its index. The goal is to get the minimum coins for every one, building to the total amount. The last member of the table represents the total amount.
    for i in range(len(table)):
        # Skip zero-th entry (base case)
        if i > 0:
            # Try every possible coin
            for coin in denom:
                # Ignore coin if it is too big to fit into the sub amount
                if coin <= i:
                    subComb = table[i-coin]
                    if (len(subComb)+1) < len(table[i]):
                        table[i] = subComb+[coin]
    return table[-1]

def minimumChange(amt, denom, strat):
    if strat:
        return __topDown(amt, denom)
    else:
        return __bottomUp(amt, denom)

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
        d = list(dict.fromkeys(d))
        d.sort()
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
    # solution = minimumChange(6,[4,3,1],0)
    solution = minimumChange(a,d,strategy)

    # Final Solution
    print(solution)
    # printSolution(solution)