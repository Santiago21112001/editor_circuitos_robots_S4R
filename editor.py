from abc import ABC, abstractmethod
from tkinter import ttk


class Editor(ABC):
    def __init__(self, container):
        self.frame = ttk.Frame(container)

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass
    