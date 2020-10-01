from datetime import date
from requests_html import HTMLSession

session= HTMLSession()

def getFormattedDateToday():
    return str(date.today()).replace("-","_")

def getUrl():
    r = session.get("https://hadshon.edu.gov.il/", verify = False)
    r.html.render()

    mediaElement = r.html.xpath('//*[@id="mep_0"]/div/div[1]')

    urlString = str(mediaElement[0].absolute_links)

    urlString = urlString.replace("{'","")
    urlString = urlString.replace("'}","")
    
    return urlString
    
def saveFile(url, filename):
    r = session.get(url, verify = False)

    path = "/Users/Harry/dev/news/hadshon/"+filename+".mp3"

    f = open(path, "wb")
    f.write(r.content)
    f.close()

if __name__ == "__main__":
    dateToday = getFormattedDateToday()

    url = getUrl()
    saveFile(url, dateToday)
    
