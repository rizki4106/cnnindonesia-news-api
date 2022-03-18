from bs4 import BeautifulSoup
from requests import get

base_url = 'https://www.cnnindonesia.com'

class Script:

    def query(self, url):
        datas = get(url)
        soup = BeautifulSoup(datas.text, 'html.parser')
        tag = soup.find_all('article')
        data = []

        for i in tag:
            try:
                title = i.find("h2", attrs={'class':'title'}).text.strip()
                link = i.find('a')['href'].strip()
                gambar = i.find('img')['src'].strip()
                # tipe = i.find('span', attrs={'class':'kanal'}).text
                # waktu = i.find('span', attrs={'class':'date'}).text
                data.append({
                    "judul": title,
                    "link": link,
                    "poster": gambar,
                    # "tipe": tipe,
                    # "waktu": waktu
                })
            except:
                pass

        return data

    def index(self):
        return self.query('{}/'.format(base_url))

    def nasional(self):
        return self.query('{}/nasional'.format(base_url))
    def internasional(self):
        return self.query('{}/internasional'.format(base_url))
    def ekonomi(self):
        return self.query('{}/ekonomi'.format(base_url))
    def olahraga(self):
        return self.query('{}/olahraga'.format(base_url))

    def teknologi(self):
        return self.query('{}/teknologi'.format(base_url))

    def hiburan(self):
        return self.query('{}/hiburan'.format(base_url))

    def social(self):
        return self.query('{}/gaya-hidup'.format(base_url))

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
        return self.query('{}/search/?query={}'.format(base_url, q))

if __name__ != '__main__':
    Code = Script()