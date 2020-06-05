class Politician:
# Base politician object. Should only be used if the politician being created has no other classification
    _first_name = None
    _middle_name = None
    _last_name = None
    _type = "Politician"
    _ID = None
    _phone = None
    _votes = {}
    _grades = {'Race':{'Black':0,'White':0,'Asain':0,'Brown':0,'Hispanic':0,'Native':0,'Other':0},
                'Gender':{'Male':0,'Female':0,'Transgender':0,'Other':0},
                'Age':{'0-17':0,'18-34':0,'35-50':0,'51-70':0,'71+':0},
                'MaritalStatus':{'Single':0,'Married':0,'Divorced/Widowed':0,'Remarried':0},
                'Education':{'SomeHS':0,'HSOnly':0,'SomeCollege':0,'Associates':0,'Bachelors':0,'Masters':0},
                'Income':{'Poverty':0,'Low':0,'Middle':0,'UpperMiddle':0,'High':0,'Max':0}}

    def __init__(self, fname, lname, phone, ID, mname=None):
        self._first_name = fname
        self._last_name = lname
        self._middle_name = mname
        self._phone = phone
        self._ID = ID

    def cast(self, vote, say=None):
    # Updates the politicans grades resulting from voted on a bill
        if say is None:
            for v in vote.log:
                if v == self._ID:
                    for key in vote.impact:
                        for demo in vote.impact[key]:
                            if vote.log[v].lower() == 'yea':
                                self._grades[key][demo] += vote.impact[key][demo]
                            elif vote.log[v].lower() == 'nay': 
                                self._grades[key][demo] -= vote.impact[key][demo]
                            else:
                                raise ValueError('A vote can only have a "yea" or"nay" value')
                        
        elif say.lower() == 'yea':
            for key in vote.impact:
                for demo in vote.impact[key]:
                    self._grades[key][demo] += vote.impact[key][demo]
        elif say.lower() == 'nay': 
            for key in vote.impact:
                for demo in vote.impact[key]:
                    self._grades[key][demo] -= vote.impact[key][demo]
        else:
            raise ValueError('A vote can only have a "yea" or"nay" value')

    def get_vote(self, vote_id):
    # Returns what the policician voted on a particular bill. If the politician hasn't voted on that
    # bill then this method will return None
        try:
            return self._votes[vote_id]
        except:
            return None

    def add_demographic(self, demographic):
    # Adds a demograpgic dict to the politician
        pass

    def get_grade(self, category, demo=None):
    # Returns the current grade of a singular demographic or a dictonary containing the grades for a
    # category of demo graphics
        if isinstance(demo, str):
            return self._grades[category][demo]
        elif isinstance(demo, list):
            grades = {}
            for d in demo:
              grades[d] = self._grades[category][d]
            return grades
        else:
            return self._grades[category]

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
    
    @property
    def votes(self):
        return self._votes
    
    @property
    def id(self):
        return self._ID
    
    @property
    def ID(self):
        return self._ID
    
    @property
    def grades(self):
        return self._grades
    
class Representative(Politician):
# Object for members of the House of Representatives
    _party = None
    _sworn_date = None
    _state = None
    _district = None

    def __init__(self, fname, lname, party, phone, date, state, district, ID, mname=None):
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
        self._ID = ID

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
# Object for members of the Senate
    _address = None
    _state = None
    _party = None

    def __init__(self, fname, lname, party, phone, state, address, ID):
        super().__init__(fname, lname, phone, ID)
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