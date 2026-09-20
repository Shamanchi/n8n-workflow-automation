from fastapi import APIRouter

router = APIRouter()

@router.get('/workflows')
async def list_workflows():
    return {'workflows': []}

@router.post('/workflows')
async def create_workflow(data: dict):
    return {'status': 'created', 'data': data}