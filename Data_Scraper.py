import requests
from bs4 import BeautifulSoup
import re
import csv
import time
#Otsuse Data, level 1
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
    row = ("Otsus",a,b,c,d,e,f,g,h,j)
    return row

#Suur eelnõu DATA, level2
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
    row2= ("Suur eelnõu",a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2)
    return row2

def seosed_eelnouParser(soup):
    a2 = soup.find(text="Staatus").findNext("td").findNext("td").find(text=True).strip()
    b2 = soup.find(text="Akti väljaandja:").findNext("td").findNext("td").find(text=True).strip()
    c2 = soup.find(text="Akti liik:").findNext("td").findNext("td").find(text=True).strip()
    d2= soup.find(text="Pealkiri:").findNext("td").findNext("td").find("br").text.strip()
    e2= soup.find(text="Reg. number:").findNext("td").findNext("td").find(text=True).strip()
    try:
        f2 = soup.find(text="Koostaja:").findNext("td").findNext("td").find(text=True).strip()
    except:
        f2=""
    try:
        g2 = soup.find(text="Koostamise kp:").findNext("td").findNext("td").find(text=True).strip()
    except:
        g2=""
    try:
        h2 = soup.find(text="Ettekandja:").findNext("td").findNext("td").find(text=True).strip()
    except:
        h2=""
    row = ("Väike eelnõu",a2,b2,c2,d2,e2,f2,g2,h2)
    return row

def seosed_koosolekuProtokollParser(soup):
    a2 = soup.findAll('tr')[0:1][0].findAll("td")[3:4][0].text.strip()
    b2 = soup.findAll('tr')[1:2][0].findAll("td")[3:4][0].text.strip()
    c2 = soup.findAll('tr')[2:3][0].findAll("td")[3:4][0].text.strip()
    d2 = soup.findAll('tr')[3:4][0].findAll("td")[3:4][0].text.strip()
    e2 = soup.findAll('tr')[4:5][0].findAll("td")[3:4][0].text.strip()
    f2 = soup.findAll('tr')[5:6][0].findAll("td")[3:4][0].text.strip()
    g2 = soup.findAll('tr')[6:7][0].findAll("td")[3:4][0].text.strip()
    h2 = soup.findAll('tr')[7:8][0].findAll("td")[3:4][0].text.strip()
    i2 = soup.findAll('tr')[8:9][0].findAll("td")[3:4][0].text.strip()
    j2 = soup.findAll('tr')[9:10][0].findAll("td")[3:4][0].text.strip()
    k2 = soup.findAll('tr')[10:11][0].findAll("td")[3:4][0].text.strip()
    l2 = soup.findAll('tr')[11:12][0].findAll("td")[3:4][0].text.strip()
    m2 = soup.findAll('tr')[12:13][0].findAll("td")[3:4][0].text.strip()
    n2 = soup.findAll('tr')[13:14][0].findAll("td")[3:4][0].text.strip()
    row = ("Koosoleku protokoll",a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2,n2)
    return row

def seosed_istungiProtokollParser(soup):
    a2 = soup.findAll('tr')[0:1][0].findAll("td")[3:4][0].text.strip()
    b2 = soup.findAll('tr')[1:2][0].findAll("td")[3:4][0].text.strip()
    c2 = soup.findAll('tr')[2:3][0].findAll("td")[3:4][0].text.strip()
    d2 = soup.findAll('tr')[3:4][0].findAll("td")[3:4][0].text.strip()
    e2 = soup.findAll('tr')[4:5][0].findAll("td")[3:4][0].text.strip()
    f2 = soup.findAll('tr')[5:6][0].findAll("td")[3:4][0].text.strip()
    g2 = soup.findAll('tr')[6:7][0].findAll("td")[3:4][0].text.strip()
    h2 = soup.findAll('tr')[7:8][0].findAll("td")[3:4][0].text.strip()
    i2 = soup.findAll('tr')[8:9][0].findAll("td")[3:4][0].text.strip()
    j2 = soup.findAll('tr')[9:10][0].findAll("td")[3:4][0].text.strip()
    k2 = soup.findAll('tr')[10:11][0].findAll("td")[3:4][0].text.strip()
    l2 = soup.findAll('tr')[11:12][0].findAll("td")[3:4][0].text.strip()
    row = ("Istungi protokoll",a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2)
    return row
