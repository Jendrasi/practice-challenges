'''
This function encapsulates the top down recursive method of solving this problem. It first recursively populates a decision tree with __appendChildren(p,d), then finds the shortest path from the top node to a leaf in a separate recursive traversal. The shortest path algorithm is abstracted away in the custom Node class.
'''
def __topDown(amt, denom):

    from node import Node

    '''
    Recursive function to build out a decision tree from a top node and series of denominations. The top node/parent has the total amount we intend to optimally make with the denominations.
    # NOTE: Since the parent is actually passed as a memory address, it can be accessed and modified directly, like a pointer. No returning the final tree into a new object.
    # !: Warning that this part of the top down recursive solution is exponentially memory hungry with higher starting amounts and lists of denominations. Hoping to improve this.
    '''
    def __appendChildren(parent, denom):
        for d in denom:
            if d <= parent.amount:
                childAmt = parent.amount - d
                child = Node(childAmt)
                if childAmt > 0:
                    __appendChildren(child, denom)
                parent.addChild(child)
            else:
                break

    '''
    Node.getMinDepth() returns the shortest path to a leaf, as a list of descending amounts as coins are subtracted. To get which coins were used, just subtract n+1 from n across the list.
    # Ex: [6,2,1,0] -> [4,1,1]
    # NOTE: The path p is expected to already be sorted in descending order the way it came from getMinDepth()
    '''
    def __pathToCoins(p):
        # path.sort(reverse=true)
        coins = []
        for i in range(len(p)-1):
            coins.append(p[i]-p[i+1])
        return coins

    # Initialize tree as a top node
    tree = Node(amt)
    # Populate it's children and their children recursively
    # !: This part could use optimization.
    __appendChildren(tree, denom)
    # Recursively traverse tree from top Node to find shortest path to a leaf
    path = tree.getMinDepth()
    # Convert the descending amounts in the shortest path to a list of coins
    return __pathToCoins(path)


'''
This function encapsulates the bottom up iterative method of solving this problem. It does all the work in a one dimensional list with a length of amount + 1. For each index i, the value becomes a list of the best coins to make i. This builds on the knowledge of how to make base cases 0 and 1, like a mathematical proof. It is well optimized and does not redo any work.
'''
def __bottomUp(amt, denom):
    # Create an example starting 'solution' that will always be beaten... A list of 1 dollar coins.
    absMaxCoins = [1]*(amt + 1)
    # The table at index 0 is an empty list. This represents an accepted base case, that you can make an amount of i=0 with 0 coins.
    table = [[]] + [absMaxCoins]*amt
    
    # Iterate the table.
    for i in range(len(table)):
        # Skip zero-th entry (base case).
        if i > 0:
            # Try to subtract every denomination that fits into i.
            for coin in denom:
                if coin <= i:
                    # Take the known best combination at table[i-coin], and add the coin to it to make a possible 'best' combination to make i.
                    subComb = table[i-coin]
                    # If the new list of coins is shorter than the previous solution to make i, replace it at table[i].
                    if (len(subComb)+1) < len(table[i]):
                        table[i] = subComb+[coin]
    # By the time the table is iterated, the final index will contain the minimal combination of coins to make the amount.
    return table[-1]


'''
Publicly visible function to execute the problem, given an amount, denomination list, and strategy (1 for 'topDownRecursive' or 0 for 'bottomUpIterative').
'''
def minimumChange(amt, denom, strat):
    # __topDown().__appendChildren() assumes that the denomations will be sorted in ascending order to save a few unnecessary if checks. So denominations list is presorted.
    denom.sort()
    # Execute the requested strategy and return the result as a minimal list of coins.
    if strat:
        return __topDown(amt, denom)
    else:
        return __bottomUp(amt, denom)


'''
Publicly visible function to print a formatted solution.
'''
def printSolution(solution):
    output = 'The minimal change is '
    amt = 0
    for coin in solution:
        output += str(coin) + ' + '
        amt += coin
    print(output[:-2] + '= ' + str(amt))


'''
Main execution
# NOTE: Commented out execution time because this method of measuring performance is not very scientific. Not accurate or precise, especially on Windows.
'''
if __name__ == "__main__":
    from ast import literal_eval
    from sys import argv, exit
    # import time

    # Input validation
    # args = argv
    argErr = "Bad arguments\nUsage: python change.py amountInteger denomList [topDown|bottomUp]"
    # ...check min number of args
    if len(argv) < 3:
        exit(argErr)
    # ...get amount
    a = argv[1]
    if not a.isnumeric():
        exit("Amount is not an integer.")
    a = int(a)
    # ...get denominations
    d = argv[2]
    try:
        d = literal_eval(d)
    except:
        exit("Couldn't parse denominations.")
    if isinstance(d, list):
        d = list(dict.fromkeys(d))
        d.sort()
    else:
        exit("Denominations are not recognized as a list.")
    # ...get algorithm strategy
    strategy = 0
    if len(argv) > 3:
        if argv[3] == "topDown":
            strategy = 1
        elif argv[3] != "bottomUp":
            exit("Optional algorithm strategy not recognized.")

    # Pre-run user validation of input
    if strategy:
        print("Algorithm strategy is top down recursive.")
    else:
        print("Algorithm strategy is bottom up iterative.")
    print("Amount is",a)
    print("Denominations are:")
    print(*d,sep=', ')
    
    # Execution Time
    # startT = time.time_ns()

    # Execute
    # solution = minimumChange(24,[5,2,1],1)
    solution = minimumChange(a,d,strategy)

    # Execution Time (cont.)
    # endT = time.time_ns()

    # Final Solution
    # print(solution)
    printSolution(solution)

    # Execution Time (fin.)
    # print("Algorithm Execution Time: %s milliseconds" % ((endT-startT)/1000000))
