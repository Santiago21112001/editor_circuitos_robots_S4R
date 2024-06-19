import tkinter as tk
from tkinter import messagebox, simpledialog

from circuit_editor import CircuitEditor
from editor import Editor


class CircuitsEditor(Editor):

    DEFAULT_CIRCUIT_PARTS = [
        {
            "type": "straight",
            "x1": 100.0,
            "y1": 100.0,
            "orient": "x",
            "width": 20,
            "dist": 70,
            "scale": 0.2
        }]

    def __init__(self, container, width, height):
        super().__init__(container)
        self.editing_index = -1
        self.width = width
        self.height = height
        self.circuits = []
        self.circuit_editor = None
        self.create_widgets(self.frame)
        self.circuits.append({"name": "circuit", "parts": self.DEFAULT_CIRCUIT_PARTS})
        self.populate_listbox()

    def create_widgets(self, frame):
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=10, pady=10)

        self.add_button = tk.Button(frame, text="Crear", command=self.create_circuit)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_button = tk.Button(frame, text="Editar", command=self.edit_circuit)
        self.edit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_name_button = tk.Button(frame, text="Editar nombre", command=self.edit_circuit_name)
        self.edit_name_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(frame, text="Borrar", command=self.delete_circuit)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text="Guardar archivo", command=self.save_file, bg="green", fg="white")
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

    def create_circuit(self):
        name = simpledialog.askstring("Crear", "Introduzca el nombre:")
        if self.__name_invalid(name):
            return
        self.circuits.append({"name": name, "parts": self.DEFAULT_CIRCUIT_PARTS})
        self.populate_listbox()

    def edit_circuit(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un circuito para editar")
            return
        index = selected[0]
        self.editing_index = index
        circuit_data = self.circuits[index]
        self.circuit_editor = CircuitEditor(self, circuit_data)
        self.frame.pack_forget()  # Hide CircuitsEditor

    def edit_circuit_name(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un circuito para editar su nombre")
            return
        index = int(selected[0])
        name = simpledialog.askstring("Editar nombre", "Introduzca el nombre:")
        if self.__name_invalid(name):
            return
        self.circuits[index]["name"] = name
        self.populate_listbox()

    def __name_invalid(self, name: str):
        if not name:
            return True
        if self.__already_exists(name):
            messagebox.showerror("Error", "Ese nombre ya existe")
            return True
        return False

    def delete_circuit(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un elemento para borrar")
            return
        index = selected[0]
        self.listbox.delete(index)

    def open_this(self, circuit_data=None):
        if circuit_data:
            self.circuits[self.editing_index] = circuit_data
        self.circuit_editor.frame.destroy()
        self.circuit_editor = None
        self.frame.pack(fill="both", expand=True)

    def open_file(self):
        if self.circuit_editor:
            self.circuit_editor.open_file()
            return
        file_content = self.file_manager.open_file()
        message = check_format(file_content)
        if message != "":
            messagebox.showerror("Archivo inválido", message)
            return
        self.circuits = file_content["circuits"]
        self.populate_listbox()

    def save_file(self):
        if self.circuit_editor:
            self.circuit_editor.save_file()
            return
        if not self.circuits:
            messagebox.showerror("No se pudo guardar", "Debe haber al menos 1 circuito.")
            return
        content = {"circuits": self.circuits}
        file_path = "circuits.json"
        self.file_manager.save_file(content, file_path)
        messagebox.showinfo("Archivo guardado", "Se ha guardado el archivo 'circuits.json' en el "
                                                "directorio raíz de la aplicación.")

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for circuit in self.circuits:
            name: str = circuit["name"]
            self.listbox.insert(tk.END, name)

    def __already_exists(self, name):
        for circuit in self.circuits:
            if circuit["name"] == name:
                return True
        return False


def check_format(data):
    # Comprobar que data es un diccionario
    if not isinstance(data, dict):
        return "El contenido debe ser un diccionario."

    # Comprobar que tiene el campo 'circuits' y que es una lista
    if 'circuits' not in data:
        return "Falta el campo 'circuits'."
    if not isinstance(data['circuits'], list):
        return "El campo 'circuits' debe ser una lista."

    # Comprobar cada circuito
    for circuit in data['circuits']:
        if not isinstance(circuit, dict):
            return "Cada elemento de 'circuits' debe ser un diccionario."
        if 'name' not in circuit:
            return "Falta el campo 'name' en un circuito."
        if 'parts' not in circuit:
            return "Falta el campo 'parts' en un circuito."
        if not isinstance(circuit['parts'], list):
            return "El campo 'parts' debe ser una lista en un circuito."

        # Comprobar cada parte del circuito
        for part in circuit['parts']:
            if not isinstance(part, dict):
                return "Cada elemento de 'parts' debe ser un diccionario."
            if 'type' not in part:
                return "Falta el campo 'type' en una parte del circuito."
            if part['type'] not in ['straight', 'turn', 'polygon', '3way']:
                return f"Tipo de parte inválido: {part['type']}"

            # Inicializar required_fields
            required_fields = []
            # Comprobar campos específicos para cada tipo
            if part['type'] == 'straight':
                required_fields = ['x1', 'y1', 'orient', 'width', 'dist', 'scale']
            elif part['type'] == 'turn':
                required_fields = ['x1', 'y1', 'dist', 'start', 'extent', 'width', 'scale']
            elif part['type'] == 'polygon':
                required_fields = ['x1', 'y1', 'width', 'scale']
            elif part['type'] == '3way':
                required_fields = ['x1', 'y1', 'width', 'scale', 'orient']

            for field in required_fields:
                if field not in part:
                    return f"Falta el campo '{field}' en una parte del tipo '{part['type']}'"

    return ""
