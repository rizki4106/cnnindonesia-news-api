from flask import Flask, jsonify, request
app = Flask(__name__)

# import module from ./src
from src import Code

@app.route('/')
def home():
    return jsonify({
        "status": 200,
        "length": len(Code.index()),
        "data": Code.index()
    }), 200
@app.route('/nasional')
def nasional():
    return jsonify({
        "status": 200,
        "length": len(Code.nasional()),
        "data": Code.nasional()
    }), 200

@app.route('/internasional')
def internasional():
    return jsonify({
        "status": 200,
        "length": len(Code.internasional()),
        "data": Code.internasional()
    }), 200

@app.route('/ekonomi')
def ekonomi():
    return jsonify({
        "status": 200,
        "length": len(Code.ekonomi()),
        "data": Code.ekonomi()
    }), 200

@app.route('/olahraga')
def olahraga():
    return jsonify({
        "status": 200,
        "length": len(Code.olahraga()),
        "data": Code.olahraga()
    }), 200

@app.route('/teknologi')
def teknologi():
    return jsonify({
        "status": 200,
        "length": len(Code.teknologi()),
        "data": Code.teknologi()
    }), 200

@app.route('/hiburan')
def hiburan():
    return jsonify({
        "status": 200,
        "length": len(Code.hiburan()),
        "data": Code.hiburan()
    }), 200
@app.route('/gaya-hidup')
def social():
    return jsonify({
        "status": 200,
        "length": len(Code.social()),
        "data": Code.social()
    }), 200

@app.route('/detail/')
def detail():
    url = request.args.get('url')
    print(url)
    return jsonify({
        "status": 200,
        "data": Code.detail(url)
    }), 200

@app.route('/search/')
def search():
    param = request.args.get('q')
    return jsonify({
        "status": 200,
        "data": Code.search(param),
        "length": len(Code.search(param))
    }), 200


if __name__ == "__main__":
    app.run(debug=True)