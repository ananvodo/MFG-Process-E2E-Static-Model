import json

from Bioreactor import Bioreactor
from PerfusionFilter import PerfusionFilter


class Input:

    classes = {
        "Bioreactor": Bioreactor,
        "PerfusionFilter": PerfusionFilter
    }

    def __init__(self, instances):
        self.instances = instances

    @classmethod
    def from_file(cls, filename):
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

        return cls(instances)

    @classmethod
    def from_http(cls, data):
        instances = {}
        # Loop through the data and create instances of the classes
        for key, params in data.items():
            # Check if the class exists
            if key in Input.classes:
                class_ = Input.classes[key]
                # Create an instance of the class using unpacking of the dictionary
                instance = class_(**params)
                instances[key] = instance

        return cls(instances)
