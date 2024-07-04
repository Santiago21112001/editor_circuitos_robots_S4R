import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

from editor import Editor
from robots_manager import RobotsManager


class RobotsEditor(Editor):
    def __init__(self, container):
        super().__init__(container)
        self.robot_manager = RobotsManager()
        # Configure grid weights
        for i in range(10):
            self.frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.frame.grid_columnconfigure(j, weight=1)
        self.create_widgets()
        self.__populate_robots_list()
        self.__select_robot(0)
        self.__select_element(0)

    def create_widgets(self):
        self.title_label = tk.Label(self.frame, text="Se está usando el editor de ROBOTS.\nPara cambiar al de "
                                                     "circuitos,\n seleccione la opción de menú 'Cambiar de editor'.")
        self.title_label.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.robots_label = tk.Label(self.frame, text="Robots")
        self.robots_label.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.elements_label = tk.Label(self.frame, text="Elementos del robot")
        self.elements_label.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        self.add_robot_button = tk.Button(self.frame, text="Añadir robot", command=self.__add_robot)
        self.add_robot_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.delete_robot_button = tk.Button(self.frame, text="Eliminar robot", command=self.__delete_robot)
        self.delete_robot_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.robots_listbox = tk.Listbox(self.frame, height=10)
        self.robots_listbox.grid(row=2, column=1, rowspan=6, columnspan=2, padx=10, pady=10, sticky='nsew')
        self.robots_listbox.bind('<<ListboxSelect>>', self.__on_robot_select)

        self.edit_name_button = tk.Button(self.frame, text="Editar nombre", command=self.__edit_name)
        self.edit_name_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.elements_listbox = tk.Listbox(self.frame, height=10)
        self.elements_listbox.grid(row=2, column=2, rowspan=6, columnspan=2, padx=10, pady=10, sticky='nsew')
        self.elements_listbox.bind('<<ListboxSelect>>', self.__on_element_select)

        self.element_pin_label = tk.Label(self.frame, text="Pin del elemento")
        self.element_pin_label.grid(row=9, column=1, padx=10, pady=5, sticky="ew")
        self.element_pin_entry = tk.Entry(self.frame)
        self.element_pin_entry.grid(row=9, column=2, padx=10, pady=5, sticky='ew')

        self.edit_pin_button = tk.Button(self.frame, text="Actualizar pin", command=self.__edit_pin)
        self.edit_pin_button.grid(row=9, column=3, padx=10, pady=10, sticky="ew")

        self.add_light_sensor_button = tk.Button(self.frame, text="Agregar sensor de luz", command=self.__add_light)
        self.add_light_sensor_button.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

        self.delete_light_sensor_button = tk.Button(self.frame, text="Eliminar sensor de luz",
                                                    command=self.__delete_light)
        self.delete_light_sensor_button.grid(row=10, column=2, padx=10, pady=10, sticky="ew")

        self.save_button = tk.Button(self.frame, text="Guardar archivo", command=self.save_file, bg="green", fg="white")
        self.save_button.grid(row=10, column=3, padx=10, pady=10, sticky="ew")

    def __add_robot(self):
        name: str = "new_robot"
        try:
            self.robot_manager.add_robot(name)
            self.__populate_robots_list()
        except ValueError as err:
            messagebox.showerror("Error al añadir el robot.", str(err))

    def __delete_robot(self):
        index: int = self.current_robot_index
        try:
            self.robot_manager.delete_robot(index)
            self.__populate_robots_list()
            self.__select_robot(0)
        except ValueError as err:
            messagebox.showerror("Error al eliminar el robot.", str(err))

    def __edit_name(self):
        selected = self.robots_listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un robot para editar su nombre")
            return
        index = int(selected[0])
        initial_value = self.robots_listbox.get(index)
        name = simpledialog.askstring("Editar nombre", "Introduzca el nombre:", initialvalue=initial_value)
        if not name:
            return
        try:
            self.robot_manager.set_robot_name(index, name)
            self.__populate_robots_list()
        except ValueError as err:
            messagebox.showerror("Error al actualizar el nombre", str(err))

    def __disable_widgets(self):
        self.edit_name_button.config(state="disabled")
        self.elements_listbox.config(state="disabled")
        self.element_pin_entry.config(state="disabled")
        self.edit_pin_button.config(state="disabled")
        self.add_light_sensor_button.config(state="disabled")
        self.delete_light_sensor_button.config(state="disabled")

    def __enable_widgets(self):
        self.edit_name_button.config(state="normal")
        self.elements_listbox.config(state="normal")
        self.element_pin_entry.config(state="normal")
        self.edit_pin_button.config(state="normal")
        self.add_light_sensor_button.config(state="normal")
        self.delete_light_sensor_button.config(state="normal")

    def __populate_robots_list(self):
        self.robots_listbox.delete(0, tk.END)
        robots = self.robot_manager.get_robots()
        for robot in robots:
            self.robots_listbox.insert(tk.END, robot.get_name())

    def __select_robot(self, index: int):
        self.current_robot_index = index
        self.__populate_robot_data()

    def __on_robot_select(self, event):
        selected_index = self.robots_listbox.curselection()
        if not selected_index:
            return
        index = int(selected_index[0])
        self.__select_robot(index)

    def __populate_robot_data(self):
        self.__enable_widgets()
        robot = self.robot_manager.get_robots()[self.current_robot_index]
        if robot.get_name() in ["actuator", "arduinoBoard"]:
            self.elements_listbox.delete(0, tk.END)
            self.elements_listbox.insert(tk.END, "NO EDITABLE")
            self.__disable_widgets()
        else:
            self.elements_listbox.delete(0, tk.END)
            elements = robot.get_elements()
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

    def __edit_pin(self):
        try:
            pin = self.element_pin_entry.get()
            element_index = self.current_element_index
            index = self.current_robot_index

            self.robot_manager.set_robot_element(index, element_index, pin)
            self.__populate_robot_data()
        except ValueError as err:
            messagebox.showerror("Error al actualizar", str(err))

    def __add_light(self):
        try:
            self.robot_manager.get_robots()[self.current_robot_index].add_light()
            self.__populate_robot_data()
        except ValueError as err:
            messagebox.showerror("Error al añadir sensor de luz", str(err))

    def __delete_light(self):
        try:
            index = self.current_robot_index
            light_index: int = self.current_element_index
            self.robot_manager.delete_light(index, light_index)
            self.__populate_robot_data()
            self.__select_element(0)
        except ValueError as err:
            messagebox.showerror("Error al eliminar sensor de luz", str(err))

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if not file_path:
            return
        try:
            file_content = self.file_manager.open_robots_file(file_path)
        except ValueError as err:
            messagebox.showerror("Archivo inválido", str(err))
            return
        self.robot_manager.load_json_data(file_content)
        self.__populate_robots_list()
        self.__select_robot(0)
        self.__select_element(0)

    def save_file(self):
        file_path = "robots.json"
        content = self.robot_manager.to_json()
        self.file_manager.save_file(content, file_path)
        messagebox.showinfo("Archivo guardado", "Se ha guardado el archivo 'robots.json' en el "
                                                "directorio raíz de la aplicación")
