class Vote:
    _id = None
    _description = None
    _question = None
    _issue = None
    _date = None
    _body = None
    _log = {}
    _processed = False
    _impact = {}

    def __init__(self, id, desc, date, question, issue, body, log, values=None):
        self._id = id
        self._description = desc
        self._date = date
        self._question = question
        self._issue = issue
        self._body = body
        self._log = log
        self._impact = values

    def evaluate(self, values):
        self._impact = values
    
    @property
    def id(self):
        return self._id
    
    @property
    def ID(self):
        return self._id

    @property
    def desc(self):
        return self._description
    
    @property
    def date(self):
        return self._date

    @property
    def question(self):
        return self._question

    @property
    def issue(self):
        return self._issue

    @property
    def body(self):
        return self._body

    @property
    def log(self):
        return self._log

    @property
    def impact(self):
        return self._impact

    @property
    def processed(self):
        return self._processed
    @processed.setter
    def processed(self, value):
        if isinstance(value, bool):
            self._processed = value
        else:
            raise TypeError('Processed must be either True or False')
