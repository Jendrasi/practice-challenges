//const form = document.querySelector('.add-form')!;
//! tells TS that this won't be null, emphasizes that we know it exists.
//Alternatively we could do a check for not null
//if (form) {
//
//}

const form = document.querySelector('.add-form') as HTMLFormElement;
//in this case it's cast as a form element, in typescript.
//but when compiled could still get null if the thing doesn't actually exist
//so why is this useful? Well, it suppresses errors like with '!',
//but also gives IDE context aware properties/methods
if (form) {
    console.log("form exists");
    console.log(form);
} else {
    console.log("form doesn't exist");
    console.log(form);
}
const num1 = document.querySelector('#num1') as HTMLInputElement;
const num2 = document.querySelector('#num2') as HTMLInputElement;
const result = document.querySelector('#result') as HTMLInputElement;

form.addEventListener('submit', (e: Event) => {
    /*
    the submit event is fired on HTMLFormElement
    it fires when the form is submitted
    the form is said to have been submitted when:
      - the user clicks a nested submit button
        ...that is, any <button> (default type is "submit")
        ...input field with type="submit" which is rendered like a basic button
        ...input field with type="image" which can render graphical clickable submit buttons
      - or when the user presses enter while context is in any nested field
      - or when a script calls form.requestSubmit()
    */
    e.preventDefault(); // this suppresses form behavior that refreshes page on submit
    result.valueAsNumber = num1.valueAsNumber + num2.valueAsNumber;
});