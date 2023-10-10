import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Returns hello + <name>
# Try it:
#   ; curl "http://localhost:5001/greet?name=David"
@app.route('/greet', methods=['GET'])
def hello():
    name = request.args['name'] 
    # Send back a friendly greeting with the name
    return f"Hello {name}!\n"

# Note: body parameters cannot go in the url like in the above example
# Try it: curl -X POST -d "person=kay" "http://localhost:5001/hello"
@app.route('/hello', methods=['POST'])
def post_greet():
    name = request.form['person']
    return f"Hello {name}!\n"

# Try it: curl -X POST -d "person=Ket&message=Hello World" "http://localhost:5001/hello_web"
@app.route('/hello_web', methods=['POST'])
def hello_web():
    name = request.form['person']
    message = request.form['message']
    return f"Thanks {name}, you sent this message: {message}\n"

#  curl "http://localhost:5001/wave?name=Ket"
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f"Hello {name}!\n"


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

