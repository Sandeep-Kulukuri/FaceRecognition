from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/exec')
def parse(name=None):
    import faces
    return render_template('index.html', name=name)


@app.route('/exec2')
def parse1(name=None):
    import faces_train
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()
    app.debug = True
