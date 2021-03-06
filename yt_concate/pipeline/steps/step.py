from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, utils, inputs, data):
        pass


class StepException(Exception):
    pass
