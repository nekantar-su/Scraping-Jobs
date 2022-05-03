import time
import requests
from bs4 import BeautifulSoup

print('Enter skills you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=new+york').text

    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_= 'joblist-comp-name').text.replace(' ','')
            skill = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skill.strip()} \n')
                    f.write(f'More info: {more_info}')
                print(f'File saved: {index}.txt')



if __name__ =='__main__':
    while True:
        find_jobs()
        time.sleep(600)
