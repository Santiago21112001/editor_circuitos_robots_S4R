class Robot:
    BANNED_NAMES = ["servo left", "servo right", "trig", "echo", "light 2", "light 3"]

    def __init__(self, name: str):
        self.__data = {
            "name": name,
            "elements": [
                {
                    "name": "servo left",
                    "pin": "8"
                },
                {
                    "name": "servo right",
                    "pin": "9"
                },
                {
                    "name": "light 2",
                    "pin": "2"
                },
                {
                    "name": "light 3",
                    "pin": "3"
                },
                {
                    "name": "trig",
                    "pin": "4"
                },
                {
                    "name": "echo",
                    "pin": "5"
                }
            ]
        }
        self.__ext_lights = 0

    def get_name(self):
        return self.__data["name"]

    def get_elements(self):
        return self.__data["elements"]

    def get_data(self):
        return self.__data.copy()

    def set_name(self, name: str):
        self.__data["name"] = name

    def set_element(self, index: int, pin: str):
        # Check that the pin is a number, although it's a string
        if not pin.isdigit():
            raise ValueError("El pin del elemento debe ser un número.")
        # Check that the pin isn't already taken by another element
        elements = self.__data["elements"]
        for e in elements:
            if e["pin"] == pin:
                raise ValueError("Ya hay un elemento con ese pin.")

        self.__data["elements"][index]["pin"] = pin

    def add_light(self) -> None:
        if self.__ext_lights == 2:
            raise ValueError("No pueden haber más de 4 sensores de luz.")

        if self.__ext_lights == 1 and self.__contains_light_x(1):
            # Exterior derecho
            self.__data["elements"].append({"name": "light 4", "pin": "11"})
        else:
            # Exterior izquierdo
            self.__data["elements"].append({"name": "light 1", "pin": "10"})
        self.__ext_lights += 1

    def delete_light(self, index: int) -> None:
        if self.__ext_lights == 0:
            raise ValueError("No pueden haber menos de 2 sensores de luz.")
        if self.__data["elements"][index]["name"] in self.BANNED_NAMES:
            raise ValueError("Error", "No puedes borrar ese elemento, sólo los sensores de luz exteriores")

        self.__data["elements"].pop(index)
        self.__ext_lights -= 1

    def __contains_light_x(self, x):
        target_name = f"light {x}"
        elements = self.__data["elements"]
        for e in elements:
            if e["name"] == target_name:
                return True
        return False

    def set_data(self, data):
        self.__data = data
