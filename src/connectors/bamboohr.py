import os,base64
from src.base_client import BaseClient
class BambooHRConnector(BaseClient):
    def __init__(self,api_key=None,subdomain=None):
        key=api_key or os.getenv('BAMBOOHR_API_KEY','');sub=subdomain or os.getenv('BAMBOOHR_SUBDOMAIN','')
        token=base64.b64encode(f'{key}:x'.encode()).decode()
        super().__init__(f'https://api.bamboohr.com/api/gateway.php/{sub}',headers={'Authorization':f'Basic {token}','Accept':'application/json'})
    def list_employees(self): return self.get('/v1/employees/directory').get('employees',[])
    def list_time_off(self,start,end): return self.get(f'/v1/time_off/requests?start={start}&end={end}') or []
