import tkinter as tk
from tkinter import ttk

from circuit_editor import CircuitEditor
from circuits_editor import CircuitsEditor
from robots_editor import RobotsEditor
from editor import Editor


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
        self.root.geometry(str(self.width)+"x"+str(self.height))
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
            self.editor.frame.destroy()
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

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.destroy)

        file_menu_editor = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Editor", menu=file_menu_editor)
        file_menu_editor.add_command(label="Ir al editor de robots", command=self.switch_to_robots_editor)
        file_menu_editor.add_command(label="Ir al editor de circuitos", command=self.switch_to_circuits_editor)

        return menu_bar

    def open_file(self):
        self.editor.open_file()

    def save_file(self):
        self.editor.save_file()
