# redirect  --> is for redirection from some specific webpage based on conditions.
#url_for    --> For creating URL dynamically

from flask import Flask, redirect, url_for
app = Flask(__name__)

# This creates a WSGI application (Web service global interface)

@app.route('/') # --> Root Web URL
def welcome():
    return "Welcome Page this is."

@app.route('/success/<int:score>')                  # --> Notice the parameter in the <URL/datatype:variable>
def success(score):
    return "The person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')                     # --> Notice the parameter in the <URL/datatype:variable>
def fail(score):
    return "The person has failed and the marks is " + str(score)

# A result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks>=70:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for( result, score = marks ))  #  --> Dynamically allocated the other URLs based on the conditions.

if __name__ == "__main__":
    # Debug = True mentions that the server doesn't have to restart every time the changes are made inside the codebase
    app.run(debug=True) 