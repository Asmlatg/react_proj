from flask import Flask, request, jsonify
from markupsafe import escape
from flask_restful import Api, Resource

app = Flask(__name__)

dic = {
    "From": "French",
    "To": "English"
}


@app.route("/")
def show_list():
    return dic


@app.route('/add', methods=['POST'])
def add_word():
    data = request.get_json()
    if 'word' in data and 'translation' in data:
        word = data['word']
        translation = data['translation']
        dic[word] = translation
        return f"Added '{word}' with translation '{translation}' to the dictionary."
    else:
        return "Please provide 'word' and 'translation' in the request body.", 400


@app.route('/del', methods=['DELETE'])
def delete_word():
    data = request.get_json()
    if 'word' in data:
        word = data['word']
        if word in dic:
            del dic[word]
            return f"Deleted '{word}' from the dictionary."
        else:
            return f"'{word}' not found in the dictionary.", 404
    else:
        return "Please provide 'word' in the request body.", 400


if __name__ == '__main__':
    app.run()
