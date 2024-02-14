-- This script lists score and name of all records of table 'second_table': no display of rows without name value and records are listed in descending score order.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
