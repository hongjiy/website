from flask import Flask, render_template
from github_webhook import Webhook

app = Flask(__name__)
#webhook = Webhook(app)


@app.route('/')
def index():
	return render_template('index.html')


# @webhook.hook()
# def on_push(data):
# 	print("Got push with: {0}".format(data))

@app.route('/postreceive', method=['POST'])
def on_push():
	print('got note')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, threaded=True, debug=False)
