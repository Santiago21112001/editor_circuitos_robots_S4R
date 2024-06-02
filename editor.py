from abc import ABC, abstractmethod
from tkinter import ttk

from file_manager import FileManager

import tkinter as tk


class Editor(ABC):
    def __init__(self, container):
        self.frame = ttk.Frame(container)
        self.file_manager = FileManager()

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

    def destroy_frame(self):
        self.frame.destroy()

    def pack_frame(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
