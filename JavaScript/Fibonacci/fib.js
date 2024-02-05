/*
After some time away from coding this is one of many basic practice exercises. Not challenges.
Just getting back to it.
Fibonnaci sequences

Temporary Note: For now, just treat the whole file as a main function and play around.
But I installed minimist to play with cmd args to run different functions.
Like recursive fib or iterative fib. A help command would also be neat.
Also, learn how to unit test in JS and write a couple for this class.
*/

const { stdout } = require('node:process');
const badInputError = (funcName) => { return new Error(`${funcName} expects a number greater than 0 as an argument.`)};

/*
Print 'i' digits of fibonnaci sequence using iterative method. If i is not populated, return error.
*/
function fibIterative(i) {
    if (i === undefined || i < 1) {
        throw badInputError(getFunctionName());
    }
    console.log(`Printing ${i} numbers of a Fibonacci sequence (iteratively)...`);
    let fib = 0;
    let nextFib = 1;
    for (let iter = 1; iter <= i; iter++) {
        stdout.write(`${fib} `);
        let newFib = fib + nextFib;
        fib = nextFib;
        nextFib = newFib;
    }
    stdout.write(`\n...Done\n`);
}

/*
Print 'i' digits of fibonnaci sequence using recursive method. If i is not populated, return error.
The rules I set for myself was to see if I could print the whole sequence, not just the n-th, WITHOUT looping.
I came across a solution while trying to resolve the efficiency issue.
The fibCache that resolves that issue happens to have the ordered list of fibs after the n-th is generated.
*/
function fibRecursive(i) {
    if (i === undefined || i < 1) {
        throw badInputError(getFunctionName());
    }
    console.log(`Printing ${i} numbers of a Fibonacci sequence (recursively)...`);

    let fibCache = [0];
    const getFib = (x) => {
        if (x == 2 && fibCache.length == 1) {
            fibCache.push(1);
            return 1;
        } else if (fibCache.length >= x) {
            return fibCache[x - 1];
        } else {
            let nFib = getFib(x - 1) + getFib(x - 2);
            fibCache.push(nFib);
            return nFib;
        }
    };

    // This will return the n-th fib on it's own...but with the fibCache which makes the algo more efficient...
    getFib(i);
    // You also have a record of every fib up to it!
    console.log(fibCache.join(" "));
    
    stdout.write(`...Done\n`);
}

/*
Use this helper to clarify the function name while covering unexpected usage errors.
*/
function getFunctionName() {
    return getFunctionName.caller.name;
}

fibIterative(30);
fibRecursive(30);