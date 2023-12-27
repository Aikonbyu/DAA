import streamlit as st
from controller.tambah_data import tambah_data
from controller.sentinel_linear_search import sentinelLinearSearch

def main():
    st.title("Aplikasi Management Data Mahasiswa")
    menu = st.selectbox("Menu", ["Data Mahasiswa", "Tambah Data", "Cari Data", "Hapus Data"])
    if  menu == "Data Mahasiswa":
        st.title("Data Mahasiswa")
        with open("./model/data.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        data_array = []
        for line in lines:
            data = line.strip().split(';')
            data = [(item) for item in data]
            data_array.append(data)

        st.table(data_array)

    elif menu == "Tambah Data":
        st.title("Tambah Data")
        nim = st.text_input("NIM", "")
        nama = st.text_input("Nama", "")
        alamat = st.text_input("Alamat", "")
        tambah = st.button("Tambah")
        if tambah:
            tambah_data(nim, nama, alamat)
            st.success("Data berhasil ditambahkan!")

    elif menu == "Cari Data":
        st.title("Program Searching NIM Mahasiswa")
        st.write("Massukkan NIM yang ingin dicari!")
        nims = st.text_input("NIM", "")
        if nims == "":    
            with open("./model/data.txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()

            data_array = []
            for line in lines:
                data = line.strip().split(';')
                data = [(item) for item in data]
                data_array.append(data)

            st.table(data_array)
        if nims != "":
            with open("./model/data.txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()

            data_array = []
            for line in lines:
                data = line.strip().split(';')
                data = [(item) for item in data]
                data_array.append(data)
            
            result = sentinelLinearSearch(data_array, nims)
            if result == -1:
                st.write("Data tidak ditemukan!")
            else:
                st.write("Data ditemukan!")
                searchresult = [data_array[result]]
                st.table(searchresult)


    elif menu == "Hapus Data":
        st.title("Hapus Data")
        nim = st.text_input("NIM", "")
        hapus = st.button("Hapus")

        if hapus:
            f = open("./model/data.txt", "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            f = open("./model/data.txt", "w", encoding="utf-8")
            for line in lines:
                data = line.strip().split(";")
                if data[0] != nim:
                    f.write(line)
            f.close()
            st.success("Data berhasil dihapus!")