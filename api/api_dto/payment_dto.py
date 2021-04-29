class MakePaymentDto:
    id: str
    booking_id: str
    amount: int
    status: str


class ListPaymentDto:
    id: str
    booking_id: str
    amount: int
    status: str


class GetPaymentDto:
    id: str
    booking_id: str
    amount: int
    status: str


class PaymentAmountDto:
    id: str
    amount: int


class PaymentStatusDto:
    id: str
    status: str


class PaymentDetailsDto:
    id: str
    booking_id: str
    amount: int
    status: str
