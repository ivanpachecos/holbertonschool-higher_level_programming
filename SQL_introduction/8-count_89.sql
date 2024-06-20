-- COunt 89 --

SELECT COUNT(*)
FROM first_table
WHERE id > (SELECT MAX(id) FROM first_table);