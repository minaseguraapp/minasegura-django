from abc import ABC, abstractmethod


class IMeasurementRepository(ABC):
    @abstractmethod
    def save(self, measurement):
        raise NotImplementedError

    @abstractmethod
    def find_by_mine(self, mine_id, zone_id, type_name):
        raise NotImplementedError
