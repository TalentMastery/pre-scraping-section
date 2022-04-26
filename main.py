"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
Modularisasi dengan {Package
"""
# from earthquakeUpdate import ekstraksi_data, tampilkan_data
import earthquakeupdate

if __name__ == '__main__':
    print('aplikasi utama')
    result = earthquakeupdate.ekstraksi_data()
    earthquakeupdate.tampilkan_data(result)
