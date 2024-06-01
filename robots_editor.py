from editor import Editor


class RobotsEditor(Editor):
    def __init__(self, container):
        super().__init__(container)
        self.file_content = None


    def open_file(self):
        file_content = self.file_manager.open_file()
        if file_content is None:
            return
        self.file_content = file_content
        self.append_file_pieces(file_content)

    def save_file(self):
        pass
