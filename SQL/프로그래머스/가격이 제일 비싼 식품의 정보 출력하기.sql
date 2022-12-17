select *
from FOOD_PRODUCT
where PRICE IN (select MAX(PRICE) from FOOD_PRODUCT);