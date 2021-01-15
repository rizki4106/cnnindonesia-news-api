from bs4 import BeautifulSoup
from requests import get
import json

class Script:

    def query(self, url):
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all('article')
        data = []

        for i in tag:
            try:
                title = i.find('h2').text
                link = i.find('a').get('href')
                gambar = i.find('img').get('src')
                tipe = i.find('span', class_="kanal").text
                waktu = i.find('span', class_="date").text
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    "tipe": tipe,
                    "waktu": waktu
                })
            except:
                pass

        return data

    def index(self):
        return self.query('https://www.cnnindonesia.com/')

    def nasional(self):
        return self.query('https://www.cnnindonesia.com/nasional')
    def internasional(self):
        return self.query('https://www.cnnindonesia.com/internasional')
    def ekonomi(self):
        return self.query('https://www.cnnindonesia.com/ekonomi')
    def olahraga(self):
        return self.query('https://www.cnnindonesia.com/olahraga')

    def teknologi(self):
        return self.query('https://www.cnnindonesia.com/teknologi')

    def hiburan(self):
        return self.query('https://www.cnnindonesia.com/hiburan')

    def social(self):
        return self.query('https://www.cnnindonesia.com/gaya-hidup')

    def detail(self, url):
        data = []
        try:
            req = get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            tag = soup.find('div', class_="detail_text")
            gambar = soup.find('div', class_='media_artikel').find('img').get('src')
            judul = soup.find('h1', class_='title').text
            body = tag.text
            data.append({
                "judul": judul,
                "poster": gambar,
                "body": body,
            })
        except:
            data.append({
                "message": "network error",
            })

        return data

    def search(self,q):
        return self.query('https://www.cnnindonesia.com/search/?query=' + q)

if __name__ != '__main__':
    Code = Script()