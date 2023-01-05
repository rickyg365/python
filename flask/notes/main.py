from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


# Variables
@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

# Json
@app.route('/json_data/')
def json():
    return jsonify({
        "name": "Test Name",
        "id": "123"
    })

# Before Request
@app.before_request
def before():
    app.logger.info('This is an INFO message')
    print("This is executed BEFORE each request.")
    
# Access request data
"""
request.data → Access incoming request data as a string

request.args → Access the parsed URL parameters. 
Returns ImmutableMultiDict

request.form → Access the form parameters. 
Return ImmutableMultiDict

request.values → Returns CombinedMultiDict that combines args and form

request.json → Returns parsed JSON data if mimetype is application/json

request.files → Returns MultiDict object which contains all uploaded files. 
Each key is the name of the file and the value is the FileStorage object.

request.authorization → Returns an object of Authorization class. 
It represents an Authorization header sent by the client.
"""

# Blueprints
from home import home_bp
from contact import contact_bp

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')


# Logging
# app.logger.debug('This is a DEBUG message')
app.logger.info('This is an INFO message')
# app.logger.warning('This is a WARNING message')
# app.logger.error('This is an ERROR message')



if __name__ == '__main__':
    """
    The default value for host is localhost or 127.0.0.1
    host specifies the server on which we want our flask application to run. 

    0.0.0.0 means “all IPv4 addresses on the local machine”. 
    This ensures that the server will be reachable from all addresses.
    
    The parameter port to use the port number of your choice.
    The default port value is 5000

    debug → If the debug parameter is set to True then the server will automatically reload on code changes and show an interactive debugger in case of unhandled exceptions. 
    The default is False

    use_reloader → When use_reloader is set to True, the server will automatically restart when the code changes. 
    Defaults to False

    threaded → When threaded is set to True, the process will handle each request in a separate thread. 
    Default is False

    ssl_context → SSL Context for the connection. Expects ssl.SSLContext , a tuple in the form (cert_file, pkey_file) , or the string 'adhoc' if the server should automatically create the context. 
    Default is None i.e. SSL is disabled.
    This is used when we want to host the Flask application on HTTPS instead of HTTP.
    
    """
    # DEFAULT: HOST=127.0.0.1  PORT=5000
    app.run()
    # app.run(host='0.0.0.0', port=105)