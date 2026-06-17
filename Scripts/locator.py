from typing import Type, TypeVar
T = TypeVar('T')

class Locator:
    _services = {}

    @classmethod
    def register(cls, service_type: Type[T], service_instance: T):
        if cls.get(service_type) is None:
            cls._services[service_type] = service_instance

    @classmethod
    def unregister(cls, service_type: Type[T]):
        if cls.get(service_type) is not None:
            del cls._services[service_type]

    @classmethod
    def get(cls, service_type: Type[T]) -> T:
        return cls._services[service_type]
