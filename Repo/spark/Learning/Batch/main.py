import azureLakeConnector as alc

def main():
    adlsAccountName = 'biglakepoctest'
    alcAccess = alc.AzureDataConnector(adlsAccountName)
    lpath="C:\\Users\\Ben\\Documents\\spark-Data\\mental-health-in-tech-survey\\survey.csv"
    outpath='/LandingZone/survey.csv'
    alcAccess.uploadfile_FromADS(lpath,outpath)



if __name__ == '__main__':
    main()