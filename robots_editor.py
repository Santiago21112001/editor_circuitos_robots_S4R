import tkinter as tk
from tkinter import messagebox

from editor import Editor


class RobotsEditor(Editor):

    def __init__(self, container):
        super().__init__(container)
        self.current_robot_index = 0

        self.ROBOT_MOBILE_DEFAULT_ELEMENTS = [
            {"name": "servo left", "pin": "8"},
            {"name": "servo right", "pin": "9"},
            {"name": "light 2", "pin": "2"},
            {"name": "light 3", "pin": "3"},
            {"name": "trig", "pin": "4"},
            {"name": "echo", "pin": "5"}]

        self.file_data = {"robots": [
            {
                "name": "mobile2",
                "elements": self.ROBOT_MOBILE_DEFAULT_ELEMENTS
            }]}

        self.current_element_index = None

        self.create_widgets()
        self.on_robot_select()

    def create_widgets(self):
        """Creates all the graphic elements and place them on the screen."""
        self.robot_name_label = tk.Label(self, text="Nombre del robot")
        self.robot_name_label.grid(row=0, column=1, padx=10, pady=5)
        self.robot_name_entry = tk.Entry(self)
        self.robot_name_entry.grid(row=0, column=2, padx=10, pady=5, sticky='ew')

        self.elements_listbox = tk.Listbox(self, height=10)
        self.elements_listbox.grid(row=1, column=1, rowspan=6, columnspan=2, padx=10, pady=10, sticky='ns')
        self.elements_listbox.bind('<<ListboxSelect>>', self.on_element_select)

        self.element_name_label = tk.Label(self, text="Nombre del elemento")
        self.element_name_label.grid(row=7, column=0, padx=10, pady=5)
        self.element_name_entry = tk.Entry(self)
        self.element_name_entry.grid(row=7, column=1, padx=10, pady=5, sticky='ew')

        self.element_pin_label = tk.Label(self, text="Pin del elemento")
        self.element_pin_label.grid(row=8, column=0, padx=10, pady=5)
        self.element_pin_entry = tk.Entry(self)
        self.element_pin_entry.grid(row=8, column=1, padx=10, pady=5, sticky='ew')

        self.update_button = tk.Button(self, text="Actualizar elemento", command=self.update_element)
        self.update_button.grid(row=9, column=0, padx=10, pady=10)

        self.add_element_button = tk.Button(self, text="Agregar elemento", command=self.add_element)
        self.add_element_button.grid(row=9, column=1, padx=10, pady=10)

        self.delete_element_button = tk.Button(self, text="Eliminar elemento", command=self.delete_element)
        self.delete_element_button.grid(row=9, column=2, padx=10, pady=10)

        self.save_button = tk.Button(self, text="Guardar archivo", command=self.save_file)
        self.save_button.grid(row=10, column=1, padx=10, pady=10)

    def on_robot_select(self):
        robot = self.file_data['robots'][self.current_robot_index]
        self.robot_name_entry.delete(0, tk.END)
        self.robot_name_entry.insert(0, robot['name'])
        self.populate_elements_list()

    def populate_elements_list(self):
        self.elements_listbox.delete(0, tk.END)
        robot = self.file_data['robots'][self.current_robot_index]
        for element in robot['elements']:
            self.elements_listbox.insert(tk.END, element['name'])

    def on_element_select(self, event):
        selected_index = self.elements_listbox.curselection()
        if not selected_index:
            return
        self.current_element_index = selected_index[0]
        element = self.file_data['robots'][self.current_robot_index]['elements'][self.current_element_index]
        self.element_name_entry.delete(0, tk.END)
        self.element_name_entry.insert(0, element['name'])
        self.element_pin_entry.delete(0, tk.END)
        self.element_pin_entry.insert(0, element['pin'])

    def update_element(self):
        element_name = self.element_name_entry.get()
        element_pin = self.element_pin_entry.get()
        if not element_name or not element_pin:
            messagebox.showerror("Error", "El nombre y el pin del elemento no pueden estar vacíos.")
            return
        robot = self.file_data['robots'][self.current_robot_index]
        robot['elements'][self.current_element_index] = {'name': element_name, 'pin': element_pin}
        self.populate_elements_list()

    def add_element(self):
        if self.current_robot_index is None:
            return
        element_name = self.element_name_entry.get()
        element_pin = self.element_pin_entry.get()
        if not element_name or not element_pin:
            messagebox.showerror("Error", "El nombre y el pin del elemento no pueden estar vacíos.")
            return
        robot = self.file_data['robots'][self.current_robot_index]
        robot['elements'].append({'name': element_name, 'pin': element_pin})
        self.populate_elements_list()

    def delete_element(self):
        try:
            robot = self.file_data['robots'][self.current_robot_index]
            del robot['elements'][self.current_element_index]
        except IndexError:
            messagebox.showerror("Error", "Selecciona un elemento de un robot antes de borrar.")
            return
        self.populate_elements_list()

    def open_file(self):
        file_content = self.file_manager.open_file()
        message = check_format(file_content)
        if message != "":
            messagebox.showerror("Archivo inválido", message)
            return
        self.file_data = file_content
        self.on_robot_select()


    def save_file(self):
        file_path = "robots.json"
        self.file_manager.save_file(self.file_data, file_path)
        messagebox.showinfo("Archivo guardado", "Se ha guardado el archivo 'robots.json' en el "
                                                "directorio raíz de la aplicación")

def check_format(data):
    # Check that data is a dictionary
    if not isinstance(data, dict):
        return "El contenido debe ser un diccionario."

    # Check that it has the 'robots' field and that it is a list
    if 'robots' not in data:
        return "Falta el campo 'robots'."
    if not isinstance(data['robots'], list):
        return "El campo 'robots' debe ser una lista."

    # Check each robot
    for robot in data['robots']:
        if not isinstance(robot, dict):
            return "Cada elemento de 'robots' debe ser un diccionario."
        if 'name' not in robot:
            return "Falta el campo 'name' en un robot."
        if 'elements' not in robot:
            return "Falta el campo 'elements' en un robot."
        if not isinstance(robot['elements'], list):
            return "El campo 'elements' debe ser una lista en un robot."

        # Check each element of the robot
        for element in robot['elements']:
            if not isinstance(element, dict):
                return "Cada elemento de 'elements' debe ser un diccionario."
            if 'name' not in element:
                return "Falta el campo 'name' en un elemento."
            if 'pin' not in element:
                return "Falta el campo 'pin' en un elemento."

    return ""
