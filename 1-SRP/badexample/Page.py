class Page:
    def __init__(self, number: int, content: str):
        self.number = number
        self.content = content

    def get_number(self):
        return self.number

    def get_content(self):
        return self.content
