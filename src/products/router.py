from fastapi import APIRouter, Depends, HTTPException
from fastapi.openapi.models import Response
from starlette import status

from .models import Product as models_product
from sqlalchemy.orm import Session
from .schemas import Product as shemas_product
from database import get_db


router = APIRouter(
    prefix="/product"
)


@router.get('/')
def get_notes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    products = db.query(models_product).filter(
        models_product.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(products), 'products': products}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: shemas_product, db: Session = Depends(get_db)):
    new_products = models_product(**payload.dict())
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    return {"status": "success", "products": new_products}

@router.patch('/{product_id}')
def update_note(product_id: str, payload: shemas_product, db: Session = Depends(get_db)):
    products_query = db.query(models_product).filter(models_product.id == product_id)
    db_products = products_query.first()

    if not db_products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {product_id} found')
    update_data = payload.dict(exclude_unset=True)
    products_query.filter(models_product.id == product_id).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_products)
    return {"status": "success", "products": db_products}


@router.get('/{product_id}')
def get_post(product_id: str, db: Session = Depends(get_db)):
    products = db.query(models_product).filter(models_product.id == product_id).first()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "products": products}


@router.delete('/{product_id}')
def delete_post(product_id: str, db: Session = Depends(get_db)):
    products_query = db.query(models_product).filter(models_product.id == product_id)
    note = products_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {id} found')
    products_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

