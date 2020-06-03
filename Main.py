from lxml import etree
import requests
import time
import pickle
import Politicians
import os
import tempfile

def main():
    start_time = time.time()
    path = "C:/Users/Masiah/Documents/GitHub/Politik/"

    for path2, dirs, files in os.walk(path+'Senators/'):
        for name in files:
            politician = pickle.load(open(path+'Senators/'+name, "rb")) 
            print(politician.name)

    print("--- %s seconds ---" % (time.time()-start_time))

def create_representatives(path):
# Creates representative objects for each house member and saves them to the provided path
    house_link = "http://clerk.house.gov/xml/lists/MemberData.xml"
    tree = etree.parse(house_link)
    root = tree.getroot()
    members = root.find("members")
    for c in members:
        politician = Politicians.Representative(c[1].find("firstname").text, c[1].find("lastname").text,
                                c[1].find("party").text, c[1].find("phone").text, 
                                c[1].find("sworn-date").text, c[1].find("state")[0].text,
                                c[1].find("district").text, c[1].find("bioguideID").text,
                                mname = c[1].find("middlename").text)
        pickle.dump(politician, open(path+'Members/'+politician.name, "wb"))

def create_senators(path):
# Creates senator objects for each senator and saves them to provided path. This fucntion gets the xml
# file from the govt website using requests because the request needs a browser header in order to
# retrieve the xml data
    senate_link = "https://www.senate.gov/general/contact_information/senators_cfm.xml"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(senate_link, headers = header)  

    # The following section of code write the xml to a file and then deletes the file after the xml is
    # pared from the file
    with open('Temp.xml', 'w') as f:
        f.write(r.text)
    with open('Temp.xml') as f:
        tree = etree.parse(f)
    os.remove('Temp.xml')

    root = tree.getroot()
    members = root.findall('member')

    for m in members:
        politician = Politicians.Senator(m.find("first_name").text, m.find("last_name").text,
                                m.find("party").text, m.find("phone").text, 
                                m.find("state").text, m.find("address").text, 
                                m.find("bioguide_id").text)
        pickle.dump(politician, open(path+'Senators/'+politician.name, "wb"))

def create_bill(xml):
    pass

if __name__ == "__main__":
	main()