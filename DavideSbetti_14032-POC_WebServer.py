from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/check_post', methods=['POST'])
def check_post():
	print("Test")
	return jsonify("A response from Python")

if __name__ == "__main__":
    app.run()