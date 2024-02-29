const hello = 'Hello world!';
console.log(hello);

// Different types
let age = 6; //number type
let happy = true; //boolean type
let feeling = 'excited'; //string type

// Clarifying type in array functions
const circleArea = (diameter: number) => {
    return diameter * Math.PI;
};
console.log(circleArea(2));

// Arrays
let products = ['laptop', 'backpack', 'keyboard', 'water bottle', 'notebook'];
products.push('colored pencils');
//products.push(10); Doesn't work...unless
let colors = ['yellow', 123456, 'f32e89', 'white']; // Initialized as such

// Objects
let ramen = {
    cuisine: 'asian',
    ingredients: ['broth', 'noodles', 'soft boiled egg', 'aromatic oil', 'scallions',
                'fried garlic', 'fried shallots', 'fried ginger'],
    rating: 5,
    hot: true
}; // Can't change type of properties or add properties after intializing
console.log(ramen);

// Initializing with type
let exists: boolean; // Now it's undefined
exists = true;
console.log(exists);

let countries: string[] = []; // This isn't undefined, initialized as empty array
console.log(countries);
countries.push('Nepal');
console.log(countries);

let userInputNumbers: (string|number)[] = []; // This can be either type specified
userInputNumbers.push(30);
userInputNumbers.push("one hundred");
console.log(userInputNumbers);

let _id: string|number; // parentheses not needed if array brackets not in use
_id = 209348;
_id = '9gr8s0';

let anyObject: object;
anyObject = {name: 'Matt', age: 29};
anyObject = ['Matt']; // An array is still an object
console.log(anyObject);
let personObject: {
    name: string,
    age: number
} // Can pre-specify the object schema. Here it's undefined
personObject = {
    name: 'Abhinav',
    age: 35
};
console.log(personObject);

let userInputAny: any = 4; // You can allow a variable to be any type.
userInputAny = 'hello';
userInputAny = true; // Though this kind of ignores the benefits of TS.
let anyArray: any[] = []; // You could do the same with arrays.
anyArray.push(1);
anyArray.push('one');
anyArray.push(true);
console.log(anyArray);

// Functions
let speakTheirLanguage: Function;

speakTheirLanguage = () => {
    console.log('felicitations, malefactors!');
}

const power = (x: number, p: number = 2, comment?: string): number => {
    //Could infer the return type there at the end of above line.
    //Not super necessary but can make things more readable.
    if (comment != undefined) {
        console.log(comment);
    }
    return x**p;
}
console.log(power(2));
console.log(power(2,3));
console.log(power(2,4,"powering up!"));
/* There doesn't seem to be a way to explicitly use one latter optional
parameter without using the previous. In this case you would probably want
to use an options object (options = {}) or maybe a 'rest parameter' (arg1, ...options)
which will make a list called options available in the function block. */

// Type Aliases

type strnum = string | number;
const printAThing = (thing: strnum) => {
    console.log(thing);
}
type user = {name: string, email: string, uid: strnum}

// Function signatures (kind of like an interface)

let hypotenuse: (a: number, b: number) => number; // can't be a const since the signature isn't initialized
hypotenuse = (a: number, bnum: number) => { //changed one of the arg names to show it is allowed
    return Math.sqrt(a**2 + bnum**2);
}
console.log(hypotenuse(1, 1));