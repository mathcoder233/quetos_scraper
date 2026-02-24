import requests
from bs4 import BeautifulSoup

def create_session():
    session=requests.Session()
    session.headers.update({"User-Agent":"mozilla.firefox/5.0"})
    return session




def login(session,url,data):
    responce=session.post(f"{url}/login",timeout=5,data=data)
    if responce.status_code==200 and "Logout" in responce.text:
        return True
    return False

def create_data(session,url):
    res=session.get(f"{url}/login",timeout=5)
    soup=BeautifulSoup(res.text,"html.parser")
    token=soup.select_one("form input")["value"]
    data={
        "username":"abduazim",
        "password":"123odbn",
        "csrf_token":token
        }
    return data
    
