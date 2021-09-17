 # a python program to scrap the website  https://itdashboard.gov/
import requests
from bs4 import BeautifulSoup
import pandas as pd
# the url of the Given site
weburl = "https://itdashboard.gov/"
r = requests.get(weburl)
htmlcontent = r.content
# parsing the html contents
soup = BeautifulSoup(htmlcontent, "html.parser")
# lists for data handling
depts = []
ls=[]
for link in soup.findAll('a'):
    depts.append(link.getText()+",")
for k in depts:
    ls.append(k.split(","))

# fetching specific contents using indexing in list
new_list = [ls[22:48]]
budget = ['2.7B','2.8B','36B','7.0B','1.5B','3.1B','819M','2.6B','5.4B','2.0B','1.0B','3.1B','385M','3.5B','765M','7.4B','447M','2.2B','125M','129M','9.1B','256M','275M','99.9M','136M','141M']
departments = []

for j in range(len(new_list[0])):
    departments.append(new_list[0][j][0])
# using padas to write to excel/csv
datFrame= pd.DataFrame({
    "Departments":[i for i in departments],
     "Budget":[j for j in budget]
})
datFrame.to_csv("agencies.csv",index=False)
print('export done.')
#

# working on downloading the contents from site: information Technology Agency Summary
weburl1 = "https://itdashboard.gov/drupal/summary/422"
r1 = requests.get(weburl1)
htmlcontent1 = r1.content
# parsing the html contents
soup1 = BeautifulSoup(htmlcontent1, "html.parser")


# downloading the files in
links = soup1.find_all('a')
i = 0
# finding links
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Download file number: ", i)

        # Get response object for link
        response = requests.get(link.get('href'))
        # Write content in pdf file
        pdf = open("pdf" + str(i) + ".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")

