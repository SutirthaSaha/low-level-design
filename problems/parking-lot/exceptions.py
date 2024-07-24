class SpotNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidVehicleException(Exception):
    def __init__(self, message):
        super().__init__(message)
