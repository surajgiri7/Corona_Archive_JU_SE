from distutils.log import debug
from corona import app

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host="134.102.121.112", debug=True, ssl_context='adhoc')
    app.run(host="localhost", port=8000, debug=True)

#this file is used for running the program