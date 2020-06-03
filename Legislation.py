class Legislation:
    _name = None
    _id = None
    _description = None
    _date = None
    _text = None
    _evaluations = {}

    def __init__(self, name, ID, desc, date, text=None):
        self._name = name
        self._id = ID
        self._description = desc
        self._date = date
        self._text = text

class Bill(Legislation):
    _house = None