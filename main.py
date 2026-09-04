from pyscript import document

def calculate(event):

    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)

    operation = document.querySelector("#operation").value

    if operation == "+":
        answer= num1+num2

    elif operation == "-":
        answer= num1-num2

    elif operation == "x":
        answer= num1*num2

    elif operation == "/":
        
        if num2 == 0:
            document.querySelector("#result").innerText = "Cannot divide by zero."
            return 
        answer= num1/num2

    document.querySelector("#result").innerText = "Result: " + str(answer)