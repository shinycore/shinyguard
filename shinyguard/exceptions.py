class CheckError(Exception):
    pass


class MissingDeviceError(CheckError):
    def __init__(self) -> None:
        super().__init__("No compatible builds found for the device")
