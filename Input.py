import json


class FileInput():

    def __init__(self, filename: str) -> None:

        with open(filename, 'r') as file:
            data = json.load(file)
            self.data = data

        return None


# class HttpInput():

#     def __init__(self, request: json) -> None:
#         self.data = request.data

#         return None
