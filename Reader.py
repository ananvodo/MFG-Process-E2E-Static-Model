class Reader():

    @staticmethod
    def read_no_nested_dict(data: dict[any], key: str, object: any) -> any:

        for item, params in data.items():
            # Check if the class exists
            if item == key:
                # Create an instance of the class using unpacking of the dictionary
                instance = object(**params)

        return instance
