/*
After some time away from coding this is one of many basic practice exercises. Not challenges.
Just getting back to it.
Fibonnaci sequences

Temporary Note: For now, just treat the whole file as a main function and play around.
But I installed minimist to play with cmd args to run different functions.
Like recursive fib or iterative fib. A help command would also be neat.
*/

const { stdout } = require('node:process');

/*
Print 'i' digits of fibonnaci sequence using iterative method. If i is not populated, return error.
*/
function fibIter(i) {
    if (i === undefined || i < 1) {
        throw new Error(`${getFunctionName()} expects a number greater than 0 as an argument.`);
    }
    console.log(`Printing ${i} numbers of a Fibonacci sequence (iteratively)...`);
    let fib = 1;
    let fibPrev = 0;
    for (let iter = 1; iter <= i; iter++) {
        stdout.write(`${fib} `);
        let newFib = fib + fibPrev;
        fibPrev = fib;
        fib = newFib;
    }
    stdout.write(`\n...Done\n`);
}

/*
Print 'i' digits of fibonnaci sequence using recursive method. If i is not populated, return error.
*/
function fibRecursive(i) {

}

/*
Use this helper to clarify the function name while covering unexpected usage errors.
*/
function getFunctionName() {
    return getFunctionName.caller.name;
}

fibIter(30);