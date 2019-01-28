from flask import Flask, render_template, request

app = Flask(__name__)


users = ['Svend Andreas', 'Walter', 'Per', 'Grethe']


@app.route('/')
def root():
    return render_template('index.html', users=users)


@app.route('/artikkel', methods=['POST'])
def post_form():
    return render_template('response.html', **request.form)


if __name__ == '__main__':
    app.run(debug=True)
