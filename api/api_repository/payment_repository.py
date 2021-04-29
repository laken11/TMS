from abc import ABCMeta, abstractmethod
from typing import List

from api.api_dto.payment_dto import *
from api.models import Payment


class PaymentRepository(metaclass=ABCMeta):
    @abstractmethod
    def make_payment(self, model: MakePaymentDto):
        """make payment object"""
        raise NotImplemented

    @abstractmethod
    def list_payment(self) -> List[ListPaymentDto]:
        """list payment objects"""
        raise NotImplemented

    @abstractmethod
    def change_payment_status(self, model: PaymentStatusDto):
        """change payment object's status"""
        raise NotImplemented

    @abstractmethod
    def payment_details(self, payment_id: str) -> PaymentDetailsDto:
        """show payment details"""
        raise NotImplemented


class DjangoORMPaymentRepository(PaymentRepository):
    def make_payment(self, model: MakePaymentDto):
        payment = Payment()
        payment.id = model.id
        payment.status = model.status
        payment.amount = model.amount
        payment.booking_id = model.booking_id
        payment.save()

    def list_payment(self) -> List[ListPaymentDto]:
        payments = Payment.objects.filter().values('id', 'booking_id', 'amount', 'status')
        results: List[ListPaymentDto] = []
        for payment in payments:
            item = ListPaymentDto()
            item.status = payment['status']
            item.id = payment['id']
            item.booking_id = payment['booking_id']
            item.amount = payment['amount']
            results.append(item)
        return results

    def change_payment_status(self, model: PaymentStatusDto):
        payment = Payment.objects.get(id=model.id)
        payment.status = model.status
        payment.save()

    def payment_details(self, payment_id: str) -> PaymentDetailsDto:
        payment = Payment.objects.values('status', 'amount', 'booking_id').get(id=payment_id)
        item = PaymentDetailsDto()
        item.status = payment.status
        item.amount = payment.amount
        item.booking_id = payment.booking_id
        return item
