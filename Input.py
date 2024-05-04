import json

from Bioreactor import Bioreactor
from PerfusionFilter import PerfusionFilter


class Input:
    def __init__(self, json_data):
        self.classes = {
            "Bioreactor": Bioreactor,
            "PerfusionFilter": PerfusionFilter
        }
        # self.instances = self.create_instances(json_data)
        self.instances = self.load_and_create_instances(json_data)

    def load_and_create_instances(self, filename):
        instances = {}
        with open(filename, 'r') as file:
            data = json.load(file)
            for key, params in data.items():
                if key in self.classes:
                    class_ = self.classes[key]
                    # Create an instance of the class using unpacking of the dictionary
                    instance = class_(**params)
                    instances[key] = instance
        return instances

    def create_instances(self, data):
        instances = {}
        for key, params in data.items():
            if key in self.classes:
                class_ = self.classes[key]
                # Create an instance of the class using unpacking of the dictionary
                instance = class_(**params)
                instances[key] = instance
        return instances
