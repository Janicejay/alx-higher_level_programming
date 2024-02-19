-- Lists all cities contained in the database 'hbtn_0d_usa'

-- Select the columns to retrieve data from
SELECT cities.id, cities.name, states.name
-- Select the table
FROM cities
LEFT JOIN states ON states.id = cities.state_id
-- Order in ascending order by cities' id
ORDER BY cities.id ASC;
