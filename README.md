`unofficial cnn indonesia api news`

## Pengumunan
API ini sudah tidak disimpan di server [developeridn.com](https://www.developeridn.com), untuk tetap menggunakan API ini silahkan upload script ini ke server anda

## Penggunaan di local server
```bash
git clone https://github.com/rizki4106/cnnindonesia-news-api.git
```

```bash
cd cnnindonesia-news-api && pip install -r requirements.txt
```

```bash
export FLASK_APP=main.py
flask run
```

# cnnindonesia-news-api
kumpulan berita dari bergai belahan dunia dan juga dari berbagai kategori

### penggunaan


<table>
<thead>
<tr>
  <th>No</th>
  <th>Kategori</th>
  <th>Endpoint</th>
  <th>Parameter</th>
  <th>Method</th>
</tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>Index semua berita</td>
    <td>/</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Nasional</td>
    <td>/nasional</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>Internasional</td>
    <td>/internasional</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>4</td>
    <td>Ekonomi</td>
    <td>/ekonomi</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>5</td>
    <td>Olahraga</td>
    <td>/olahraga</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>6</td>
    <td>Teknologi</td>
    <td>/teknologi</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Hiburan</td>
    <td>/hiburan</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>8</td>
    <td>Gaya Hidup</td>
    <td>/gaya-hidupp</td>
    <td>Tidak ada</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>9</td>
    <td>Detail Berita</td>
    <td>/detail/?url=</td>
    <td>url</td>
    <td>GET</td>
  </tr>
  
  <tr>
    <td>10</td>
    <td>Pencarian Berita</td>
    <td>/search/?q=</td>
    <td>q</td>
    <td>GET</td>
  </tr>
</tbody>
</table>

### CONTOH REUQUEST

request random berita

<pre>
$ curl https://www.news.developeridn.com

{
  "data":[
      {
        "judul":"Cara Membayar Fidiah, Tebusan Bagi yang Tak Bisa Berpuasa",
        "link":"https://www.cnnindonesia.com/gaya-hidup/20200506182707-284-500842/cara-membayar-fidiah-tebusan-bagi-yang-tak-bisa-berpuasa",
        "poster":"https://awsimages.detik.net.id/visual/2020/04/17/a4d493fd-90d3-4d05-8e7d-487a30fe2eea_169.jpeg?w=140&q=90",
        "tipe":"Gaya Hidup",
        "waktu":"12 menit yang lalu"
       }
    ],
    "length":40,
    "status":200
}
</pre>

request detail berita

<pre>
$ curl /detail/?url=https://www.cnnindonesia.com/internasional/20200513095240-134-502769/turis-jatuh-usai-nekat-kunjungi-yellowstone-saat-pandemi

{
data: [
    {
      body: " Jakarta, CNN Indonesia -- Seorang turis perempuan diam-diam mengunjungi Taman Nasional Yellowstone, Amerika Serikat yang tengah ditutup akibat pandemi virus corona pada Selasa (12/5).Ia dilaporkan menderita luka bakar lantaran jatuh ke kawah air panas Yellowstone.Juru bicara taman nasional Linda Veress mengatakan perempuan tersebut berusaha mengambil foto sebelum jatuh ke dalam kawah air panas. Perempuan tersebut diketahui muncul di dekat gletser Old Faithful. Kendati mengalami luka-luka, perempuan itu sempat menyetir sejauh 80 kilometer hingga dihentikan oleh penjaga taman nasional di dekat Mammoth Hot Springs. Lihat juga: Dua Staf Kena Corona, Gedung Putih Wajibkan Penggunaan Masker Mengutip Associated Press, perempuan yang tidak diungkap identitas dan cederanya itu kemudian diterbangkan ke rumah sakit di Idaho Falls, Idaho untuk mendapat perawatan.Kejadian pengunjung yang jatuh ke kawah air panas juga pernah terjadi pada 2016 lalu. Colin Scott jatuh ke kawah air panas yang memiliki kandungan zat asam hingga dilaporkan meninggal.Taman Nasional Yellowstone sebenarnya sudah ditutup untuk publik sejak 24 Maret lalu seiring dengan meningkatnya angka penularan virus corona di Amerika Serikat.Selain Yellowstone, Taman Nasional Grand Teton yang berada di dekatnya juga ditutup dan rencananya baru akan dibuka secara bertahap mulai hari ini, Rabu (13/5). Lihat juga: Ditentang China, Selandia Baru Dukung Taiwan Masuk WHO Pengujung sebenarnya sudah diperingatkan untuk berada jauh dari kawah air panas Yellowstone yang meliputi gletser, mata air panas yang memiliki kandungan zat asam.Tak jarang meski sudah mendapat peringatan, turis kerap melanggar jarak aman yang memicu luka bakar hingga mengakibatkan kematian. Sebelum resmi ditutup, seorang pria dilaporkan jatuh hingga menderita luka bakar serius saat berjalan di dekat kawah Yellowstone pada malam hari.Amerika Serikat saat ini menjadi negara dengan kasus dan kematian tertinggi akibat virus corona. Data statistik Worldometers mencatat saat ini ada 1.408.636 kasus virus corona dengan 83.425 kematian dan 296.746 pasien dinyatakan sembuh. (AP/evn) [Gambas:Video CNN] ",
      judul: " Turis Jatuh usai Nekat Kunjungi Yellowstone saat Pandemi ",
      poster: "https://awsimages.detik.net.id/visual/2019/02/06/29f223cf-d5e8-44da-b1a4-e48e31d8c239_169.jpeg?w=650"
    }
  ],
  status: 200
}
</pre>

request pencarian berita

<pre>
$ curl /search/?q=indonesia

{
data: [
      {
        judul: "Arus Modal Keluar Diprediksi Tekan Laju IHSG",
        link: "https://www.cnnindonesia.com/ekonomi/20200514052227-92-503138/arus-modal-keluar-diprediksi-tekan-laju-ihsg",
        poster: "https://awsimages.detik.net.id/visual/2019/02/27/5757e3f9-223f-497e-90cd-e2b47fcf6779_169.jpeg?w=270&q=90",
        tipe: "Ekonomi",
        waktu: " • 47 detik yang lalu"
      },
      {
        judul: "Wagub DKI: Banyak Warga Mampu Ambil Bansos Corona",
        link: "https://www.cnnindonesia.com/nasional/20200513204056-32-503103/wagub-dki-banyak-warga-mampu-ambil-bansos-corona",
        poster: "https://awsimages.detik.net.id/visual/2020/03/06/6f269c56-d2b9-48ee-a544-9e5c396000ce_169.jpeg?w=270&q=90",
        tipe: "Nasional",
        waktu: " • 5 menit yang lalu"
    },
  ],
  length: 7,
  status: 200
}
</pre>




