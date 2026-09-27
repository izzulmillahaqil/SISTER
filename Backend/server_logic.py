# backend/server_logic.py
import math

# 1. Operasi Matematika Lanjutan
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan!"
    return a / b

def pangkat(basis, eksponen):
    return math.pow(basis, eksponen)


# 2. Operasi Manipulasi String / Teks
def balik_teks(teks):
    return str(teks)[::-1]

def hitung_karakter(teks):
    return len(str(teks))


# 3. Operasi Manipulasi List / Data (Mirip contoh di slide materi)
def append_data(item, data_list):
    if isinstance(data_list, list):
        data_list.append(item)
        return data_list
    return "Error: Argumen kedua harus berupa list!"

def cari_max(data_list):
    if isinstance(data_list, list) and len(data_list) > 0:
        return max(data_list)
    return "Error: List kosong atau tidak valid!"   