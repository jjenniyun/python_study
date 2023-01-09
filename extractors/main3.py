from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
#from extractors.jobkorea import extract_jobkorea_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
# jobkorea = extract_jobkorea_jobs(keyword)
jobs = indeed+wwr
# jobs = indeed + wwr + jobkorea

# 파일로 저장
file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
file.write("Position, Company, Location, URL\n")

# jobkorea 추가 할 때 
#file = open(f"jobkorea.csv", "w",encoding="utf-8-sig")
#file.write("Position, Company, Location, URL\n")
# for job in results:
#   file.write(f"{job['link']},{job['company']},{job['location']},{job['position']}\n")
# file.close()

for job in jobs:
  # 딕셔너리 접근할 때는 ""에러남/ ''로 사용할 것!
  file.write(f"{job['link']}, {job['company']},{job['location']}, {job['position']}\n")

file.close()