import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

from circuit_pieces_editor import CircuitPiecesEditor
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
        self.circuit_parts_editor = None
        self.create_widgets(self.frame)
        self.circuits.append({"name": "circuit", "parts": self.DEFAULT_CIRCUIT_PARTS})
        self.populate_listbox()

    def create_widgets(self, frame):
        self.title_label = tk.Label(self.frame, text="Se está usando el editor de CIRCUITOS. Para cambiar al de robots, "
                                               "seleccione la opción de menú 'Cambiar de editor.'")
        self.title_label.pack(side=tk.TOP, padx=5, pady=5)

        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=10, pady=10)

        self.add_circuit_button = tk.Button(frame, text="Crear", command=self.add_circuit)
        self.add_circuit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_circuit_button = tk.Button(frame, text="Editar", command=self.edit_circuit)
        self.edit_circuit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_circuit_name_button = tk.Button(frame, text="Editar nombre", command=self.edit_circuit_name)
        self.edit_circuit_name_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_circuit_button = tk.Button(frame, text="Borrar", command=self.delete_circuit)
        self.delete_circuit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text="Guardar archivo", command=self.save_file, bg="green", fg="white")
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_circuit(self):
        name = simpledialog.askstring("Crear", "Introduzca el nombre:")
        if self.__is_name_invalid(name):
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
        self.circuit_parts_editor = CircuitPiecesEditor(self, circuit_data)
        self.frame.pack_forget()  # Hide CircuitsEditor

    def edit_circuit_name(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un circuito para editar su nombre")
            return
        index = int(selected[0])
        name = simpledialog.askstring("Editar nombre", "Introduzca el nombre:")
        if self.__is_name_invalid(name):
            return
        self.circuits[index]["name"] = name
        self.populate_listbox()

    def __is_name_invalid(self, name: str):
        if not name:
            return True
        for circuit in self.circuits:
            if circuit["name"] == name:
                messagebox.showerror("Error", "Ese nombre ya existe")
                return True
        return False

    def delete_circuit(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un elemento para borrar")
            return
        index = selected[0]
        del self.circuits[index]
        self.populate_listbox()

    def open_this(self, circuit_data=None):
        if circuit_data:
            self.circuits[self.editing_index] = circuit_data
        self.circuit_parts_editor.frame.destroy()
        self.circuit_parts_editor = None
        self.frame.pack(fill="both", expand=True)

    def open_file(self):
        if self.circuit_parts_editor:
            messagebox.showerror("Error", "Para abrir un archivo tienes que volver a la ventana anterior.")
            return
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if not file_path:
            return
        try:
            file_content = self.file_manager.open_circuits_file(file_path)
        except ValueError as err:
            messagebox.showerror("Archivo inválido", str(err))
            return
        self.circuits = file_content["circuits"]
        self.populate_listbox()

    def save_file(self):
        if self.circuit_parts_editor:
            messagebox.showerror("Error", "Para guardar un archivo tienes que volver a la ventana anterior.")
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

    def destroy(self):
        if self.circuit_parts_editor:
            self.circuit_parts_editor.frame.destroy()
        self.frame.destroy()
