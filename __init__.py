from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route("/")  # this sets the route to this page
def home():
	return jsonify({'Message': "This app is run on a Linux Server hosted in AWS!"})

if __name__ == "__main__":
    app.run()
