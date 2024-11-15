import tkinter as tk
from tkinter import ttk

from gui.circuits_editor import CircuitsEditor
from gui.editor import Editor
from gui.robots_editor import RobotsEditor


class App:
    def __init__(self):
        """
        Constructor for App.
        """
        self.selected_piece = None
        self.root = tk.Tk()
        self.root.title("Editor de circuitos y robots")
        self.width = 1024
        self.height = 768
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)

        # Main frame container
        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Create frame
        self.editor: Editor = CircuitsEditor(self.container, self.width, self.height)

        self.menu_bar = self.create_menu()

        self.editor.frame.tkraise()

    def run(self):
        self.root.mainloop()

    def set_editor(self, new_editor_str):
        """Destroys current editor and replaces it with a new one."""
        if self.editor is not None:
            self.editor.destroy()
        if new_editor_str == "c":
            new_editor = CircuitsEditor(self.container, self.width, self.height)
        else:
            new_editor = RobotsEditor(self.container)
        self.editor = new_editor

    def switch_to_robots_editor(self):
        self.set_editor("r")

    def switch_to_circuits_editor(self):
        self.set_editor("c")

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        #  'Archivo' Menu bar
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file, accelerator="Ctrl+O")
        self.root.bind("<Control-o>", lambda event: self.open_file())
        file_menu.add_command(label="Guardar", command=self.save_file, accelerator="Ctrl+S")
        self.root.bind("<Control-s>", lambda event: self.save_file())
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy, accelerator="Ctrl+Q")
        self.root.bind("<Control-q>", lambda event: self.root.destroy())

        #  'Cambiar de editor' Menu bar
        file_menu_editor = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Cambiar de editor", menu=file_menu_editor)
        file_menu_editor.add_command(label="Ir al editor de robots", command=self.switch_to_robots_editor,
                                     accelerator="Ctrl+R")
        self.root.bind("<Control-r>", lambda event: self.switch_to_robots_editor())
        file_menu_editor.add_command(label="Ir al editor de circuitos", command=self.switch_to_circuits_editor,
                                     accelerator="Ctrl+C")
        self.root.bind("<Control-c>", lambda event: self.switch_to_circuits_editor())

        return menu_bar

    def open_file(self):
        self.editor.open_file()

    def save_file(self):
        self.editor.save_file()
