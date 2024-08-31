import opencc
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}

SCHEMES = [
    "s2t",
    "t2s",
    "s2tw",
    "tw2s",
    "s2hk",
    "hk2s",
    "s2twp",
    "tw2sp",
    "t2tw",
    "t2hk",
]


@app.route('/<path:_type>', methods=['POST'])
def convert(_type):
    if _type not in SCHEMES:
        _type = "t2s"

    try:
        cc = opencc.OpenCC(f'{_type}.json')
        title = cc.convert(request.form.get('title', ''))
        content = cc.convert(request.form.get('content', ''))
        return jsonify({
            'title': title,
            'content': content,
        }), 200
    except Exception as e:
        app.logger.error(f"Error during conversion: {e}")
        return jsonify({
            'title': 'Error occurred',
            'content': 'An unexpected error occurred.',
        }), 500


@app.route('/', methods=['GET'])
def redirect_to_github():
    return redirect('https://github.com/LandonLi/YA-OpenCC-API', code=301)


if __name__ == '__main__':
    app.run(debug=False)
