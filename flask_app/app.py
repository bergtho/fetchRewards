from flask import Flask
import os

app = Flask(__name__)

### endpoints
@app.route('/')
def hello():
    return '<h1>Hello, World</h1>'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format('The word is: ' + word)


### errors (need to read about these)
#@app.errorhandler(404)
#def not_found(error):
    # need to make import statement:
    # from flask import Flask, jsonify, make_response

    #      need to lookup, to json,                       error code
#    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
#    app.run(debug=True)
#    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0")
#    app.run(port=5000)

