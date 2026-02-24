from session import*
from parser import*
from excel_saver import save_to_excel
url="https://quotes.toscrape.com"
print(f"scraping in {url}... ") 
start=int(input("please write your start page number(without string or probel):"))
print("well done...")
end=int(input("please write last page which you wanna do scrape(without string or probel:"))

session=create_session()
data=create_data(session,url)

logi=login(session,url,data)

if not logi:
    print("login error")
else:
    all_data=pagination(session,url,start,end)

    for q in all_data:
        q["tags"]=",".join(q["tags"])

    save_to_excel(all_data, f"data_from_{start}_until_{end}.xlsx")
