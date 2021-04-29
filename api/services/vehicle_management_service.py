from abc import ABCMeta, abstractmethod
from api.dto.vehicle_dto import *
from api.models import Vehicle
from api.repositories.vehicle_repository import VehicleRepository
from typing import List, Union


class VehicleManagementService(metaclass=ABCMeta):
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


class DefaultVehicleManagementService(VehicleManagementService):
    repository: VehicleRepository

    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def create_vehicle(self, model: CreateVehicleDto):
        try:
            self.repository.get_vehicle(registration_number=model.registration_number)
        except Vehicle.DoesNotExist:
            self.repository.create_vehicle(model)
            return True
        else:
            return False

    def edit_vehicle(self, vehicle_id: int, model: EditVehicleDto):
        return self.repository.edit_vehicle(vehicle_id, model)

    def list_vehicles(self) -> List[ListVehiclesDto]:
        return self.repository.list_vehicles()

    def get_vehicle(self, vehicle_id=None, registration_number=None) -> Union[GetVehicleDto, bool]:
        try:
            return self.repository.get_vehicle(vehicle_id, registration_number)
        except Vehicle.DoesNotExist:
            return False
