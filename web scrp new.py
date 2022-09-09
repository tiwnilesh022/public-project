#  Importing required modules

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

'''Here we have initialized the chrome Options and we are using it in headless mode,i.e. the window of chrome will 
not popup
'''
options = Options()
options.add_argument('--headless')  # configuring chrome to run in headless mode
options.add_argument('--disable-gpu')  # disabling the gpu acceleration
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)  # Instantiating the chromedriver

number = int(
    input("Enter how many IP Addresses you want to search: "))  # taking input from the user of number of IPs to search
IPs = []  # Empty list of IPs

#  Taking input from the user "number" times
for i in range(number):
    IPs.append(input("Enter the IP Address: "))

ips = ",".join(str(e) for e in
               IPs)  # separating each IP address taken from the user with " ," so that it can be passed to the URL.
url = f"https://www.maxmind.com/en/geoip2-precision-demo?ip_address={ips}"  # Base url for GEO IP search
driver.get(url)  # requesting the driver to open the url
time.sleep(5)  # putting the code to halt for 5 seconds for the table data to be loaded
soup = BeautifulSoup(driver.page_source, 'html.parser')  # Instantiating the Beautiful Soup object in a vairable
# called "soup".
table = soup.find("table")  # Finding all the tables and storing them in "table"
rows = table.findAll('tr')  # Finding all the rows
table_headings = table.findAll('th')  # Finding all the Table headers

'''The basic concept used here is that after our data loads we get the source code of the page and pass it to the 
BeautifulSoup Class so that we can find what we're looking for, here we are seeking the table data.
For each of the column we have defined 11 lists in which the values of their fields will be entered.

'''



IP_Address = []
Country_Code = []
Location = []
Network = []
Postal_Code = []
Approximate_Coordinates = []
Accuracy_Radius_km = []
ISP = []
Organization = []
Domain = []
Metro_Code = []
helloo = []
data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]  # Credit - StackOverflow, Finding
#  all the table data to and then storing them as a list corresponding to each IP address


# Here we have applied a loop for assigning the table columns values to their corresponding lists so that they can be
# used further in making the dataframe with the help of pandas.

for i in data:  # This loop iterates through the list of all IP search details which is a list
    try:
        # The 'k' loop is for assigning appropriate values extracted from the table data to the lists that have been
        # defined above, for example upon observing the data variables' contents we find that IP is at the first index,
        # so, we append the first element (IP) in the IP_Address list, same goes for all the lists.

        for k in range(12):
            if k == 0:
                IP_Address.append(i[k][0])
            if k == 1:
                Country_Code.append(i[k][0])
            if k == 2:
                Location.append(i[k][0])
            if k == 3:
                Network.append(i[k][0])
            if k == 4:
                if i[k]:
                    Postal_Code.append(i[k][0])
                else:
                    Postal_Code.append("-")
            if k == 5:
                Approximate_Coordinates.append(f"{i[k][0]} {i[k][1]}")
            if k == 6:
                Accuracy_Radius_km.append(i[k][0])
            if k == 7:
                ISP.append(i[k][0])
            if k == 8:
                Organization.append(i[k][0])
            if k == 9:
                # print(i[k])
                if i[k]:
                    Domain.append(i[k][0])
                    # print(Domain)
                else:
                    Domain.append('-')
            if k == 10:
                if i[k]:
                    Metro_Code.append(i[k][0])
                else:
                    Metro_Code.append('-')

    except IndexError as e:
        pass

'''Lists are being converted in to Pandas Series here because they are compatible with the Dataframe object of Pandas 
module '''

s0 = pd.Series(IP_Address, name="IP_Address")   # Here we have converted the IP_Address list into a Pandas Series so
# that the Pandas module can infer these lists and make a dataframe, same goes for all the successive series

s1 = pd.Series(Country_Code, name="Country_Code")
s2 = pd.Series(Location, name="Location")
s3 = pd.Series(Network, name="Network")
s4 = pd.Series(Postal_Code, name="Postal_Code")
s5 = pd.Series(Approximate_Coordinates, name="Approximate_Coordinates")
s6 = pd.Series(Accuracy_Radius_km, name="Accuracy_Radius_km")
s7 = pd.Series(ISP, name="ISP")
s8 = pd.Series(Organization, name="Organization")
s9 = pd.Series(Domain, name="Domain", dtype=str)
s10 = pd.Series(Metro_Code, name="Metro_Code", dtype=str)

df = pd.concat([s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10], axis=1)  # Joining all series to get the ultimate
# desired dataframe

df.to_csv('IP_INFO.csv', index=False, encoding='utf-8')  # Converting the dataframe into csv for better data inference.
print("The file has been written as IP_INFO.csv")
