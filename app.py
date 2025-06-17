from flask import Flask
app = Flask(__name__)

# This creates a WSGI appllication (Web service global interface)

@app.route('/') # --> Root Web URL
def welcome():
    return "Welcome to my first learning and I have set debug = True and I just noticed that it works."

@app.route('/second-page')
def second_page():
    return "This is the second page of the application."

if __name__ == "__main__":
    # Debug = True mentions that server didn't have to restart everytime the changes are made inside the codebase
    app.run(debug=True)