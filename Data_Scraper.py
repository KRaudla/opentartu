
import requests
from bs4 import BeautifulSoup
import re
import csv

#tase 1
def otsus_parser(url):
    r = requests.get(url,headers=headers)
    resp = r.content
    soup2 = BeautifulSoup(resp, "html.parser")

    a = soup2.find(text="Akti väljaandja:").findNext("td").findNext("td").find(text=True).strip()
    b = soup2.find(text="Akti liik:").findNext("td").findNext("td").find(text=True).strip()
    c = soup2.find(text="Teema:").findNext("td").findNext("td").find(text=True).strip()
    d= soup2.find(text="Reg. number:").findNext("td").findNext("td").find(text=True).strip()
    e= soup2.find(text="Seisund:").findNext("td").findNext("td").find(text=True).strip()
    f= soup2.find(text="Vastuvõtmise kp:").findNext("td").findNext("td").find(text=True).strip()
    g= soup2.find(text="Akti kehtivus:").findNext("td").findNext("td").find(text=True).strip()
    h = soup2.find(text="Eelnõu:").findNext("td").findNext("td").find("br").text.strip()
    #Sisu parsimine on hetkel puudu
    #try:
    #    print (soup2.find("ul").findNext("table").findnext("tbody").findAll("li").findAll(text=True))
    #except:
    try:
        url_algus= "http://info.raad.tartu.ee/webaktid.nsf/web/gpunid"
        j = url_algus+soup2.find(text="Eelnõu:").findNext("a").get("href").split("gpunid")[1].strip()
    except:
        j = ""
    row = (a,b,c,d,e,f,g,h,j)
    return row

#tase 2
def eelnou_parser(url):
    r = requests.get(url,headers=headers)
    resp = r.content
    soup2 = BeautifulSoup(resp, "html.parser")
    a2 = soup2.find(text="Staatus").findNext("td").findNext("td").find(text=True).strip()
    b2 = soup2.find(text="Akti väljaandja:").findNext("td").findNext("td").find(text=True).strip()
    c2 = soup2.find(text="Akti liik:").findNext("td").findNext("td").find(text=True).strip()
    d2= soup2.find(text="Pealkiri:").findNext("td").findNext("td").find("br").text.strip()
    e2= soup2.find(text="Reg. number:").findNext("td").findNext("td").find(text=True).strip()
    try:
        f2= soup2.find(text="Koostaja:").findNext("td").findNext("td").find(text=True).strip()
    except:
        f2=""
    g2= soup2.find(text="Koostamise kp:").findNext("td").findNext("td").find(text=True).strip()
    try:
        h2 = soup2.find(text="Ettekandja:").findNext("td").findNext("td").find(text=True).strip()
    except:
        h2=""
    i2= soup2.find(text="Esitab:").findNext("td").findNext("td").find(text=True).strip()
    try:
        j2= soup2.find(text="Juhtiv komisjon:").findNext("td").findNext("td").find(text=True).strip()
    except:
        j2=""
    try:
        k2 = []
        for i in soup2.find(text="Seosed:").findNext("td").findNext("td").findAll("a"):
            url_algus= "http://info.raad.tartu.ee/webaktid.nsf/web/gpunid"
            k2.append(url_algus+i.get("href").split("gpunid")[1].strip())

    except:
        k2=[]
    row2= (a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2)
    return row2

with open("output2.csv","w", encoding="utf-8") as output_file:
    writer = csv.writer(output_file, delimiter="\t",quoting=csv.QUOTE_ALL)
    fieldnames = ['Url','Väljaandja','Liik','Teema','Reg_nr', 'Seisund','Vastuvotmise_kp','Akti_kehtivus','Pealkiri','Alam_url'\
                  ,'Staatus','Akti_valjaandja','Akti_Liik','Pealkiri','Reg_nr','Koostaja','Koostamise_kp','Ettekandja','Esitaja','Juhtiv_komisjon','Seose_urlid']
    writer.writerow(fieldnames)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    #Starting url
    r = requests.get("http://www.tartu.ee/?page_id=1256&lang_id=1&menu_id=2&lotus_url=/webaktid.nsf/WebOtsused?OpenView&Start=1&Count=400&RestrictToCategory=Tartu_Linnavolikogu_8._koosseis_(alates_20.10.13)",headers=headers)
    resp = r.content
    soup = BeautifulSoup(resp, "html.parser")
    for i in soup.findAll("li"):
        otsuse_url=i.find("a").get("href")
        otsus_data = otsus_parser(otsuse_url)
        #tase 1 data koos
        row = (otsuse_url,)+otsus_data
        tase2url=row[-1]
        #tase 2 data koos
        row2 = eelnou_parser(tase2url)
        #tase 1 ja 2 data koos
        row3 = row+row2
        #print (row3)




        writer.writerow([str(item).strip() for item in row3])