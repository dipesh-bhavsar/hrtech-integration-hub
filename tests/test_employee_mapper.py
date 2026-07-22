from src.connectors.hibob import HiBobEmployee
from src.transformers.employee_mapper import from_hibob,from_bamboohr
def test_from_hibob():
    emp=HiBobEmployee('h1','Jane','j@co.com','Eng','London','SWE','2022-01-01',True)
    u=from_hibob(emp);assert u.source=='hibob' and u.full_name=='Jane'
def test_from_bamboohr():
    emp={'id':42,'firstName':'John','lastName':'Smith','workEmail':'j@co.com','department':'HR','jobTitle':'Mgr','status':'Active'}
    u=from_bamboohr(emp);assert u.full_name=='John Smith' and u.source=='bamboohr'
