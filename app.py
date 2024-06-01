import tkinter as tk
from tkinter import ttk

from circuits_editor import CircuitsEditor


class App:
    def __init__(self):
        """
        Constructor for App.
        """
        self.selected_piece = None
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        width = 1024
        height = 768
        self.root.geometry(str(width)+"x"+str(height))
        self.root.resizable(False, False)

        # Contenedor principal para los frames
        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Instanciar todas las ventanas
        self.editor = CircuitsEditor(self.container, width, height)

        self.menu_bar = self.create_menu()

        self.editor.frame.grid(row=0, column=0, sticky="nsew")
        self.editor.frame.tkraise()
        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy)

        return menu_bar

    def open_file(self):
        self.editor.open_file()

    def save_file(self):
        self.editor.save_file()
