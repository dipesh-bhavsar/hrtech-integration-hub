import os
from dataclasses import dataclass
from src.base_client import BaseClient
@dataclass
class HiBobEmployee:
    id:str;display_name:str;email:str;department:str;site:str;job_title:str;start_date:str;is_active:bool
class HiBobConnector(BaseClient):
    def __init__(self,api_key=None):
        key=api_key or os.getenv('HIBOB_API_KEY','')
        super().__init__('https://api.hibob.com/v1',headers={'Authorization':f'Basic {key}','Content-Type':'application/json'})
    def list_employees(self,active_only=True):
        result=[]
        for emp in self.get('/people').get('employees',[]):
            work=emp.get('work',{});active=work.get('active',True)
            if active_only and not active: continue
            result.append(HiBobEmployee(id=emp.get('id',''),display_name=emp.get('displayName',''),email=emp.get('email',''),department=work.get('department',''),site=work.get('site',''),job_title=work.get('title',''),start_date=work.get('startDate',''),is_active=active))
        return result
