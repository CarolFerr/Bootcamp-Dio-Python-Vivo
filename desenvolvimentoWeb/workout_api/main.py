from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

# if __name__ == 'main':
#     import uvicorn
#     # Com o reaload=True não há necessidade de se parar o servidor para realizar alterações
#     # ele salva as alteraçõe automaticamente sem a necessidade do servidor parar
#     uvicorn.run('main:app', host='0.0.0.0', port=1000, log_level='info', reload=True)
