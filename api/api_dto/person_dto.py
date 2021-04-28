from datetime import date


class CreatePersonDto:
    id: str
    email: str
    first_name: str
    last_name: str
    password: str
    confirm_password: str
    address: str
    telephone: str
    role: str
    permission: str
    date_created: date


class UpdatePersonDto:
    first_name: str
    last_name: str
    address: str
    telephone: str
    role: str
    permission: str
    date_updated: date


class ListPersonDto:
    first_name: str
    last_name: str
    address: str
    telephone: str
    role: str


class PersonDetailsDto:
    id: str
    email: str
    first_name: str
    last_name: str
    password: str
    confirm_password: str
    address: str
    telephone: str
    role: str
    permission: str
    date_created: date
    date_updated: date