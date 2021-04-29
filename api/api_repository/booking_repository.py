from abc import ABCMeta, abstractmethod
from typing import List

from api.api_dto.booking_dto import *
from api.models import Booking


class BookingRepository(metaclass=ABCMeta):
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


class DjangoORMBookingRepository(BookingRepository):

    def make_booking(self, model: MakeBookingDto):
        item = Booking()
        item.id = model.id
        item.status = model.status
        item.pay = model.pay
        item.reference = model.reference
        item.save()

    def list_booking(self) -> List[ListBookingsDto]:
        bookings = Booking.objects.filter().values('pay', 'status', 'reference')
        result: List[ListBookingsDto] = []
        for booking in bookings:
            item = ListBookingsDto()
            item.pay = booking['pay']
            item.status = booking['status']
            item.reference = booking['reference']
            result.append(item)
        return result

    def change_booking_status(self, model: ChangeBookingStatusDto):
        booking = Booking.objects.get(reference=model.reference)
        booking.status = model.status
        booking.save()

    def change_pay_status(self, model: ChangeBookingStatusDto):
        booking = Booking.objects.get(reference=model.reference)
        booking.status = model.status
        booking.save()

    def booking_details(self, booking_id: str) -> BookingDetailsDto:
        booking = Booking.objects.values('id', 'reference', 'status', 'pay').get(id=booking_id)
        item = BookingDetailsDto()
        item.status = booking.status
        item.amount = booking.amount
        item.booking_id = booking.booking_id
        return item
