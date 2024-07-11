from common import Credentials
from processes import Artera, CareFirst, Carelon, CareSource, CGS, Cohere, Epic, Everence, Evicore, HealthHelp, HumanaMilitary, IndianaMCD, Jiva, MDWISE, MHS, PHP, TurningPoint, UnifiedGroup
from processes.OSManager import OSManager
from secret_credentials import Secrets


class Runners:
    def __init__(self, directory=None):
        self.directory = directory
    
    
    def run_artera(self):
        artera_credentials = Credentials(url=Secrets.Artera.url, username=Secrets.Artera.username, password=Secrets.Artera.password)
        artera = Artera(credentials=artera_credentials)
        artera.login()

    def run_care_first(self):
        care_first_credentials = Credentials(url=Secrets.CareFirst.url, username=Secrets.CareFirst.username, password=Secrets.CareFirst.password)
        care_first = CareFirst(credentials=care_first_credentials)
        care_first.login()

    def run_carelon(self):
        carelon_credentials = Credentials(url=Secrets.Carelon.url, username=Secrets.Carelon.username, password=Secrets.Carelon.password)
        carelon = Carelon(credentials=carelon_credentials)
        carelon.login()

    def run_care_source(self):
        care_source_credentials = Credentials(url=Secrets.CareSource.url, username=Secrets.CareSource.username, password=Secrets.CareSource.password)
        care_source = CareSource(credentials=care_source_credentials)
        care_source.login()

    def run_cgs(self):
        cgs_credentials = Credentials(url=Secrets.CGS.url, username=Secrets.CGS.username, password=Secrets.CGS.password)
        cgs = CGS(credentials=cgs_credentials)
        cgs.login()

    def run_cohere(self):
        cohere_credentials = Credentials(url=Secrets.Cohere.url, username=Secrets.Cohere.username, password=Secrets.Cohere.password)
        cohere = Cohere(credentials=cohere_credentials)
        cohere.login()

    def run_epic(self):
        epic_credentials = Credentials(url=Secrets.Epic.url, username=Secrets.Epic.username, password=Secrets.Epic.password, customer_id=Secrets.Epic.customer_id)
        epic = Epic(credentials=epic_credentials)
        epic.login()

    def run_everence(self):
        everence_credentials = Credentials(url=Secrets.Everence.url, username=Secrets.Everence.username, password=Secrets.Everence.password)
        everence = Everence(credentials=everence_credentials)
        everence.login()

    def run_evicore(self):
        evicore_credentials = Credentials(url=Secrets.Evicore.url, username=Secrets.Evicore.username, password=Secrets.Evicore.password, customer_id=Secrets.Evicore.customer_id)
        evicore = Evicore(credentials=evicore_credentials)
        evicore.login()

    def run_health_help(self):
        health_help_credentials = Credentials(url=Secrets.HealthHelp.url, username=Secrets.HealthHelp.username, password=Secrets.HealthHelp.password, customer_id=Secrets.HealthHelp.customer_id)
        health_help = HealthHelp(credentials=health_help_credentials)
        health_help.login()

    def run_humana_military(self):
        humana_military_credentials = Credentials(url=Secrets.HumanaMilitary.url, username=Secrets.HumanaMilitary.username, password=Secrets.HumanaMilitary.password, customer_id=Secrets.HumanaMilitary.customer_id)
        humana_military = HumanaMilitary(credentials=humana_military_credentials)
        humana_military.login()

    def run_indiana_mcd(self):
        indiana_mcd_credentials = Credentials(url=Secrets.IndianaMCD.url, username=Secrets.IndianaMCD.username, password=Secrets.IndianaMCD.password, customer_id=Secrets.IndianaMCD.customer_id, city_born=Secrets.IndianaMCD.city_born)
        indiana_mcd = IndianaMCD(credentials=indiana_mcd_credentials)
        indiana_mcd.login()

    def run_jiva(self):
        jiva_credentials = Credentials(url=Secrets.Jiva.url, username=Secrets.Jiva.username, password=Secrets.Jiva.password)
        jiva = Jiva(credentials=jiva_credentials)
        jiva.login()

    def run_mdwise(self):
        mdwise_credentials = Credentials(url=Secrets.MDWISE.url, username=Secrets.MDWISE.username, password=Secrets.MDWISE.password)
        mdwise = MDWISE(credentials=mdwise_credentials)
        mdwise.login()
    
    def run_mhs(self):
        mhs_credentials = Credentials(url=Secrets.MHS.url, username=Secrets.MHS.username, password=Secrets.MHS.password, email=Secrets.MHS.email)
        mhs = MHS(credentials=mhs_credentials)
        mhs.login()

    def run_php(self):
        php_credentials = Credentials(url=Secrets.PHP.url, username=Secrets.PHP.username, password=Secrets.PHP.password, email=Secrets.PHP.email)
        php = PHP(credentials=php_credentials)
        php.login()

    def run_turning_point(self):
        turning_point_credentials = Credentials(url=Secrets.TurningPoint.url, username=Secrets.TurningPoint.username, password=Secrets.TurningPoint.password, email=Secrets.TurningPoint.email)
        turning_point = TurningPoint(credentials=turning_point_credentials)
        turning_point.login()
    
    def run_unified_group(self):
        unified_group_credentials = Credentials(url=Secrets.UnifiedGroup.url, username=Secrets.UnifiedGroup.username, password=Secrets.UnifiedGroup.password)
        unified_group = UnifiedGroup(credentials=unified_group_credentials)
        unified_group.login()

    def run_OS_manager(self, directory):
        os_manager = OSManager(directory)
        # file_contents = os_manager.read_files()
        # print(file_contents)

        # last_element = os_manager.get_most_recent_element()
        # print(last_element)

        # renamed_file = os_manager.rename('main.css', '123456')
        # print(renamed_file)
        
        # os_manager.delete_file('ad.png')

        # os_manager.add_file('luke\'s_file.txt', 'This is my newly created file')
        # os_manager.rename('luke\'s_file.txt', 'luke\'s_new_file')
        
        # os_manager.add_text_to_file('luke\'s_new_file.txt', '\nAdding to this file')

        # os_manager.remove_text_from_file('luke\'s_new_file.txt', 'this')
        
        # line_number = os_manager.find_line_number('luke\'s_new_file.txt', 'file')
        # print(line_number)

        os_manager.find_text_in_file('luke\'s_new_file.txt', 'Adding')
