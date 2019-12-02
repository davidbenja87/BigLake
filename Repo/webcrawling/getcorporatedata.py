import requests
import os
import time



def main():
    headers = {
            "username":"reedbusinessinfo",
            "password":"SUI914",
            "Connection": "keep-alive",
     
           }
           
    downloadheaders = {
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "f": "/www/corporate.tpsonline.org.uk//data/tps.txt"
        }  
    file_name="tps.txt"
    session = requests.Session()

#the website sets the cookies first
#Request again to download

    def create_data_export(headers: str,downloadheaders: str):
        session.post("https://corporate.tpsonline.org.uk/index.php/tps/download", data = headers,verify=False)
        download_data = session.post("https://corporate.tpsonline.org.uk/index.php/tps/get_file", data = downloadheaders, verify=False)
        return download_data

    def setup_download_directory():  
        base_path= os.path.dirname(os.path.realpath(__file__))
        download_tmp_path = os.path.join(base_path,'tmp')     
        if not os.path.exists(download_tmp_path):
            os.mkdir(download_tmp_path)  
        fully_qualified_name = os.path.join(download_tmp_path, file_name)
        return fully_qualified_name


    def download_file():
        download_data = create_data_export(headers , downloadheaders)
        fully_qualified_name = setup_download_directory()
        try:
            no_count = 0
            while no_count < 5:
                no_count += 1
                if len(download_data.content)>100:
                    break
                time.sleep(90)    
            with open(fully_qualified_name, "wb") as saveMidi:
                saveMidi.write(download_data.content)
        finally:
            print('TPS successfully loaded')

    download_file() 

                 

if __name__ == "__main__": 
    main() 
            




    







