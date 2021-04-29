import datetime


class CreateAddressDto:
    id: int
    line: str
    postal_code: int
    city: str
    state: str
    country: str


class ListAddressDto:
    line: str
    postal_code: int
    city: str
    state: str
    country: str


class AddressDetailsDto:
    id: int
    line: str
    postal_code: int
    city: str
    state: str
    country: str


class EditAddressDto:
    line: str
    postal_code: int
    city: str
    state: str
    country: str
