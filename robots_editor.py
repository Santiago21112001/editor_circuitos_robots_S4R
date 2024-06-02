from tkinter import messagebox

from editor import Editor


class RobotsEditor(Editor):

    def __init__(self, container):
        super().__init__(container)
        self.file_content = {"robots": [
            {
                "name": "mobile2",
                "elements": []
            }]}

    def open_file(self):
        file_content = self.file_manager.open_file()
        message = check_format(file_content)
        if message != "":
            messagebox.showerror("Archivo inválido", message)
            return
        self.file_content = file_content

    def save_file(self):
        pass


def check_format(data):
    # Comprobar que data es un diccionario
    if not isinstance(data, dict):
        return "El contenido debe ser un diccionario."

    # Comprobar que tiene el campo 'robots' y que es una lista
    if 'robots' not in data:
        return "Falta el campo 'robots'."
    if not isinstance(data['robots'], list):
        return "El campo 'robots' debe ser una lista."

    # Comprobar cada robot
    for robot in data['robots']:
        if not isinstance(robot, dict):
            return "Cada elemento de 'robots' debe ser un diccionario."
        if 'name' not in robot:
            return "Falta el campo 'name' en un robot."
        if 'elements' not in robot:
            return "Falta el campo 'elements' en un robot."
        if not isinstance(robot['elements'], list):
            return "El campo 'elements' debe ser una lista en un robot."

        # Comprobar cada elemento del robot
        for element in robot['elements']:
            if not isinstance(element, dict):
                return "Cada elemento de 'elements' debe ser un diccionario."
            if 'name' not in element:
                return "Falta el campo 'name' en un elemento."
            if 'pin' not in element:
                return "Falta el campo 'pin' en un elemento."

    return ""
