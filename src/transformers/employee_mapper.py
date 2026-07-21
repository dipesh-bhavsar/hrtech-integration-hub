from dataclasses import dataclass
from src.connectors.hibob import HiBobEmployee
@dataclass
class UnifiedEmployee:
    source:str;source_id:str;full_name:str;email:str;department:str;job_title:str;is_active:bool
def from_hibob(emp:HiBobEmployee)->UnifiedEmployee:
    return UnifiedEmployee('hibob',emp.id,emp.display_name,emp.email,emp.department,emp.job_title,emp.is_active)
def from_bamboohr(emp:dict)->UnifiedEmployee:
    return UnifiedEmployee('bamboohr',str(emp.get('id','')),f"{emp.get('firstName','')} {emp.get('lastName','')}".strip(),emp.get('workEmail',''),emp.get('department',''),emp.get('jobTitle',''),emp.get('status','Active')=='Active')
