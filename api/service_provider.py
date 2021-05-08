from typing import Callable

from dependency_injector import containers, providers

from api.api_repository.PersonRepository import *
from api.api_services.PersonService import *
from api.api_repository.PermissionRepository import *
from api.api_services.PermissionService import *
from api.api_repository.RoleRepository import *
from api.api_services.RoleService import *
from api.api_repository.AddressRepository import *
from api.api_services.AddressManagementService import *
from api.api_repository.DestinationRepository import *
from api.api_services.DestinationManagementService import *
from api.api_repository.journey_repository import *
from api.api_services.journey_management_service import *
from api.api_repository.vehicle_repository import *
from api.api_services.vehicle_management_service import *


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    person_repository: Callable[[], PersonRepository] = providers.Factory(
        DjangoORMPersonRepository
    )

    person_services: Callable[[], PersonManagementService] = providers.Factory(
        DefaultPersonManagementService,
        repository =person_repository
    )

    permission_repository: Callable[[], PermissionRepository] = providers.Factory(
        DjangoORMPermissionRepository
    )

    permission_services: Callable[[], PermissionManagementService] = providers.Factory(
        DefaultPermissionManagementService,
        repository = permission_repository
    )

    role_repository: Callable[[], RoleRepository] = providers.Factory(
        DjangoORMRoleRepository
    )

    role_permission: Callable[[], RoleManagementService] = providers.Factory(
        DefaultRoleManagementService,
        repository=role_repository
    )

    address_repository: Callable[[], AddressRepository] = providers.Factory(
        DjangoORMAddressRepository
    )

    address_services: Callable[[], AddressManagementService] = providers.Factory(
        DefaultAddressManagementService,
        repository=address_repository
    )

    destination_repository: Callable[[], DestinationRepository] = providers.Factory(
        DjangoORMDestinationRepository
    )

    destination_services: Callable[[], DestinationManagementService] = providers.Factory(
        DefaultDestinationManagementService,
        repository=destination_repository
    )

    vehicle_repository: Callable[[], VehicleRepository] = providers.Factory(
        DjangoORMVehicleRepository
    )

    vehicle_services: Callable[[], VehicleManagementService] = providers.Factory(
        DefaultVehicleManagementService,
        repository=vehicle_repository
    )

    journey_repository: Callable[[], JourneyRepository] = providers.Factory(
        DjangoORMJourneyRepository
    )

    journey_services: Callable[[], JourneyManagementService] = providers.Factory(
        DefaultJourneyManagementService,
        repository=journey_repository
    )

service_provider = Container()