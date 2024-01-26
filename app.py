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

calc="1 + 2"
result = eval(calc)
print("The result of the calculation is: ", result)
stringInterpret=result
print("The result of the calculation is: ", stringInterpret, type(stringInterpret))

import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_countAlpha(self):
        self.assertEqual(countAlpha, 12)
    
    def test_countFloat(self):
        self.assertEqual(type(countFloat), type(float()))
        
    def test_pi(self):
        self.assertEqual(3.14, roundPi)
    
    def test_reversed(self):
        self.assertEqual(reversedText, ['!', ' ', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H'])
    
    def test_age(self):
        self.assertEqual(type(age), type(str()))
        
    def test_sorted(self):
        self.assertEqual(sortNum, [1, 2, 3, 4, 6, 7, 8])
    
    def test_sum(self):
        self.assertEqual(sumOfList, 31)
    
    def test_min(self):
        self.assertEqual(minValue, 1)
    
    def test_max(self):
        self.assertEqual(maxValue, 8)
    
unittest.main(argv=[''], verbosity=2, exit=False)
if __name__ == "__main__":
    app.run(debug=True)



