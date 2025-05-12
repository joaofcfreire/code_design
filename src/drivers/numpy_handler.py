import numpy
from typing import List

class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return float(self.__np.std(numbers))
