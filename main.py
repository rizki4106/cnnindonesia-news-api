from flask import Flask, request
from src import res
app = Flask(__name__)

# import module from ./src
from src import Code

@app.route('/')
def home():
    response = Code.index()
    return res.success(response)

@app.route('/nasional')
def nasional():
    response = Code.nasional()
    return res.success(response)

@app.route('/internasional')
def internasional():
    response = Code.internasional()
    return res.success(response)

@app.route('/ekonomi')
def ekonomi():
    response = Code.ekonomi()
    return res.success(response)

@app.route('/olahraga')
def olahraga():
    response = Code.olahraga()
    return res.success(response)

@app.route('/teknologi')
def teknologi():
    response = Code.teknologi()
    return res.success(response)

@app.route('/hiburan')
def hiburan():
    response = Code.hiburan()
    return res.success(response)

@app.route('/gaya-hidup')
def social():
    response = Code.social()
    return res.success(response)

@app.route('/detail/')
def detail():
    url = request.args.get('url')
    response = Code.detail(url)
    return res.success(response)

@app.route('/search/')
def search():
    param = request.args.get('q')
    response = Code.search(param)
    return res.success(response)


if __name__ == "__main__":
    app.run(debug=True)