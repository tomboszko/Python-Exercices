from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

print("Starting the Flask application...")

age = input("How old are you?")
print("Your age", age)

if __name__ == "__main__":
    app.run(debug=True)

age = input("How old are you?")
print("Your age", age)

