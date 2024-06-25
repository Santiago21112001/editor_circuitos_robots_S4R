import json
from tkinter import filedialog


class FileManager:
    def __init__(self):
        pass

    def open_file(self, file_path):
        if file_path:
            with open(file_path, 'r') as file:
                content = json.load(file)
                print("Archivo abierto")
            return content
        else:
            return None

    def save_file(self, content, file_path):
        with open(file_path, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Se ha guardado el archivo JSON como '{file_path}'.")
