class CreateJourneyDto:
    id: int
    vehicle_id: int
    name: str
    description: str
    price: float


class EditJourneyDto:
    id: int
    vehicle_id: int
    name: str
    description: str
    price: float


class ListJourneyDto:
    id: int
    vehicle_id: int
    name: str
    description: str


class GetJourneyDto:
    id: int
    vehicle_id: int
    name: str
    description: str
    price: float
