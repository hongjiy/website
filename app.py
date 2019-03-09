from flask import Flask, render_template, request
import json
import git
import os
import logging

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/postreceive', methods=['POST'])
def on_push():
	data = request.get_json()
	print('New commit received: ', data['head_commit']['id'])
	g = git.cmd.Git(os.getcwd())
	g.pull()
	print('codebase update: successful')
	return json.dumps(('', 200))


if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
