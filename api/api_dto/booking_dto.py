class MakeBookingDto:
    id: int
    reference: str
    status: str
    pay: str


class GetBookingDto:
    id: int
    reference: str
    status: str
    pay: str


class ChangeBookingStatusDto:
    reference: str
    status: str


class ChangePayStatusDto:
    id: int
    reference: str
    status: str


class ListBookingsDto:
    reference: str
    status: str
    pay: str


class BookingDetailsDto:
    id: int
    reference: str
    status: str
    pay: str
