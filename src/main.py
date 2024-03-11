import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from products.router import router as product_router
from wildberies.router import router as wildberries_router
from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(product_router, tags=["Product"])
app.include_router(wildberries_router, tags=["Wilberries"])
templates = Jinja2Templates(directory="templates")



@app.get('/')
def started_index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
