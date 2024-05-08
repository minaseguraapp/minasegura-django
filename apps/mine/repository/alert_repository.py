from abc import ABC, abstractmethod


class IAlertRepository(ABC):
    @abstractmethod
    def find_by_mine(self, mine_id):
        raise NotImplementedError
