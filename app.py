from flask import Flask, render_template, request
import git
import os

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/postreceive', methods=['POST'])
def on_push():
	data = request.form
	print(data)
	g = git.cmd.Git(os.getcwd())
	g.pull()


	return 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
