from ChromResin import ProaChromResin
from ChromStep import ChromStep, ProaBufferStep, ProaLoadStep
from Column import ProaSbmColumn
from Proa import Proa


class Reader():

    @staticmethod
    def read_no_nested_dict(data: dict[any], key: str, object: any) -> any:

        for item, params in data.items():
            # Check if the class exists
            if item == key:
                # Create an instance of the class using unpacking of the dictionary
                instance = object(**params)

        return instance

    @staticmethod
    def read_proa(data, key):
        parentClass = Proa

        # Here we map JSON keys to their respective classes, including a tuple for steps
        childMappings = {
            'resin': ProaChromResin,
            'column': ProaSbmColumn,
            # Tuple of possible classes for steps
            'steps': (ProaBufferStep, ProaLoadStep)
        }

        parent_data = data[key]
        child_objs = {}

        # Process resin and column which are straightforward
        for json_key, child_class in childMappings.items():
            if json_key != 'steps':  # Skip steps here
                child_objs[json_key] = child_class(**parent_data[json_key])

        # Special handling for steps
        steps = []
        for step_data in parent_data['steps']:
            step_class = ProaLoadStep if step_data['name'] == "Loading" else ProaBufferStep
            step_obj = step_class(**step_data)
            steps.append(step_obj)
        child_objs['steps'] = steps

        # Pass unpacked objects to the parent class constructor
        instance = parentClass(
            column=child_objs['column'],
            resin=child_objs['resin'],
            steps=child_objs['steps'],
            efficiency=parent_data['efficiency']
        )

        return instance
