from lxml import etree
import requests
import time
import pickle
import Politicians
import os
from Votes import Vote

def main():
    start_time = time.time()
    path = "/home/mbando/grind/Politik View/"
    house_vote = "http://clerk.house.gov/evs/2019/roll701.xml"
    senate_vote = "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1162/vote_116_2_00092.xml"
    sample_values = {'Race':{'Black':5,'Hispanic':3},
                    'Age':{'0-17':6,'18-34':1},
                    'Income':{'High':-5,'Max':-8}}

    create_senators()
    create_representatives()
    # create_vote(senate_vote, 'senate', sample_values)
    # test_vote = pickle.load(open('/home/mbando/grind/Politik View/Votes/Senate/92', 'rb'))
    # process_vote(test_vote)

    # for path2, dirs, files in os.walk('/home/mbando/grind/Politik View/Senators/'):
    #     for name in files:
    #         politician = pickle.load(open('/home/mbando/grind/Politik View/Senators/'+name, 'rb')) 
    #         print('%s: %s' % (politician.name, politician.get_grade('Income',['High','Max'])))

    print("--- %s seconds ---" % (time.time()-start_time))

def create_representatives():
# Creates representative objects for each house member and saves them to the provided path
    house_link = "http://clerk.house.gov/xml/lists/MemberData.xml"
    tree = etree.parse(house_link)
    root = tree.getroot()
    members = root.find("members")
    for c in members:
        if (c[1].find("bioguideID").text) == None:
        # This skips vacant positions due to resignation
            continue
        politician = Politicians.Representative(c[1].find("firstname").text, c[1].find("lastname").text,
                                c[1].find("party").text, c[1].find("phone").text, 
                                c[1].find("sworn-date").text, c[1].find("state")[0].text,
                                c[1].find("district").text, c[1].find("bioguideID").text,
                                mname = c[1].find("middlename").text)
        pickle.dump(politician, open('Representatives/'+politician.id, "wb"))

def create_senators():
# Creates senator objects for each senator and saves them to provided path.
    senate_link = "https://www.senate.gov/general/contact_information/senators_cfm.xml"
    senate_link2 = "https://www.senate.gov/legislative/LIS_MEMBER/cvc_member_data.xml"
    tree = fake_browser_visit(senate_link)
    tree2 = fake_browser_visit(senate_link2)
    root = tree.getroot()
    root2 = tree2.getroot()
    members = root.findall('member')
    senators = root2.findall('senator')
    
    id_link = {}
    for s in senators:
        id_link[s.find('bioguideId').text] = s.get('lis_member_id')

    for m in members:
        if m.find("bioguide_id").text == None:
            raise SystemError('Might be vacant position')
        politician = Politicians.Senator(m.find("first_name").text, m.find("last_name").text,
                                m.find("party").text, m.find("phone").text, 
                                m.find("state").text, m.find("address").text, 
                                id_link[m.find("bioguide_id").text])
        pickle.dump(politician, open('Senators/'+politician.ID, "wb"))

def create_vote(xml, body, values=None):
# Creates a vote object from xml data and given demograhic values(if any) and saves it to the given path
    if body.lower() == 'house':
        tree = etree.parse(xml)
        root = tree.getroot()

        id = root[0].find('rollcall-num').text
        issue = root[0].find('legis-num').text
        question = root[0].find('vote-question').text
        date = root[0].find('action-date').text
        desc = root[0].find('vote-desc').text

        log = {}
        for c in root[1]:
            log[c[0].get('name-id')] = c[1].text

        vote = Vote(id, desc, date, question, issue, body.lower(), log, values=values)
        pickle.dump(vote, open('/home/mbando/grind/Politik View/Votes/House/'+vote.id, 'wb'))
    elif body.lower() == 'senate':
        tree = fake_browser_visit(xml)
        root = tree.getroot()

        id = root.find('vote_number').text
        issue = root.find('document').find('document_name').text
        question = root.find('question').text
        date = root.find('vote_date').text
        desc = root.find('vote_document_text').text

        log = {}
        for m in root.find('members'):
            log[m.find('lis_member_id').text] = m.find('vote_cast').text

        vote = Vote(id, desc, date, question, issue, body.lower(), log, values=values)
        pickle.dump(vote, open('Senate/'+vote.id, 'wb'))

def process_vote(vote):
# Takes vote objects and applies them to politician objects
    if vote.processed == False:
        if vote.body.lower() == 'house':
            for id in vote.log:
                try:
                    politician = pickle.load(open('/home/mbando/grind/Politik View/Representatives/'+id, 'rb'))
                    politician.cast(vote, vote.log[id])
                    pickle.dump(politician, open('/home/mbando/grind/Politik View/Representatives/'+id, 'wb'))
                    print('%s: %s' % (politician.name, politician.get_grade('Race',['Black','Hispanic'])))
                except:
                    continue
            vote.processed = True
            pickle.dump(vote, open('/home/mbando/grind/Politik View/Votes/House/'+vote.id, 'wb'))
        elif vote.body.lower() == 'senate':
            for id in vote.log:
                try:
                    politician = pickle.load(open('/home/mbando/grind/Politik View/Senators/'+id, 'rb'))
                    politician.cast(vote, vote.log[id])
                    pickle.dump(politician, open('/home/mbando/grind/Politik View/Senators/'+id, 'wb'))
                    print('%s: %s' % (politician.name, politician.get_grade('Race',['Black','Hispanic'])))
                except:
                    continue
            vote.processed = True
            pickle.dump(vote, open('/home/mbando/grind/Politik View/Votes/Senate/'+vote.id, 'wb'))
    else:
        raise SystemError('This vote was already processed')

def fake_browser_visit(xml_link):
# The senate website apparently does not allow for programs to retrieve xml data so this function request the xml data with a browser header and returns
# an xml tree object
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(xml_link, headers = header)  

    # The following section of code write the xml to a file and then deletes the file after the xml is
    # pared from the file
    with open('Temp.xml', 'w') as f:
        f.write(r.text)
    with open('Temp.xml') as f:
        tree = etree.parse(f)
    os.remove('Temp.xml')
    
    return tree

if __name__ == "__main__":
	main()