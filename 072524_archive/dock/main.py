import os
from flask import Flask

"""

"""


app = Flask(__name__)

@app.route('/')
def program():
    return 'Program Running'

if __name__ == "__main__":
    # Need host to run in external server
    app.run(host="0.0.0.0", port=5000)
