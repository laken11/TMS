from abc import ABCMeta, abstractmethod
from api.dto.vehicle_dto import *
from api.models import Vehicle
from typing import List, Union


class VehicleRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_vehicle(self, model: CreateVehicleDto):
        """Create Vehicle Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_vehicle(self, vehicle_id: int, model: EditVehicleDto):
        """Edit Vehicle Object"""
        raise NotImplementedError

    @abstractmethod
    def list_vehicles(self) -> List[ListVehiclesDto]:
        """List Vehicle Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_vehicle(self, vehicle_id=None, registration_number=None) -> Union[GetVehicleDto, bool]:
        """Get Vehicle Object"""
        raise NotImplementedError


class DjangoORMVehicleRepository(VehicleRepository):
    def create_vehicle(self, model: CreateVehicleDto):
        vehicle = Vehicle()
        vehicle.id = model.id
        vehicle.name = model.name
        vehicle.registration_number = model.registration_number
        vehicle.capacity = model.capacity
        vehicle.status = model.status
        vehicle.save()

    def edit_vehicle(self, vehicle_id: int, model: EditVehicleDto):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.name = model.name
        vehicle.capacity = model.capacity
        vehicle.status = model.status
        vehicle.save()

    def list_vehicles(self) -> List[ListVehiclesDto]:
        vehicles = Vehicle.objects.all()
        result: List[ListVehiclesDto] = []
        for vehicle in vehicles:
            item = ListVehiclesDto()
            item.id = vehicle.id
            item.name = vehicle.name
            item.capacity = vehicle.capacity
            item.status = vehicle.status
            result.append(item)
        return result

    def get_vehicle(self, vehicle_id=None, registration_number=None) -> Union[GetVehicleDto, bool]:
        try:
            if vehicle_id is not None:
                vehicle = Vehicle.objects.get(id=vehicle_id)
            elif registration_number is not None:
                vehicle = Vehicle.objects.get(registration_number=registration_number)
            item = GetVehicleDto()
            item.id = vehicle.id
            item.name = vehicle.name
            item.registration_number = vehicle.registration_number
            item.capacity = vehicle.capacity
            item.status = vehicle.status
            return item
        except Vehicle.DoesNotExist:
            return False
