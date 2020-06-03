class Politician:
    _first_name = None
    _middle_name = None
    _last_name = None
    _type = "Politician"
    _phone = None

    def __init__(self, fname, lname, phone, mname=None):
        self._first_name = fname
        self._last_name = lname
        self._middle_name = mname
        self._phone = phone

    @property
    def name(self):
        if self._middle_name is not None:
            return "%s, %s %s" % (self._last_name, self._first_name, self._middle_name)
        else: 
            return "%s, %s" % (self._last_name, self._first_name)

    @property
    def firstname(self):
        return self._first_name

    @property
    def middlename(self):
        return self._middle_name

    @property
    def lastname(self):
        return self._last_name
    
    @property
    def type(self):
        return self._type
    
class Representative(Politician):
    _party = None
    _sworn_date = None
    _state = None
    _district = None

    def __init__(self, fname, lname, party, phone, date, state, district, mname=None):
        self._first_name = fname
        if mname is not None:
            try:
                x = mname.index('"')
                self._middle_name = mname[:x]
            except:
                self._middle_name = mname
        self._last_name = lname
        self._party = party
        self._phone = phone
        self._sworn_date = date
        self._state = state
        self._district = district
        self._type = "Representative"

    def vote(bill, favor):
        pass

    @property
    def party(self):
        return self._party
    
    @property
    def phone(self):
        return self._phone
    
    @property
    def sworn_date(self):
        return self._sworn_date
    
    @property
    def state(self):
        return self._state
    
    @property
    def district(self):
        return self._district

class Senator(Politician):
    _address = None
    _state = None
    _party = None

    def __init__(self, fname, lname, party, phone, state, address, midname=None):
        super(fname, lname, phone, mname=midname)
        self._address = address
        self._state = state
        self._party = party
        self._type = "Senator"
    
    @property
    def address(self):
        return self._address
    
    @property
    def state(self):
        return self._state
    
    @property
    def party(self):
        return self._party