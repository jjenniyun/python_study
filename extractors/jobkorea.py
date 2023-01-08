# jobkorea webscrapper
from requests import get
from bs4 import BeautifulSoup

def extract_jobkorea_jobs(keyword):
  results = []
  url = "https://www.jobkorea.co.kr/Search/?stext="
  search_term = "python"
  final_url = f"{url}{search_term}"
  response = get(final_url)
  if response.status_code != 200:
    print("Cannot Request Page")
  else:
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.select('ul.clear li.list-post', class_ = "clear")
  
  for i in range(20):
    post = posts[i]
  
    company = post.select_one('div.post-list-corp a')
    link = company['href']
    job_info = post.find('div', class_='post-list-info')
    title = job_info.find('a', class_='title')
    region = job_info.find('span', class_='loc long')
    if region == None:
      job_data={
      'company': company.string.replace(",", " "),
      'link' : f'https://www.jobkorea.co.kr{link}',
      'location' : 'None',
      'position' : title['title'].replace(",", " ")
      }
    else:
      job_data={
      'company': company.string.replace(",", " "),
      'link' : f'https://www.jobkorea.co.kr{link}',
      'location' : region.string.replace(",", " "),
      'position' : title['title'].replace(",", " ")
      }
    results.append(job_data)
return results