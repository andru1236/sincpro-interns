from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "!hola "


## @app.route('/exercise', methods=['GET'])
## def index():
##   nombreUser = request.args.get('nombreUser')
##   return nombreUser

if __name__ == "__main__":
    app.run(host='0.0.0.0')
