#encoding=utf-8
import sys
import urllib2
import ProxyPool as PXP
reload(sys)
sys.setdefaultencoding('utf-8')

def CreateDownloadList(Papers):
    iCount = 0

    for eachPaper in Papers:
        print('Trying to Download the Paper: {}'.format(eachPaper.doi))
        OpenPaperWebSite(eachPaper.doi,iCount)
        iCount = iCount + 1

    print 'Number of Papers with DOI: {}'.format(iCount)

def OpenPaperWebSite(sDOI,iCount):

    #TODO: Criar parametro para a URL do SCI-HUB
    sSciHub = 'https://sci-hub.tw/'
    sWebPage = sSciHub + sDOI
    print 'Página Inicial: {}'.format(sWebPage)
    bURLExtracted, sPDFPAge = PXP.extract_Main_URL(sWebPage)
    PXP.DownloadFile_ProxyPool(sPDFPAge,iCount,bURLExtracted)
   # time.sleep(10)

def download_file(download_url,iCount):
    response = urllib2.urlopen(download_url)
    file = open("Papers/Paper{}.pdf".format(iCount), 'w')
    file.write(response.read())
    file.close()
    print("Completed")


def extractCaptchaImage(sMainURL):
    # Extract Captcha Image
    bCaptchaPage = False
    try:
        if 'captcha' in sMainURL:
            bCaptchaPage = True
        # objBrowser.get(sMainURL)
        # sSourceCode = objBrowser.page_source
        # soup = BeautifulSoup(str(sSourceCode))
        # arTAGs = soup.findAll("img", attrs={'id': 'captcha'})
        # for eachTAG in arTAGs:
        #     sImageURL = eachTAG.attrs[1][1]
        # return sImageURL
    except:
        print ("Error Parsing HTML for Captcha")
    return bCaptchaPage