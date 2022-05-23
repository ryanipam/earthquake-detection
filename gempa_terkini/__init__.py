from bs4 import BeautifulSoup
import requests


def data_extraction():
    try:
        r = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    # condition if website true
    if r.status_code == 200:
        hasil = dict()
        soup = BeautifulSoup(r.text, 'html.parser')

        # geting data which used for result
        """ Tanggal & waktu """
        tanggal = soup.find('span', {'class': 'waktu'}).text.split(', ')
        waktu = tanggal[1]
        tanggal = tanggal[0]

        """ Magnitudo, Kedalaman, Center"""
        res = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        res = res.findChildren('li')
        hasil = {
            'tanggal': tanggal,
            'waktu': waktu,
            'magnitudo': res[1].text,
            'kedalaman': res[2].text,
            'pusat': res[4].text
        }
        return hasil
    else:
        return None


def show_data(response):
    if response is not None:
        print(f"Earthquake date: {response['tanggal']}")
        print(f"Earthquake time: {response['waktu']}")
        print(f"Magnitudo: {response['magnitudo']}")
        print(f"Depth: {response['kedalaman']}")
        print(f"Center Earthquake: {response['pusat']}")
    else:
        print('no data catched')