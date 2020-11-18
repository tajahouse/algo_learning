const [weight] = useState(0)
const [height] = useState(0) 
const [bmi, setBMI] = useState(0)// These are just what I assume you have, but this is the state of your weight and height

const evaluateBMI = (weight, height) =>{
    user_bmi = 703 * (weight/height)
    setBMI(user_bmi)
} // This would be your function

const clickHandler = (e) =>{
    e.preventDefault()
    evaluateBMI(weight, height) //here is where you would use your function
}

<form>
    <button onClick = {clickHandler}> BMI </button>
</form>