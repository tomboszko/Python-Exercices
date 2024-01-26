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

if __name__ == "__main__":
    app.run(debug=True)



