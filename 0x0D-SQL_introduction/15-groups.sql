--  lists the number of records with the same score in the table second_table
-- the number of records for this score with the label number

SELECT `score`, COUNT('score') 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC; 
