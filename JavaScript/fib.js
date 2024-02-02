/*
After some time away from coding this is one of many basic practice exercises. Not challenges.
Just getting back to it.
Fibonnaci Sequences

Temporary Note: For now, just treat the whole file as a main function and play around.
But I installed minimist to play with cmd args to run different functions.
Like recursive fib or iterative fib. A help command would also be neat.
*/

/*
Print 'i' digits of fibonnaci sequence using iterative method. If i is not populated, return error.
*/
function fibIter(i) {
    if (i === undefined) {
        let func = getFunctionName();
        throw new Error(`${func} expects an argument.`);
    }
}

/*
Print 'i' digits of fibonnaci sequence using recursive method. If i is not populated, return error.
*/
function fibRecursive(i) {

}

/*
I thought it'd be fun to cover unexpected usage of functions with error messages that clarify the name with this helper.
*/
function getFunctionName() {
    return getFunctionName.caller.name;
}

fibIter();