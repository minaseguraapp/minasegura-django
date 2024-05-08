from apps.mine.repository.measurement_repository import IMeasurementRepository


class MemoryMeasurementRepository(IMeasurementRepository):
    def __init__(self):
        self._measurements = []

    def save(self, measurement):
        self._measurements.append(measurement)

    def find_all(self):
        return self._measurements
