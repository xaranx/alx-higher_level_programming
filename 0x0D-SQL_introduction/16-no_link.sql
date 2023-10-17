-- lists all records of the table second_table
-- Don’t list rows without a name value
-- Records should be listed by descending score

SELECT score, name FROM second_table
WHERE name != "" AND name IS NOT NULL
ORDER BY score DESC;
