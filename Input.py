import json

from Bioreactor import Bioreactor
from PerfusionFilter import PerfusionFilter
from Susv import ContinuousSusv, SemiContinuousSusv


class Input:

    classes = {
        "Bioreactor": Bioreactor,
        "PerfusionFilter": PerfusionFilter,
        "Susv1": ContinuousSusv
    }

    def __init__(self, instances):
        self.instances = instances


class FileInput(Input):

    def __init__(
        self,
        filename: str
    ) -> None:

        instances = {}
        # Read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Loop through the data and create instances of the classes
            for key, params in data.items():
                # Check if the class exists
                if key in Input.classes:
                    class_ = Input.classes[key]
                    # Create an instance of the class using unpacking of the dictionary
                    instance = class_(**params)
                    instances[key] = instance

            super().__init__(instances)

        return None

    class HttpInput(Input):

        def __init__(
            self,
            request: json
        ) -> None:

            instances = {}
            # Loop through the data and create instances of the classes
            for key, params in request.data.items():
                # Check if the class exists
                if key in Input.classes:
                    class_ = Input.classes[key]
                    # Create an instance of the class using unpacking of the dictionary
                    instance = class_(**params)
                    instances[key] = instance

            super().__init__(instances)

            return None
