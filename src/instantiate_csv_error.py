class InstantiateCSVError(Exception):
    def __init__(self, file_path):
        super().__init__(f"Файл {file_path.split('/')[-1]} поврежден")

