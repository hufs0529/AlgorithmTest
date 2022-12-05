select PRODUCT_CODE, sum(p.PRICE * o.SALES_AMOUNT)as sales
from PRODUCT p join OFFLINE_SALE o
on p.PRODUCT_ID = o.PRODUCT_ID
group by p.PRODUCT_CODE
order by sales desc, PRODUCT_CODE asc;