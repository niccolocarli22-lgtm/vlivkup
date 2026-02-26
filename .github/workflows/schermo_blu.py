import tkinter as tk

# Crea la finestra
def mostra_schermo():
    finestra = tk.Tk()
    finestra.title("Ciao!")
    finestra.configure(bg='blue')
    finestra.geometry('400x200')

    messaggio = tk.Label(finestra, text="Ciao!", font=("Arial", 30), bg='blue', fg='white')
    messaggio.pack(expand=True)

    finestra.mainloop()

if __name__ == "__main__":
    mostra_schermo()
