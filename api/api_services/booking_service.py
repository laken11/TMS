from abc import ABCMeta, abstractmethod
from typing import List

from api.api_dto.booking_dto import *
from api.models import Booking
from api.api_repository.booking_repository import BookingRepository


class BookingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def make_booking(self, model: MakeBookingDto):
        """create a booking object"""
        raise NotImplemented

    @abstractmethod
    def list_booking(self) -> List[ListBookingsDto]:
        """list all booking objects"""
        raise NotImplemented

    @abstractmethod
    def change_booking_status(self, model: ChangeBookingStatusDto):
        """change booking object's status"""
        raise NotImplemented

    @abstractmethod
    def change_pay_status(self, model: ChangePayStatusDto):
        """change booking object's pay status"""
        raise NotImplemented

    @abstractmethod
    def booking_details(self, booking_id: str) -> BookingDetailsDto:
        """show payment details"""
        raise NotImplemented


class DefaultBookingManagementService(BookingManagementService):
    repository: BookingRepository

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def make_booking(self, model: MakeBookingDto):
        try:
            result = self.repository.make_booking(model)
            if result:
                return result
        except Booking.DoesNotExist as e:
            raise e

    def list_booking(self) -> List[ListBookingsDto]:
        return self.repository.list_booking()

    def change_booking_status(self, model: ChangeBookingStatusDto):
        try:
            result = self.repository.change_booking_status(model)
            if result:
                return result
        except Booking.DoesNotExist as e:
            raise e

    def change_pay_status(self, model: ChangePayStatusDto):
        try:
            result = self.repository.change_pay_status(model)
            if result:
                return result
        except Booking.DoesNotExist as e:
            raise e

    def booking_details(self, booking_id: str) -> BookingDetailsDto:
        try:
            result = self.repository.booking_details(booking_id)
            if result:
                return result
        except Booking.DoesNotExist as e:
            raise e
