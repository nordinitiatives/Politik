from lxml import etree
import requests
import time
import pickle
import Politicians
import os

def main():
    start_time = time.time()
    path = "C:/Users/Masiah/Documents/GitHub/Politik/Members/"
    house_link = "http://clerk.house.gov/xml/lists/MemberData.xml"
    senate_link = "https://www.senate.gov/general/committee_membership/committee_memberships_SSAP.xml"
    senate_link2 = "https://www.senate.gov/general/contact_information/senators_cfm.xml"

    # tree = etree.parse(house_link)
    # root = tree.getroot()
    # members = root.find("members")
    # for c in members:
    #    politician = Politicians.Representative(c[1].find("firstname").text, c[1].find("lastname").text,
    #                             c[1].find("party").text, c[1].find("phone").text, 
    #                             c[1].find("sworn-date").text, c[1].find("state")[0].text,
    #                             c[1].find("district").text, mname = c[1].find("middlename").text)
    #     pickle.dump(politician, open(path+politician.name, "wb"))
    
    # r = requests.get(senate_link2)
    # print(r.text)
    # tree = etree.parse(senate_link)
    # root = tree.getroot()
    # print(len(root))

    # for path2, dirs, files in os.walk(path):
    #     for name in files:
    #         politician = pickle.load(open(path+name, "rb")) 
    #         print(politician.district)

    print("--- %s seconds ---" % (time.time()-start_time))

if __name__ == "__main__":
	main()