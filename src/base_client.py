import logging,httpx
from tenacity import retry,stop_after_attempt,wait_exponential,retry_if_exception_type
logger=logging.getLogger(__name__)
class BaseClient:
    def __init__(self,base_url,headers=None,timeout=10.0):
        self.base_url=base_url.rstrip('/');self.timeout=timeout;self._headers=headers or {}
    @retry(stop=stop_after_attempt(3),wait=wait_exponential(min=2,max=10),retry=retry_if_exception_type(httpx.HTTPStatusError),reraise=True)
    def get(self,path,params=None):
        with httpx.Client(timeout=self.timeout) as c:
            r=c.get(f'{self.base_url}/{path.lstrip("/")}',headers=self._headers,params=params)
            r.raise_for_status();return r.json()
    def post(self,path,payload):
        with httpx.Client(timeout=self.timeout) as c:
            r=c.post(f'{self.base_url}/{path.lstrip("/")}',headers=self._headers,json=payload)
            r.raise_for_status();return r.json()
