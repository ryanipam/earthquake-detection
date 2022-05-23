"""
Main aplication
"""
import gempa_terkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempa_terkini.data_extraction()
    gempa_terkini.show_data(result)
