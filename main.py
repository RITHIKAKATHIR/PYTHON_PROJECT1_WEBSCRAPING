import time

from bs4 import BeautifulSoup
import requests
import time
from soupsieve.util import lower

print("Skills you are not familiar with: ")
unfamiliar_skills = input('>')
print(f"Filtering out {unfamiliar_skills}")


# requesting informing from the website with the help of 'requests'

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search. html?searchType=personalizedSearch&from'
# '=submit&txtKeywords=python&txtLocation=')

# print(html_text)


# if u run just line 5 and 7 the console prints response
# 200 meaning request is accepted, but we want the html code of page, so we modify this

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    # this pull the html code and print tht in the console

    soup = BeautifulSoup(html_text, 'html.parser')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # job has the first job card
    # print(job)  this statement prints the first card
    for index, job in enumerate(jobs):  # enumerates allows us to iterate over the index of jobs and job content
        job_published = job.find('span', class_='sim-posted').text
        # this extracts the name of the company
        if 'few' in job_published:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            # this extracts the name of the company
            # more_info = job.find('header', class_='clearfix').h2.a # this picks the title of the card as well
            # more_info = job.header.h2.a #again the same problem
            # to fix this call the href attribute
            more_info = job.header.h2.a['href']
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            #   if unfamiliar_skills not in skills: # remember this is case-sensitive.
            #   so the next line makes if cas insensitive
            if lower(unfamiliar_skills) not in lower(skills):  # remember this is case-sensitive
                with open(f'post/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Skills: {skills.strip()}")
                    f.write(f"more info: {more_info}")
                    f.write('')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        timewait = 10
        print(f"Waiting Time {timewait * 60} seconds...")
        time.sleep(60 * timewait)
