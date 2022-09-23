from flask import Flask, request
from src import res
app = Flask(__name__)

# import module from ./src
from src import cnn

@app.route('/')
def home():
    response = cnn.index()
    return res.success(response)

@app.route('/nasional')
def nasional():
    response = cnn.berita_nasional()
    return res.success(response)

@app.route('/internasional')
def internasional():
    response = cnn.berita_internasional()
    return res.success(response)

@app.route('/ekonomi')
def ekonomi():
    response = cnn.berita_ekonomi()
    return res.success(response)

@app.route('/olahraga')
def olahraga():
    response = cnn.berita_olahraga()
    return res.success(response)

@app.route('/teknologi')
def teknologi():
    response = cnn.berita_teknologi()
    return res.success(response)

@app.route('/hiburan')
def hiburan():
    response = cnn.berita_hiburan()
    return res.success(response)

@app.route('/gaya-hidup')
def social():
    response = cnn.berita_social()
    return res.success(response)

@app.route('/detail/')
def detail():
    url = request.args.get('url')
    response = cnn.detail(url)
    return res.success(response)

@app.route('/search/')
def search():
    param = request.args.get('q')
    response = cnn.search(param)
    return res.success(response)


if __name__ == "__main__":
    app.run(debug=True)