commonID=0
with open("otsus.csv","w", encoding="utf-8") as otsused_output,\
     open("suur_eelnou.csv","w",encoding="utf-8") as suurEelnou_output,\
     open("vaike_eelnou.csv","w", encoding="utf-8") as vaikeEelnou_output,\
     open("koosolekuProtokollid.csv","w", encoding="utf-8") as koosolekuProtokollid_output,\
     open("istungiProtokollid.csv","w", encoding="utf-8") as istungiProtokollid_output:

    otsusWriter = csv.writer(otsused_output, delimiter="\t",quoting=csv.QUOTE_ALL)
    suurEelnouWriter = csv.writer(suurEelnou_output, delimiter="\t",quoting=csv.QUOTE_ALL)
    vaikeEelnouWriter = csv.writer(vaikeEelnou_output, delimiter="\t",quoting=csv.QUOTE_ALL)
    olekuProtokollidWriter = csv.writer(koosolekuProtokollid_output, delimiter="\t",quoting=csv.QUOTE_ALL)
    istungiProtokollidWriter = csv.writer(istungiProtokollid_output, delimiter="\t",quoting=csv.QUOTE_ALL)

    fieldsOtsus = ['Url','Id_custom','Tyyp_custom','Akti_valjaandja','Akti_liik',\
                   'Teema','Reg_nr', 'Seisund','Vastuvotmise_kp','Akti_kehtivus',\
                   'Eelnou_pealkiri','Url_SuurEelnou']
    fieldsSuurEelnou = ['Url','Id_custom','Tyyp_custom','Staatus','Akti_valjaandja',\
                        'Akti_liik','Pealkiri','Reg_nr','Koostaja','Koostamise_kp',\
                        'Ettekandja','Esitab','Juhtiv_komisjon','Seosed_urls']
    fieldsVaikeEelnou= ['Url_suurEelnou','Url_vaikeEelnou','Id_custom','Tyyp_custom',\
                        'Staatus','Akti_valjaandja','Akti_liik', 'Pealkiri',\
                       'Reg_nr','Koostaja','Koostamise_kp','Ettekandja']
    fieldsOlekuProtokoll = ['Url_suurEelnou','Url_koosolekuProtokoll','Id_custom','Tyyp_custom',\
                            'Asutuse_nimetus', 'Organi_nimetus','Reg_nr','Sarja_indeks',\
                            'Teema', 'Kuupaev','Kellaaeg','Toimumise_koht','Juhataja',\
                            'Protokollija', 'Koosolekul_osalesid','Puudusid',\
                            'Kutsutud','Seisund']
    fieldsIstungiProtokoll = ['Url_suurEelnou','Url_istungiProtokoll','Id_custom','Tyyp_custom',\
                              'Istungi_pidaja','Istungi_kp','Protokolli_nr','Toimumise_koht',\
                              'Istungi_kellaaeg','Istungit_juhatas','Protokollija',\
                              'Istungist_votsid_osa','Puudusid','Kutsutud',\
                              'Kylalised','Seisund']


    otsusWriter.writerow(fieldsOtsus)
    suurEelnouWriter.writerow(fieldsSuurEelnou)
    vaikeEelnouWriter.writerow(fieldsVaikeEelnou)
    olekuProtokollidWriter.writerow(fieldsOlekuProtokoll)
    istungiProtokollidWriter.writerow(fieldsIstungiProtokoll)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    #Starting url
    r = requests.get("http://www.tartu.ee/?page_id=1256&lang_id=1&menu_id=2&lotus_url=/webaktid.nsf/WebOtsused?OpenView&Start=1&Count=400&RestrictToCategory=Tartu_Linnavolikogu_8._koosseis_(alates_20.10.13)",headers=headers)
    resp = r.content
    soup = BeautifulSoup(resp, "html.parser")
    for i in soup.findAll("li"):
        time.sleep(1)
        otsuse_url=i.find("a").get("href")
        print(otsuse_url)
        otsus_data = otsus_parser(otsuse_url)
        #Otsused_data koos
        row = (otsuse_url,str(commonID),)+otsus_data
        otsusWriter.writerow([str(item).strip() for item in row])
        tase2url=row[-1]
        #SuurEelnõu data koos
        eelnoudata=eelnou_parser(tase2url)

        #Kas suurel eelnõul on väike eelnõu või protokolli? kontroll
        # on kolmanda taseme listide kogum, esitatud listina. Just In case
        row2 = ((tase2url,)+(str(commonID),)+eelnoudata)#,+tase2url)# on kolmanda taseme listide kogum, esitatud listina. Just In case
        suurEelnouWriter.writerow([str(item).strip() for item in row2])

        if len((row2[-1]))>0:
            #row2[0] #väikeeelnõu url, teised on protokolli urlid
            for urlSeos in row2[-1]:
                #time.sleep(0.5)
                #kontrolli, millega on tegu ja millist parsetreed rakendada (väike eelnõu, protokoll või midagi muud)
                r = requests.get(urlSeos,headers=headers)
                seoseResp= r.content
                seoseSoup = BeautifulSoup(seoseResp, "html.parser")
                #Otsusta, kuhu saadan supi parsimiseks
                if "õigusakti eelnõu" in seoseSoup.find("b").text.lower().strip():
                    vaikeEelnouRow=(tase2url,urlSeos,str(commonID),)+seosed_eelnouParser(seoseSoup)
                    vaikeEelnouWriter.writerow([str(item).strip() for item in vaikeEelnouRow])

                elif "koosoleku protokoll" in seoseSoup.find("b").text.lower().strip():
                    olekuProtokollRow=(tase2url,urlSeos,str(commonID),)+seosed_koosolekuProtokollParser(seoseSoup)
                    olekuProtokollidWriter.writerow([str(item).strip() for item in olekuProtokollRow])

                elif "istungi protokoll" in seoseSoup.find("b").text.lower().strip():
                    istungiProtokollRow=(tase2url,urlSeos,str(commonID),)+seosed_istungiProtokollParser(seoseSoup)
                    istungiProtokollidWriter.writerow([str(item).strip() for item in istungiProtokollRow])
                else:
                    print (urlSeos,seoseSoup.find("b").text.lower().strip())
                    #continue
            commonID=commonID+1
        else:
            continue