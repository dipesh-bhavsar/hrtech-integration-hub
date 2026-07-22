from unittest.mock import patch
from src.connectors.hibob import HiBobConnector
SAMPLE={'employees':[{'id':'e1','displayName':'Alice','email':'a@co.com','work':{'department':'Eng','site':'London','title':'SWE','startDate':'2022-01-10','active':True}}]}
def test_maps_fields():
    c=HiBobConnector(api_key='test')
    with patch.object(c,'get',return_value=SAMPLE): emps=c.list_employees()
    assert len(emps)==1 and emps[0].display_name=='Alice'
def test_filters_inactive():
    resp={'employees':[{'id':'e2','displayName':'Bob','email':'b@co.com','work':{'department':'HR','site':'NY','title':'Mgr','startDate':'2020-01-01','active':False}}]}
    c=HiBobConnector(api_key='test')
    with patch.object(c,'get',return_value=resp): assert c.list_employees(active_only=True)==[]
