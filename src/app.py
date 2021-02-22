import os

from flask import Flask, request, g, session, redirect, url_for, render_template
from flask_github import GitHub

from fork import forktherepo


app = Flask(__name__)
app.config.from_object('conf.PrdConf')
github = GitHub(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def hello_world():
    return {'status': 'success'}


@app.route('/login')
def login():
    return github.authorize(
        scope='user,repo',
    )


@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        print("authorization failed.")
        return redirect('retry')

    forktherepo(oauth_token=oauth_token)

    return redirect('success')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/retry')
def retry():
    return render_template('retry.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))