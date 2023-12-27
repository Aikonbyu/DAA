def tambah_data(nim, nama, alamat):
    f = open("./model/data.txt", "a", encoding="utf-8")
    f.write(f"{nim};{nama};{alamat}\n")
    f.close
