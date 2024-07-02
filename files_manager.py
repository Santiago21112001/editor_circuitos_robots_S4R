import json


class FilesManager:
    def __init__(self):
        pass

    def open_robots_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.check_robots_data_format(data)
        return data

    def check_robots_data_format(self, data):
        # Check that data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("El contenido debe ser un diccionario.")

        # Check that it has the 'robots' field and that it is a list
        if 'robots' not in data:
            raise ValueError("Falta el campo 'robots'.")
        if not isinstance(data['robots'], list):
            raise ValueError("El campo 'robots' debe ser una lista.")

        # Check each robot
        for robot in data['robots']:
            if not isinstance(robot, dict):
                raise ValueError("Cada elemento de 'robots' debe ser un diccionario.")
            if 'name' not in robot:
                raise ValueError("Falta el campo 'name' en un robot.")
            if 'elements' not in robot:
                raise ValueError("Falta el campo 'elements' en un robot.")
            if not isinstance(robot['elements'], list):
                raise ValueError("El campo 'elements' debe ser una lista en un robot.")

            # Check each element of the robot
            for element in robot['elements']:
                if not isinstance(element, dict):
                    raise ValueError("Cada elemento de 'elements' debe ser un diccionario.")
                if 'name' not in element:
                    raise ValueError("Falta el campo 'name' en un elemento.")
                if 'pin' not in element:
                    raise ValueError("Falta el campo 'pin' en un elemento.")

    def open_circuits_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.check_circuits_data_format(data)
        return data

    def check_circuits_data_format(self, data):
        # Check that data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("El contenido debe ser un diccionario.")

        # Check that it has the 'circuits' field and that it is a list
        if 'circuits' not in data:
            raise ValueError("Falta el campo 'circuits'.")
        if not isinstance(data['circuits'], list):
            raise ValueError("El campo 'circuits' debe ser una lista.")

        # Check each circuit
        for circuit in data['circuits']:
            if not isinstance(circuit, dict):
                raise ValueError("Cada elemento de 'circuits' debe ser un diccionario.")
            if 'name' not in circuit:
                raise ValueError("Falta el campo 'name' en un circuito.")
            if 'parts' not in circuit:
                raise ValueError("Falta el campo 'parts' en un circuito.")
            if not isinstance(circuit['parts'], list):
                raise ValueError("El campo 'parts' debe ser una lista en un circuito.")

            # Check each part of the circuit
            for part in circuit['parts']:
                if not isinstance(part, dict):
                    raise ValueError("Cada elemento de 'parts' debe ser un diccionario.")
                if 'type' not in part:
                    raise ValueError("Falta el campo 'type' en una parte del circuito.")
                if part['type'] not in ['straight', 'turn', 'three-way', 'four-way']:
                    raise ValueError(f"Tipo de parte inválido: {part['type']}")

                required_fields = []
                # Check specific fields for each type
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
                        raise ValueError(f"Falta el campo '{field}' en una parte del tipo '{part['type']}'")

    def save_file(self, content, file_path):
        with open(file_path, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Se ha guardado el archivo JSON como '{file_path}'.")
