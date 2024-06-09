from abc import abstractmethod
import tkinter as tk

from file_manager import FileManager


class Editor:
    def __init__(self, container):
        self.frame = tk.Frame(master=container)
        self.file_manager = FileManager()
        self.frame.pack(fill="both", expand=True)

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass
