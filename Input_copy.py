import json

from Bioreactor import Bioreactor
from GuardFilter import GuardFilter
from PerfusionFilter import PerfusionFilter
from Proa import Proa
from Susv import ContinuousSusv, SemiContinuousSusv


class InputCopy:

    classes = {
        'Bioreactor': Bioreactor,
        'PerfusionFilter': PerfusionFilter,
        'Susv1': ContinuousSusv,
        'ProaGuardFilter': GuardFilter,
        'Proa': Proa
    }

    def __init__(self, instances):
        self.instances = instances


class FileInput(InputCopy):

    def __init__(self, filename: str) -> None:

        instances = {}
        # Read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            self.data = data
            # Loop through the data and create instances of the classes
            for key, params in data.items():
                # Check if the class exists
                if key in InputCopy.classes:
                    class_ = InputCopy.classes[key]
                    # Create an instance of the class using unpacking of the dictionary
                    instance = class_(**params)
                    instances[key] = instance

            super().__init__(instances)

        return None

    class HttpInput(InputCopy):

        def __init__(self, request: json) -> None:

            instances = {}
            # Loop through the data and create instances of the classes
            for key, params in request.data.items():
                # Check if the class exists
                if key in InputCopy.classes:
                    class_ = InputCopy.classes[key]
                    # Create an instance of the class using unpacking of the dictionary
                    instance = class_(**params)
                    instances[key] = instance

            super().__init__(instances)

            return None
