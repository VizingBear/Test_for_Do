from fastapi import APIRouter, Response, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status
from database import get_db
from .models import Product_Wildberies as product_wildberies_model
from .shemas import Product_Wildberies as product_wildberies_shemas

router = APIRouter(
    prefix="/wildberries"
)

@router.get('/')
def get_product_by_id(nm_id: int, db: Session = Depends(get_db)):
    wildberries = db.query(product_wildberies_model).filter(
        product_wildberies_model.nm_id == nm_id).first()
    return wildberries


@router.get('/')
def get_all_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(product_wildberies_model).offset(skip).limit(limit).all()


@router.post('/')
def create_product(product_data: product_wildberies_shemas, db: Session = Depends(get_db)):
    db_wildberries = product_wildberies_model(**product_data.dict())
    db.add(db_wildberries)
    db.commit()
    db.refresh(db_wildberries)
    return {"status": "success", "products": db_wildberries}




@router.get('/barcode/{count_id}')  #Получение баркода
def returned_wildberies_barcode(count_id:int, response: Response):
    content = {"count": count_id}
    header = {'AUTHORIZATIONS': "eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwMjI2djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyNTgxNjY3MCwiaWQiOiJiMWVkOTQzNS0wODcyLTQ1NTUtYjJhZi00M2ZkZTkyNmMyZWEiLCJpaWQiOjE1NzczOTEwLCJvaWQiOjE0MjA1MjQsInMiOjEwNzM3NDIzMzQsInNpZCI6ImU5YjE2OTlmLTc4NDUtNDFiNi1iN2IwLTU1NDJiNDhkYzg1MSIsInQiOmZhbHNlLCJ1aWQiOjE1NzczOTEwfQ.uV7tI5UjwUJx8zAUTUqRmPJ6T6yHB_BZ67k6OLzovyGBe3rtgzwyfcTlzf97SNshkO8WGaBoqxpMSPq_oTtlhA"}
    return JSONResponse(content=content, headers=header)