SELECT name ,age, CAST(STRFTIME('%Y', DATE('now', '-' || age || ' year')) AS INT) AS birth_year,
--  Peter P.  30   1995  
CASE 
	WHEN CAST(STRFTIME('%Y', DATE('now', '-' || age || ' year')) AS INT)  <=1964 
        THEN 'Baby Boomer'
	--                                  |'- 30 year'         |
	WHEN CAST(STRFTIME('%Y', DATE('now', '-' || age || ' year')) AS INT) BETWEEN  1965 AND 1980 
        THEN 'Gen. X'
	WHEN CAST(STRFTIME('%Y', DATE('now', '-' || age || ' year')) AS INT) BETWEEN  1981 AND 1996 
        THEN 'Millennial'
 	WHEN CAST(STRFTIME('%Y', DATE('now', '-' || age || ' year')) AS INT) BETWEEN  1997 AND 2012 
        THEN 'Gen. Z'
	ELSE 'NO GEN'
END generation
FROM student

-- 