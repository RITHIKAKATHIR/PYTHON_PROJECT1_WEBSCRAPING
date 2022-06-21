from bs4 import BeautifulSoup
import requests

# requesting informing from the website with the help of 'requests'

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search. html?searchType=personalizedSearch&from'
# '=submit&txtKeywords=python&txtLocation=')

# print(html_text)


# if u run just line 5 and 7 the console prints response
# 200 meaning request is accepted, but we want the html code of page, so we modify this


html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)

# this pull the html code and print tht in the console

soup = BeautifulSoup(html_text, 'html.parser')

job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# job has the first job card
# print(job)  this statement prints the first card
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')  # this extracts the name of the company
skills = job.find('span', class_='srp-skills').text.replace(' ', '')
job_published = job.find('span', class_='sim-posted').text
# print(company_name)
# print(skills)
print(f'''
Company Name: {company_name}
Required Skill: {skills}
Date posted: {job_published}
 ''')
