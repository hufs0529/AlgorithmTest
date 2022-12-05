select a.FLAVOR
from FIRST_HALF AS a
left join ICECREAM_INFO AS b
on a.FLAVOR = b.FLAVOR
where a.TOTAL_ORDER > 3000 AND b.INGREDIENT_TYPE like 'fruit_based'
order by a.TOTAL_ORDER desc;