from typing import Callable

from dependency_injector import containers, providers

from api.api_repository.PersonRepository import *
from api.api_repository.PermissionRepository import *
from api.api_repository.RoleRepository import *
from api.api_repository.AddressRepository import *
from api.api_repository.DestinationRepository import *
from api.api_repository.journey_repository import *
from api.api_repository.vehicle_repository import *


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    person_repository: Callable[[], PersonRepository] = providers.Factory(
        DjangoORMPersonRepository
    )

    permission_repository: Callable[[], PermissionRepository] = providers.Factory(
        DjangoORMPermissionRepository
    )

    role_repository: Callable[[], RoleRepository] = providers.Factory(
        DjangoORMRoleRepository
    )

    address_repository: Callable[[], AddressRepository] = providers.Factory(
        DjangoORMAddressRepository
    )

    destination_repository: Callable[[], DestinationRepository] = providers.Factory(
        DjangoORMDestinationRepository
    )

    vehicle_repository: Callable[[], VehicleRepository] = providers.Factory(
        DjangoORMVehicleRepository
    )

    journey_repository: Callable[[], JourneyRepository] = providers.Factory(
        DjangoORMJourneyRepository
    )

service_provider = Container()