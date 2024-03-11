# Тестовое задание
Задание разделено на 2 части:
- создание концепции базы данных для определения товара с его свойствами;
- создание API для личного кабинета сервиса "Wildberries"

## Задание 1

* [Ссылка](https://drive.google.com/file/d/17JqEQG0YXV1-_Bap8KamgoKwf6gyiEot/view?usp=sharing) - Визуализация таблицы.

Описание таблиц:
1. Таблица Product - используется для отображения товара со свойствами конкретной позиции.
2. CharValues  - хранение значения свойств для конкретной характеристики.
3. Properties - хранение свойств товаров.
4. PropertyValues  - используется в том случае, если Properties.valueType не стандартный тип значения.

### Пример использования

_Product_

id: 1  quantity: 50, name: 'Кросовок', description: 'Большое описание'

id: 2  quantity: 70, name: 'Футболка', description: 'Большое описание'



_CharValues_

product_Id: 1 , property_Id: 1, valueType: list, value: 1(ссылка на белый цвет)

product_Id: 2 , property_Id: 2, valueType: number, value: 37 

 product_Id: 1, property_Id: 1, valueType: list, value: 2(ссылка на синий цвет)

product_Id: 2,  property_Id: 2, valueType: number, value: 39


_Properties_

id: 1, property: 'Цвет', valueType: 'list', 

id: 2, property: 'Размер', valueType: 'number'

_PropertyValues_:

id: 1, property_Id: 1, value: 'Белый'

id: 2, property_Id: 1, value: 'Красный'

id: 3, property_Id: 1, value: 'Синий'


## Задание 2


_Для запуска приложения необходимо ввести команду в терминале из папки src._


```bash
uvicorn main:app --reload
```

_Для просмотра API необходимо ввести в адресной строке ._

Explain how to test the project and give some example.

```bash
http://127.0.0.1:8000/docs
```

