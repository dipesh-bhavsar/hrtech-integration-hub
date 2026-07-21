from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
app=FastAPI(title='HRTech Integration Hub',version='0.1.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/webhooks/hibob')
async def hibob_webhook(request:Request):
    payload=await request.json()
    return JSONResponse({'received':True,'event':payload.get('eventType','unknown')})
@app.post('/sync/employees')
def trigger_sync(): return {'message':'Sync triggered. Implement sync_employees() here.'}
