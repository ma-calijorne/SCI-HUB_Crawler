#*-* coding: latin-1 *-*
import json



def ReadJSONInfo(sJSONFileIndex, Papers):

    class PapersInfo:
        authors= []
        title= ''
        venue= ''
        volume= ''
        number= ''
        pages= ''
        year= ''
        type= ''
        key= ''
        doi= ''
        ee= ''


    sJSONFilePath = 'Data/JSON{}.json'.format(sJSONFileIndex)
    sJSON_File = open(sJSONFilePath).read()

    JSONData = json.loads(sJSON_File)
    print "Arquivo Carregado..."
    for eachHit in JSONData['result']['hits']['hit']:
        objPaperInfo = PapersInfo()
        try:
            if ('author') in eachHit['info']['authors']:
                objPaperInfo.authors = eachHit['info']['authors']['author']
            else:
                objPaperInfo.authors = 'N/A'
            if ('title') in eachHit['info']:
                objPaperInfo.title   = eachHit['info']['title']
            else:
                objPaperInfo.title = 'N/A'
            if ('venue') in eachHit['info']:
                objPaperInfo.venue   = eachHit['info']['venue']
            else:
                objPaperInfo.venue = 'N/A'
            if ('volume') in eachHit['info']:
                objPaperInfo.volume  = eachHit['info']['volume']
            else:
                objPaperInfo.volume = 'N/A'
            if ('number') in eachHit['info']:
                objPaperInfo.number  = eachHit['info']['number']
            else:
                objPaperInfo.number = 'N/A'
            if ('pages') in eachHit['info']:
                objPaperInfo.pages   = eachHit['info']['pages']
            else:
                objPaperInfo.pages = 'N/A'
            if ('year') in eachHit['info']:
                objPaperInfo.year    = eachHit['info']['year']
            else:
                objPaperInfo.year = 'N/A'
            if ('type') in eachHit['info']:
                objPaperInfo.type    = eachHit['info']['type']
            else:
                objPaperInfo.type = 'N/A'
            if ('key') in eachHit['info']:
                objPaperInfo.key     = eachHit['info']['key']
            if ('doi') in eachHit['info']:
                objPaperInfo.doi     = eachHit['info']['doi']
            else:
                objPaperInfo.doi      = 'N/A'
            if ('ee') in eachHit['info']:
                objPaperInfo.ee      = eachHit['info']['ee']
            else:
                objPaperInfo.ee      = 'N/A'
            Papers.append(objPaperInfo)
        except:
            print 'Excpetion Raised'
            pass

    return Papers
