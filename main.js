

const submitButton = document.getElementById('submit-button')

submitButton.addEventListener('click', (e) => {
    e.preventDefault()
    console.log("clicked")

})
function sayHello() {
    console.log("hello world")
}
sayHello()