#*-* coding: latin-1 *-*
import DBLP_JSONPapers_Parser as JPP
import CreateDownloadList as CDL

#Controle do La�o para leitura de Arquivos.
#TODO: Criar arquivo JSON de Configura��o
iIndex = 0
#Vetor de Objetos com as informa��es dos Papers.
Papers = []

for iIndex in range(3):
    Papers = JPP.ReadJSONInfo(str(iIndex + 1),Papers)

CDL.CreateDownloadList(Papers)