import os
from flask import Flask

#buat instance
app = Flask(__name__)

#definisi route dasar
@app.route('/')
def home():
    return "Hello World! Ini halaman utama."

#penambahan route /about
@app.route('/about')
def about():
    return "<h1> Tentang Kami</h1><p>Ini adalah halaman about.</p><ul><li>Item1</li></ul>"

@app.route('/contact')
def contact():
    return "<h1>Hubungi kami</h1><p>email@contoh.com</p>"
#jalankan server
if __name__ == '__main__':
    app.run(debug=True, port=3900)