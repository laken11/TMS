from abc import ABCMeta, abstractmethod
from typing import List

from api.api_dto.payment_dto import *
from api.models import Payment
from api.api_repository.payment_repository import PaymentRepository


class PaymentManagementService(metaclass=ABCMeta):
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


class DefaultPaymentManagementService(PaymentManagementService):
    repository: PaymentRepository

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def make_payment(self, model: MakePaymentDto):
        try:
            result = self.repository.make_payment(model)
            if result:
                return result
        except Payment.DoesNotExist as e:
            raise e

    def list_payment(self) -> List[ListPaymentDto]:
        return self.repository.list_payment()

    def change_payment_status(self, model: PaymentStatusDto):
        try:
            result = self.repository.change_payment_status(model)
            if result:
                return result
        except Payment.DoesNotExist as e:
            raise e

    def payment_details(self, payment_id: str) -> PaymentDetailsDto:
        try:
            result = self.repository.payment_details(payment_id)
            if result:
                return result
        except Payment.DoesNotExist as e:
            raise e
