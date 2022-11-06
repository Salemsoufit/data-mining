from distutils import dir_util
from tkinter import *
from tkinter import filedialog, ttk
import tkinter
from apriori_traitment import apriori_for_csv, getCSVFromArff
import os
from PIL import Image, ImageTk
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
icon_path = dir_path + '/images/apriori_logo.ico';

my_window = tkinter.Tk()
my_window.geometry("600x500")  # Size of the window
my_window.title('Algorithme Apriori')
my_window.iconbitmap(icon_path)
title = 'Veuillez Choisir le type de fichier à charger !'
# Charger l'image
image = Image.open(dir_path + '/images/image1.png')

# Redimensionner l'image (width, height)
img = image.resize((200, 100))

# Convertir en TkImage
my_img = ImageTk.PhotoImage(img)
image_label = tkinter.Label(anchor=CENTER, image=my_img)
image_label.image = my_img
image_label.place(rely=0, relx=0.25)

frame1 = tkinter.LabelFrame(my_window, text="Résultat")
frame1.place(height=250, width=500, rely=0.20, relx=0)
file_frame = tkinter.LabelFrame(my_window, text="Choisir une action")
file_frame.place(height=100, width=400, rely=0.80, relx=0)
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=2, relwidth=1)

treescrolly = tkinter.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tkinter.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


def open_csv_file():
    f_types = [('CSV files', "*.csv")]
    file = filedialog.askopenfilename(filetypes=f_types)
    file_name = file[file.rfind('/') + 1: file.find('.')]
    df = apriori_for_csv(file)
    result_dir = 'resultats'
    if not os.path.exists(result_dir):
      os.makedirs(result_dir)
    df.to_csv(dir_path + '/' + result_dir + '/' + file_name + '.csv')
    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)


def open_arff_file():
    f_types = [('ARFF files', "*.arff")]
    file = filedialog.askopenfilename(filetypes=f_types)
    if (file):
        getCSVFromArff(file)


# CSV
browse_csv_btn = tkinter.Button(my_window, text='Fichier CSV', width=20, command=lambda: open_csv_file())
browse_csv_btn.place(rely=0.90, relx=0.30)

# ARFF
browse_arff_btn = tkinter.Button(my_window, text='ARFF -> CSV', width=20, command=lambda: open_arff_file())
browse_arff_btn.place(rely=0.90, relx=0.10)

my_window.mainloop()
