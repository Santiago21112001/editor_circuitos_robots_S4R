import tkinter as tk
from tkinter import filedialog
import json
import os


class FileManager:
    def __init__(self):
        pass

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                content = json.load(file)
                print(f"Contenido del archivo JSON:\n{content}")

    def save_file(self, content):
        file_path = os.path.join(os.getcwd(), "circuits.json")
        with open(file_path, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Se ha guardado el archivo JSON como '{file_path}'.")
