import pandas as pd
import numpy as np
import urllib.request
import requests
from bs4 import BeautifulSoup
import re


URL = "https://computersecurityclass.com/"

#Task 1.1
#creating the DataFrame from the .dat file
original_csv = pd.read_table("user_artists.dat", sep="\t", usecols=['userID', 'artistID', 'weight'])

original_csv.dropna()
original_csv.drop_duplicates()

#print(original_csv)
original_csv.to_csv("csv_user_artists.csv")



#Task 1.2
#creating function to scrape the data for a single user
def scraping(user):
    temp_url = URL + user
    #print(temp_url)
    temp_text = requests.get(temp_url).text
    soup = BeautifulSoup(temp_text, 'html.parser')
    #print(soup.prettify())

    return_arr = []

    for link in soup.find_all('li'):
        #print(link.get('href'))
        #print(link.get_text())
        temp_arr = []
        splitline = link.get_text().split('has been listened to')
        #print(splitline)

        artist_name = splitline[0][0:len(splitline[0]) - 1]
        #print(artist_name)
        temp_arr.append(artist_name)

        times_listened = int(re.sub(",","",splitline[1][1:len(splitline[1]) - 7]))
        #print(times_listened)
        temp_arr.append(times_listened)

        return_arr.append(temp_arr)

    return return_arr


#opening URL
page = requests.get(URL)
text = page.text

soup = BeautifulSoup(text, 'html.parser')
#print(soup.prettify())

#creating a list of href objects to check within the names
users = []
for link in soup.find_all('a'):
    #print(link.get('href'))
    users.append(link.get('href'))

#print(users)


csv_scraped =  pd.DataFrame(columns = ['user','artist','weight'])
for user in users:
    #print(user[0:len(user) - 5])
    #print(scraping(user))
    for scrapes in scraping(user):
        add = pd.DataFrame({
                    'user': [user[0:len(user) - 5]],
                    'artist' : [scrapes[0]],
                    'weight' : [scrapes[1]]})
        csv_scraped = pd.concat([csv_scraped, add], ignore_index = True, axis = 0)
    
#print(csv_scraped)
csv_scraped.to_csv("scraped.csv")



#creating dictionary for the original given data
#working with original_csv and csv_scraped

def 

    
    

