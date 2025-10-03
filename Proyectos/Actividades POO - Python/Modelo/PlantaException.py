class PlantaException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
