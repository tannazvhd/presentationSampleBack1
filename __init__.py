from flask import Flask
from flask_cors import CORS

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True) 



CORS(app)



from app import routes