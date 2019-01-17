from flask import Flask, render_template, request
import requests as rq
from bs4 import BeautifulSoup as bs


app=Flask(__name__,template_folder="views")

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/search")
def search():
    input_data=request.args.get("userName")
    url="http://www.op.gg/summoner/userName=?"
    res=rq.get(url+input_data)
    # 1. op.gg data 검색
    # 2. 승, 패 정보만 가져오기
    a=bs(res.text,"html.parser")
    win_num=a.select(".wins")[0].text[:-1]
    lose_num=a.select(".losses")[0].text[:-1]

    # print(request.args.get("userName"))
    # print(type(request.args))
    try:
        return render_template("search.html",data=input_data,wins=win_num,losses=lose_num)
    except:
        return "NO the id exist"
    
# request.full_path
# request.remote_addr
# request.url
# request.args
## request is very versatile object~! yes
