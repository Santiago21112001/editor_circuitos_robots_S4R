from tkinter import filedialog
import json
import os


class FileManager:
    def __init__(self):
        pass

    def open_data_file(self):
        file_path = "robot_data.json"
        if file_path:
            with open(file_path, 'r') as file:
                content = json.load(file)
                print(f"Contenido del archivo JSON:\n{content}")
            return content
        else:
            return None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                content = json.load(file)
                print(f"Contenido del archivo JSON:\n{content}")
            return content
        else:
            return None

    def save_file(self, content):
        file_path = os.path.join(os.getcwd(), "robot_data.json")
        with open(file_path, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Se ha guardado el archivo JSON como '{file_path}'.")
