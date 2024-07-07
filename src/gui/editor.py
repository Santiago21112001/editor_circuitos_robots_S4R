from abc import abstractmethod
import tkinter as tk

from files_manager.files_manager import FilesManager


class Editor:
    def __init__(self, container):
        self.frame = tk.Frame(master=container)
        self.file_manager = FilesManager()
        self.frame.pack(fill="both", expand=True)

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    def destroy(self):
        self.frame.destroy()
