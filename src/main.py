from fastapi import FastAPI
from comerciantes.router import router as comerciantes_router
from productos.router import router as productos_router

app = FastAPI()

app.include_router(comerciantes_router)
app.include_router(productos_router)
