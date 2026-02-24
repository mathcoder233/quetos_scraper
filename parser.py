import requests
from bs4 import BeautifulSoup as bs


def scraper(session,url):
    responce=session.get(url,timeout=5)
    info=[]
    soup=bs(responce.text,"html.parser")
    shakarob=soup.select(".quote")
    for ins in shakarob:
        text=ins.select_one(".text").text
        author=ins.select_one(".author").text
        tag=ins.select(".tag")
        tags=[]
        for tag_in in tag:
            tags.append(tag_in.text)
        info.append(
            {
                "text":text,
                     "author":author,
                    "tags":tags
                     }
                    )
    return info


def pagination(session,url,start,end):
    all_data=[]
    for page in range(start,end+1):
        ur_l=f"{url}/page/{page}"
        data=scraper(session,ur_l)
        all_data.extend(data)
    return all_data
