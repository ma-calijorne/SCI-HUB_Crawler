#*-* coding: latin-1 *-*
import DBLP_JSONPapers_Parser as JPP
import CreateDownloadList as CDL

#Controle do Laço para leitura de Arquivos.
#TODO: Criar arquivo JSON de Configuração
iIndex = 0
#Vetor de Objetos com as informações dos Papers.
Papers = []

for iIndex in range(3):
    Papers = JPP.ReadJSONInfo(str(iIndex + 1),Papers)

CDL.CreateDownloadList(Papers)