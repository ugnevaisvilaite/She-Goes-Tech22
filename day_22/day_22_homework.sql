#LESSON 6

SELECT title, domestic_sales, international_sales 
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;


SELECT title, domestic_sales, international_sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;


SELECT title, rating
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;

#LESSON 7

SELECT DISTINCT building FROM employees;

SELECT  building_name, capacity FROM buildings;

SELECT distinct building_name, role FROM buildings
LEFT JOIN employees
ON building_name = employees.building;

#LESSON 8

SELECT name, role FROM employees
where building IS NULL;

SELECT building_name FROM buildings
LEFT JOIN employees
ON buildings.building_name = employees.building
WHERE employees.building IS NULL; 

#LESSON 9

SELECT DISTINCT title,(domestic_sales + international_sales)/1000000 AS sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id;

SELECT DISTINCT title,(rating * 10) AS rating_percentage
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id;

SELECT title
FROM movies
WHERE year%2 = 0;

#LESSON 10

SELECT max(years_employed) AS longest_employed
FROM employees;

SELECT role, AVG(Years_employed) AS average_employed
FROM employees
GROUP BY role;

SELECT building, SUM(Years_employed) AS total_employed
FROM employees
GROUP BY building;

#LESSON 11

SELECT role, count(role) AS count_number
FROM employees
where role = "Artist";

SELECT role, count(name) AS number_of_people
FROM employees
GROUP BY role;

SELECT role, sum(years_employed)
FROM employees
WHERE role = 'Engineer';

#LESSON 12

SELECT director, count(title)
FROM movies
GROUP BY director;

SELECT director,sum(domestic_sales) + sum(international_sales) AS sales
FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
GROUP BY director;

#LESSON 13

INSERT INTO movies 
VALUES (15, "Toy Story 4", "John Lasseter", 2010, 123);

INSERT INTO boxoffice
(movie_id, rating, domestic_sales, international_sales)
VALUES (15, 8.7, 340000000, 270000000);

#LESSON 14

UPDATE movies
SET director = "John Lasseter"
WHERE id = 2;

UPDATE movies
SET year = 1999 
WHERE id = 3;

UPDATE movies
SET title = "Toy Story 3",
    director = "Lee Unkrich"
WHERE ID = 11;

#LESSON 15

DELETE FROM movies
WHERE year < 2005;

DELETE FROM movies
WHERE director = "Andrew Stanton";

#LESSON 16

CREATE TABLE Database (
    name STRING PRIMARY KEY,
    version INTEGER,
    year INTEGER, 
    download_count INTEGER
);


#LESSON 17

ALTER TABLE movies
ADD Aspect_ratio FLOAT;

ALTER TABLE movies
ADD Language TEXT
    DEFAULT English;

#LESSON 18

DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS boxoffice;

