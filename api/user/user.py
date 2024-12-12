class User:

    def __init__(self, text):
        self.text = text
        self.metadata = vars(Metadata())

class Metadata:
    def __init__(self):
        self.api = "GHW_DATA Project"
        self.branch = "set-up-backend"
