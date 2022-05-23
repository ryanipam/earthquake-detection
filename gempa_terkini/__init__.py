def data_extraction():
    hasil = {
        'tanggal': '23 Mei 2022, 00:38:14 WIB',
        'magnitudo': '4.7',
        'kedalaman': '60 km',
        'pusat': 'Pusat gempa berada di laut 55 km Baratdaya Lubukbasung'
    }
    return hasil


def show_data(response):
    print(f"Earthquake date: {response['tanggal']}")
    print(f"Magnitud: {response['magnitudo']}")
    print(f"Depth: {response['kedalaman']}")
    print(f"Center Earthquake: {response['pusat']}")