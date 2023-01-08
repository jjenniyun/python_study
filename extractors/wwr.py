from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  url = "https://weworkremotely.com/remote-jobs/search?term="
  response = get(f"{url}{keyword}")
  if response.status_code != 200:
    print("Cant request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)  #view_all 제거
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']  # 딕셔너리
        # 리스트에 넣어서 list 순서대로 값을 저장(시간 절약)
        company, kind, region = anchor.find_all(
          'span', class_="company")  # 회사이름, 직무, 일하는 지역
        title = anchor.find('span', class_='title')  # 하나의 항목 찾기
        job_data = {
          'link': f"https://weworkremotely.com/{link}",
          'company': company.string.replace(","," "),
          'location': region.string.replace(","," "),
          'position': title.string.replace(","," ")
        }
        results.append(job_data)
    return results