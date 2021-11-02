import os
from flask import Flask, render_template, send_file, request
from api import api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#https://theaudiodb.com/api/v1/json/1/search.php?s=coldplay
@app.route('/download')
def download_file():
    p = 'logo.png'
    return send_file(p, as_attachment=True)

@app.route('/getapi', methods=['GET', 'POST'])
def buscar_valor():
    if request.method == 'POST':
        artista = request.form['input-search']
        print(artista)
        context = api.BotCsv().ler_nome_lojas(artista=artista)
        print(context)
        if context:
            return render_template('index.html', context=context)
    return render_template('index.html')
    #return render_template('index.html')
# if __name__ == '__main__':
#     app.run(debug=True)
def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()