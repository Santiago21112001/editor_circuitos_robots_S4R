import tkinter as tk
from tkinter import messagebox

from editor import Editor
from robots_manager import RobotsManager


class RobotsEditor(Editor):
    def __init__(self, container):
        super().__init__(container)
        self.robot_manager = RobotsManager()
        self.create_widgets()
        self.__populate_robots_list()
        self.__select_robot(0)
        self.__select_element(0)

    def create_widgets(self):
        """Creates all the graphic elements and places them on the screen."""
        self.robots_label = tk.Label(self, text="Robots")
        self.robots_label.grid(row=0, column=0, padx=10, pady=5)

        self.robots_listbox = tk.Listbox(self, height=10)
        self.robots_listbox.grid(row=1, column=0, rowspan=6, columnspan=2, padx=10, pady=10, sticky='ns')
        self.robots_listbox.bind('<<ListboxSelect>>', self.__on_robot_select)

        self.robot_name_label = tk.Label(self, text="Nombre del robot")
        self.robot_name_label.grid(row=0, column=1, padx=10, pady=5)
        self.robot_name_entry = tk.Entry(self)
        self.robot_name_entry.grid(row=0, column=2, padx=10, pady=5, sticky='ew')

        self.elements_listbox = tk.Listbox(self, height=10)
        self.elements_listbox.grid(row=1, column=1, rowspan=6, columnspan=2, padx=10, pady=10, sticky='ns')
        self.elements_listbox.bind('<<ListboxSelect>>', self.__on_element_select)

        self.element_pin_label = tk.Label(self, text="Pin del elemento")
        self.element_pin_label.grid(row=8, column=0, padx=10, pady=5)
        self.element_pin_entry = tk.Entry(self)
        self.element_pin_entry.grid(row=8, column=1, padx=10, pady=5, sticky='ew')

        self.update_button = tk.Button(self, text="Actualizar pin", command=self.__update_element)
        self.update_button.grid(row=8, column=2, padx=10, pady=10)

        self.add_element_button = tk.Button(self, text="Agregar sensor de luz", command=self.__add_light)
        self.add_element_button.grid(row=9, column=0, padx=10, pady=10)

        self.delete_element_button = tk.Button(self, text="Eliminar sensor de luz", command=self.__delete_light)
        self.delete_element_button.grid(row=9, column=1, padx=10, pady=10)

        self.save_button = tk.Button(self, text="Guardar archivo", command=self.save_file, bg="green", fg="white")
        self.save_button.grid(row=9, column=2, padx=10, pady=10)

    def __populate_robots_list(self):
        self.robots_listbox.delete(0, tk.END)
        robots = self.robot_manager.get_robots()
        for robot in robots:
            self.robots_listbox.insert(tk.END, robot.get_name())

    def __select_robot(self, index: int):
        self.current_robot_index = index
        self.robot_name_entry.delete(0, tk.END)
        self.robot_name_entry.insert(0, self.robot_manager.get_robots()[index].get_name())
        self.__populate_elements_list()

    def __on_robot_select(self, event):
        selected_index = self.robots_listbox.curselection()
        if not selected_index:
            return
        index = int(selected_index[0])
        self.__select_robot(index)

    def __populate_elements_list(self):
        self.elements_listbox.delete(0, tk.END)
        elements = self.robot_manager.get_robots()[self.current_robot_index].get_elements()
        for e in elements:
            self.elements_listbox.insert(tk.END, e["name"])

    def __select_element(self, index: int):
        self.current_element_index = index
        self.element_pin_entry.delete(0, tk.END)
        elements = self.robot_manager.get_robots()[self.current_robot_index].get_elements()
        self.element_pin_entry.insert(0, elements[self.current_element_index]["pin"])

    def __on_element_select(self, event):
        selected_index = self.elements_listbox.curselection()
        if not selected_index:
            return
        index = int(selected_index[0])
        self.__select_element(index)

    def __update_element(self):
        try:
            pin = self.element_pin_entry.get()
            element_index = self.current_element_index
            index = self.current_robot_index

            self.robot_manager.update_robot_element(index, element_index, pin)
            self.__populate_elements_list()
        except ValueError:
            messagebox.showerror("Error al actualizar", "El pin del elemento debe ser un número.")

    def __add_light(self):
        try:
            self.robot_manager.get_robots()[self.current_robot_index].add_light()
            self.__populate_elements_list()
        except ValueError as err:
            messagebox.showerror("Error al añadir sensor de luz", str(err))

    def __delete_light(self):
        try:
            index = self.current_robot_index
            light_index: int = self.current_element_index
            self.robot_manager.delete_light(index, light_index)
            self.__populate_elements_list()
            self.__select_element(0)
        except ValueError as err:
            messagebox.showerror("Error al eliminar sensor de luz", str(err))

    def open_file(self):
        file_content = self.file_manager.open_file()
        message = check_format(file_content)
        if message != "":
            messagebox.showerror("Archivo inválido", message)
            return
        self.robot_manager.load_json_data(file_content)
        self.__populate_robots_list()
        self.__select_robot(0)
        self.__select_element(0)

    def save_file(self):
        file_path = "robots.json"
        file_data = self.robot_manager.to_json()
        self.file_manager.save_file(file_data, file_path)
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
