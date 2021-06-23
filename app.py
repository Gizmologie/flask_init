from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

book = [
    {
        'id': 1,
        'titre': 'un titre',
    },
    {
        'id': 2,
        'titre': 'un autre titre random',
    }
]


@app.route("/")
def index():
    return 'hello myapp'


@app.route('/api/book')
def books():
    return jsonify(book)


@app.route('/book/id/<id>')
def books_id(id):
    return jsonify(list(filter(lambda x: x['id'] == int(id), book)))


@app.route('/book/name/<titre>')
def books_name(titre):
    return jsonify(list(filter(lambda x: x['titre'] == titre, book)))


if __name__ == '__main__':
    app.run(debug=True)
