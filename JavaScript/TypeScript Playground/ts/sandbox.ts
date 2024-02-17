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
console.log(exists);
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
let personObject: {
    name: string,
    age: number
} // Can pre-specify the object schema
personObject = {
    name: 'Abhinav',
    age: 35
};