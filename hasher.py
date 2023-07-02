#Install depends before running script
#pip3 install crcmod

import tkinter as tk
import hashlib
import binascii
import zlib
import crcmod
from tkinter import filedialog, messagebox

def calculate_hash():
    selected_algorithm = algorithm_var.get()
    file_path = file_var.get()
    checksum = checksum_entry.get()

    try:
        with open(file_path, 'rb') as file:
            content = file.read()

            if selected_algorithm == 'SHA1':
                calculated_hash = hashlib.sha1(content).hexdigest()
            elif selected_algorithm == 'SHA256':
                calculated_hash = hashlib.sha256(content).hexdigest()
            elif selected_algorithm == 'SHA384':
                calculated_hash = hashlib.sha384(content).hexdigest()
            elif selected_algorithm == 'SHA512':
                calculated_hash = hashlib.sha512(content).hexdigest()
            elif selected_algorithm == 'Blake2':
                calculated_hash = hashlib.blake2s(content).hexdigest()
            elif selected_algorithm == 'Whirlpool':
                calculated_hash = hashlib.new('whirlpool', content).hexdigest()
            elif selected_algorithm == 'RIPEMD160':
                calculated_hash = hashlib.new('ripemd160', content).hexdigest()
            elif selected_algorithm == 'Tiger':
                calculated_hash = hashlib.new('tiger192,3', content).hexdigest()
            elif selected_algorithm == 'MurmurHash':
                calculated_hash = binascii.hexlify(hashlib.murmur3_32(content).digest()).decode('utf-8')
            elif selected_algorithm == 'CRC16':
                crc_func = crcmod.mkCrcFun('crc-16')
                calculated_hash = hex(crc_func(content))[2:]
            elif selected_algorithm == 'CRC32':
                calculated_hash = hex(zlib.crc32(content))[2:]
            elif selected_algorithm == 'CRC8':
                crc_func = crcmod.predefined.Crc('crc-8')
                crc_func.update(content)
                calculated_hash = hex(crc_func.crcValue)[2:]
            elif selected_algorithm == 'CRC64':
                crc_func = crcmod.predefined.Crc('crc-64')
                crc_func.update(content)
                calculated_hash = hex(crc_func.crcValue)[2:]
            else:
                calculated_hash = ''

            if calculated_hash == checksum:
                messagebox.showinfo('Hash Comparison', 'The calculated hash matches the provided checksum.')
            else:
                messagebox.showinfo('Hash Comparison', 'The calculated hash does not match the provided checksum.')
    except FileNotFoundError:
        messagebox.showerror('Error', 'File not found.')

def browse_file():
    file_path = filedialog.askopenfilename()
    file_var.set(file_path)

window = tk.Tk()
window.title('Hash Calculator')

checksum_label = tk.Label(window, text='Checksum:')
checksum_label.pack()
checksum_entry = tk.Entry(window)
checksum_entry.pack()

browse_button = tk.Button(window, text='Browse', command=browse_file)
browse_button.pack()

algorithm_var = tk.StringVar(window)
algorithm_var.set('SHA1')
algorithm_label = tk.Label(window, text='Algorithm:')
algorithm_label.pack()
algorithm_menu = tk.OptionMenu(window, algorithm_var, 'SHA1', 'SHA256', 'SHA384', 'SHA512',
                              'Blake2', 'Whirlpool', 'RIPEMD160', 'Tiger', 'MurmurHash',
                              'CRC16', 'CRC32', 'CRC8', 'CRC64')
algorithm_menu.pack()

calculate_button = tk.Button(window, text='Calculate Hash', command=calculate_hash)
calculate_button.pack()

file_var = tk.StringVar()

window.mainloop()