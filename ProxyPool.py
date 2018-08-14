from lxml.html import fromstring
import requests
import sys
from itertools import cycle
from BeautifulSoup import BeautifulSoup
import CreateDownloadList
import time
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def DownloadFile_ProxyPool(url,iCount,bURLExtracted):
    #If you are copy pasting proxy ips, put in the list below
    #proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']

    if bURLExtracted:
        proxies = get_proxies()
        proxy_pool = cycle(proxies)

        for i in range(1,11):
            #Get a proxy from the pool
            proxy = next(proxy_pool)
            print('Pagina do PDF: {}'.format(url))
            try:
                response = requests.get(url,proxies={"http": proxy, "https": proxy}, stream=True)
                bCaptchaPage = CreateDownloadList.extractCaptchaImage(response.content)
                if not bCaptchaPage:
                    print 'Codigo Retorno: {}'.format(response.status_code)
                    if response.status_code == 200:
                        handle = open("Papers/Paper{}.pdf".format(iCount), "wb")
                        handle.write(response.content)
                        # for chunk in response.iter_content(chunk_size=512):
                        #     if chunk:  # filter out keep-alive new chunks
                        #         handle.write(chunk)
                    else:
                        print("Couldn't Download the Paper: {}".format(url))
                    break
                else:
                    print("Pagina com Captcha. Tentar outro Proxy.")
            except:
                #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
                #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
                print("Skipping. Connection error")
    else:
        print 'URL {} error'.format(url)

def extract_Main_URL(sPageSource):

    # If you are copy pasting proxy ips, put in the list below
    # proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    sSourceCode = ''
    bURLExtracted = True

    for i in range(1, 11):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        #print("Request #%d" % i)
        try:
            response = requests.get(sPageSource, proxies={"http": proxy, "https": proxy})
            sSourceCode = response.content
            bURLExtracted = True
            break
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            bURLExtracted = False
            print("Skipping. Connnection error")


    #Extract Main Pages of the Paper
    if sSourceCode <> '':
        soup = BeautifulSoup(str(sSourceCode))
        arTAGs = soup.findAll("div", attrs={'id': 'main_content'})
        sMainURL = arTAGs[0].contents[1].attrs[0][1]
        sMainURL = sMainURL[:sMainURL.index('.pdf') + 4]
    return bURLExtracted, sMainURL

def ProgressBar():

    toolbar_width = 60

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(1)  # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n")

