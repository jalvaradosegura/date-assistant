class DateAssistant:
    def __init__(self, date: str):
        self.date = date

    def __repr__(self):
        return f'DateAssistant({self.date!r})'

    def __str__(self):
        return self.date
