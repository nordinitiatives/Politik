class Legislation:
    _name = None
    _id = None
    _description = None
    _date = None
    _text = None
    _processed = False
    _evaluations = {}

    def __init__(self, name, ID, desc, date, text=None, values=None):
        self._name = name
        self._id = ID
        self._description = desc
        self._date = date
        self._text = text
        self._evaluations = values
    
    def process(self, ):
        pass

class Bill(Legislation):
    _house = None

    def __init__(self, name, ID, desc, date, house, text=None, values=None):
        super().__init__(name, ID, desc, date, text=text, values=values)
        self._house = house