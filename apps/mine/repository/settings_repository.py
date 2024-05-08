from abc import ABC, abstractmethod


class ISettingRepository(ABC):
    @abstractmethod
    def save(self, setting):
        raise NotImplementedError

    @abstractmethod
    def find_by_mine(self, mine_id):
        raise NotImplementedError
