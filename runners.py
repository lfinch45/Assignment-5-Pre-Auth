from common import Credentials
from processes import Zelis
from secret_credentials import Secrets


class Runners:
    def __init__(self):
        pass


    def run_zelis(self):
        zelis_credentials = Credentials(url=Secrets.Zelis.url, username=Secrets.Zelis.username, password=Secrets.Zelis.password)
        zelis = Zelis(credentials=zelis_credentials)
        zelis.login()
    
    # Use Zelis as a template to run the rest of the websites
    