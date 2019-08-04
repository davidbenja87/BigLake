
## Required for Azure Data Lake Storage Gen1 filesystem management
from azure.datalake.store import core, lib, multithread
import pandas as pd
import config
import csv
# Common Azure imports
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

class AzureDataConnector:
    def __init__(self,adlsAccountName: str):
        self._subscriptionId = config.azure['subscriptionId']
        self._adlsAccountName = adlsAccountName
        self._tenant = config.azure['tenant']  # service prinicpal tenant ID
        self.RESOURCE = 'https://datalake.azure.net/'   # data lake store account
        self._client_id = config.azure['client_id'] # client ID
        self._client_secret = config.azure['client_secret'] # client secret key

    def _establish_azure_conn(self):
        adlCreds = lib.auth(tenant_id = self._tenant,
                client_secret = self._client_secret,
                client_id = self._client_id,
                resource = self.RESOURCE)
        return adlCreds        

    def _create_filesytem_conn(self):
        ## Create a filesystem client object
        adlCreds = self._establish_azure_conn()
        adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=self._adlsAccountName)
        return adlsFileSystemClient
    
    def downloadfile_ToADS(self,inpath: str,outpath: str):
        # ## Download a file
        adlsFileSystemClient = self._create_filesytem_conn()
        multithread.ADLDownloader(adlsFileSystemClient,
                          lpath=inpath,
                          rpath=outpath,
                          nthreads=64,
                          overwrite=True,
                          buffersize=4194304,
                          blocksize=4194304)

    def uploadfile_FromADS(self,inpath: str,outpath: str):
        adlsFileSystemClient = self._create_filesytem_conn()
        multithread.ADLUploader(adlsFileSystemClient,
                        lpath=inpath,
                        rpath=outpath,
                        nthreads=64,
                        overwrite=True,
                        buffersize=4194304,
                        blocksize=4194304)
                      
    def readfile_ADS(self,path: str):
        adlsFileSystemClient = self._create_filesytem_conn()
        with adlsFileSystemClient.open(path,'rb') as f:
            input_file = pd.read_csv(f, dtype='unicode')
        return input_file    


    def listfile_ADS(self,path: str):
        adlsFileSystemClient = self._create_filesytem_conn()
        lsfile = adlsFileSystemClient.listdir(path) 
        return lsfile   
