class CreateVehicleDto:
    id: int
    name: str
    registration_number: int
    capacity: int
    status: str


class EditVehicleDto:
    id: int
    name: str
    capacity: int
    status: str


class ListVehiclesDto:
    id: int
    name: str
    capacity: int
    status: str


class GetVehicleDto:
    id: int
    name: str
    registration_number: int
    capacity: int
    status: str
