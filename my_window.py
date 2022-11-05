from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter.filedialog import askopenfile
import pandas as pd 
from apyori import apriori
from apriori_traitment import apriori_for_csv, getCSVFromArff
import os 
from PIL import Image, ImageTk
from pandastable import Table, TableModel


dir_path = os.path.dirname(os.path.realpath(__file__))
icon_path = dir_path + '/images/apriori_logo.ico';

def open_csv_file():
  f_types = [('CSV files',"*.csv")]
  file = filedialog.askopenfilename(filetypes=f_types)
  print(apriori_for_csv(file))
  #return apriori_for_csv(file)


def open_arff_file():
  f_types = [('ARFF files',"*.arff")]
  file = filedialog.askopenfilename(filetypes=f_types)
  getCSVFromArff(file)

my_window = tkinter.Tk()
my_window.geometry("600x500")  # Size of the window 
my_window.title('Algorithme Apriori')
my_window.iconbitmap(icon_path)
title = 'Veuillez Choisir le type de fichier à charger !'

# Load the image
image=Image.open(dir_path + '/images/image1.png')

# Resize the image in the given (width, height)
img=image.resize((200, 150))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)
image_label = tkinter.Label(anchor=CENTER, image=my_img)
image_label.image = my_img
image_label.grid(row=2, column=2)

#CSV
browse_csv_btn = tkinter.Button(my_window, text='Fichier CSV', width=20,command = lambda:open_csv_file())
browse_csv_btn.grid(row=7,column=1)

#ARFF
browse_arff_btn = tkinter.Button(my_window, text='Convert ARFF to CSV', width=20,command = lambda:open_arff_file())
browse_arff_btn.grid(row=7,column=2)

#Result Button
browse_arff_btn = tkinter.Button(my_window, text='Afficher les résultats', width=20,command = lambda:open_arff_file())
browse_arff_btn.grid(row=7,column=3)



my_window.mainloop() 




  