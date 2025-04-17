import os

from website import create_app
# Login
# Sign up


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
