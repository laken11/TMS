

class CreateDestinationDto:
    id: int
    location: str
    description: str
    journey: str


class ListDestinationDto:
    location: str
    description: str
    journey: str


class DestinationDetailsDto:
    id: int
    location: str
    description: str
    journey: str


class EditDestination:
    location: str
    description: str
    journey: str


