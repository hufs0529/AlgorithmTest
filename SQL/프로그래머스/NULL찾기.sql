select ANIMAL_TYPE, 
        IFNULL(NAME, 'No name') AS NAME,
        SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID