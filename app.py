from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

print("Starting the Flask application...")

countAlpha = len("Hello world!")
print("The number of characters in the string 'Hello world!' is: ", countAlpha)

countFloat = float(countAlpha)
print("The float value of countAlpha is: ", countFloat)

import math

pi = math.pi
roundPi = round(pi, 2)
print("The value of pi is: ", pi)

reversedText = list("Hello world!"[::-1])

print("The number of characters in the string 'Hello world!' is: ", countAlpha)

countFloat = float(countAlpha)
print("The float value of countAlpha is: ", countFloat)

import math

pi = math.pi
roundPi = round(pi, 2)
print("The value of pi is: ", pi)

reversedText = list("Hello world!"[::-1])
print("The reversed string is: ", reversedText)


##age=int(input("Enter your age: "))
##print("Your age is: ",age, type(age))

num = [2, 8, 1, 4, 6, 3, 7] 
sortNum = sorted(num)
print("The sorted list is: ", sortNum)
sumOfList=sum(num)
print("The sum of the list is: ", sumOfList)
minValue=min(num)
print("The minimum value of the list is: ", minValue)
maxValue=max(num)
print("The maximum value of the list is: ", maxValue)



if __name__ == "__main__":
    app.run(debug=True)



