from abc import ABC, abstractmethod
from tkinter import ttk

from file_manager import FileManager

import tkinter as tk


class Editor(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.file_manager = FileManager()
        self.pack(fill=tk.BOTH, expand=True)

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass
