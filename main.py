from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

# 플라스크 시작
app = Flask("JobScrapper")

# 홈페이지 응답
@app.route("/")  # decorator
def home():
  return render_template("home.html", name="jisu")

db = {} # 가짜 데이터베이스, 서버가 커져있을 때만 유지

@app.route("/search")
def hello():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr # list
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv",as_attachment=True) # 파일 다운로드 허용

app.run("0.0.0.0")  # 웹 서버 실행
