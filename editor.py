import tkinter as tk
from abc import abstractmethod
from tkinter import ttk

from file_manager import FileManager


class Editor:
    def __init__(self, container):
        self.frame = ttk.Frame(master=container)
        self.file_manager = FileManager()
        self.frame.pack(fill=tk.BOTH, expand=True)

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass
