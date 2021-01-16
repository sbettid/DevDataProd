from flask import Flask, render_template, jsonify, request
from DavideSbetti_14032_ModelApp import ModelApp 
from DavideSbetti_14032_AnsweringModule import AnsweringModule

app = Flask(__name__)

myModel = ModelApp("model")
am = AnsweringModule("exampleRules.json")

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/check_post', methods=['POST'])
def check_post():
	text = request.form["post"]
	classification = myModel.classifyPost(text)
	if classification > 0:
		answer = am.answerPost(text, classification)
		return jsonify(classification=classification, answer=answer)
	else:	
		return jsonify(classification=classification)

if __name__ == "__main__":
    app.run()