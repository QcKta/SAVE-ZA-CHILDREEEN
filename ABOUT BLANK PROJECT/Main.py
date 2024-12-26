import os

# Definisci il testo da scrivere nel blocco note
testo = "le mini titties poco sviluppate sono golosissime!!!! le mini titties poco sviluppate sono golosissime!!!! le mini titties poco sviluppate sono golosissime!!!! le mini titties poco sviluppate sono golosissime!!!! le mini titties poco sviluppate sono golosissime!!!!\n" * 100  # Ripete il testo 100 volte, con una nuova linea per ogni occorrenza

# Crea un file temporaneo
percorso_file = "ByFilippo.txt"
with open(percorso_file, "w") as file:
    file.write(testo)

# Apre il file creato nel Blocco Note (Notepad) su Windows
os.system(f"notepad {percorso_file}")

import tkinter as tk
import os
import time
import webbrowser

# Funzione per aprire la pagina Save the Children
def apri_save_the_children():
    webbrowser.open("https://www.savethechildren.org/")

# Scrivere il testo nel file
testo = "odio i bambini\n" * 100
percorso_file = "odio_i_bambini.txt"
with open(percorso_file, "w") as file:
    file.write(testo)

# Apre il file creato nel Blocco Note (Notepad) su Windows
os.system(f"notepad {percorso_file}")

# Creazione della finestra principale con tkinter
finestra = tk.Tk()
finestra.title("Interfaccia")

# Funzione che viene chiamata dopo 3 secondi per mostrare il bottone
def mostra_bottone():
    bottone_amo = tk.Button(finestra, text="Amo i bambini", command=apri_save_the_children)
    bottone_amo.pack(pady=20)

# Mostra il bottone dopo 7 secondi
finestra.after(7000, mostra_bottone)

# Avvia l'interfaccia grafica
finestra.mainloop()