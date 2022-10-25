SELECT city, population
FROM north_american_cities
where country = "Canada";

SELECT city
FROM north_american_cities
WHERE country = "United States"
ORDER BY latitude DESC;


SELECT city 
FROM north_american_cities
where longitude < -87.629798
order by longitude;

SELECT city 
FROM north_american_cities
where country = "Mexico"
order by population DESC
limit 2;

SELECT city 
FROM north_american_cities
where country = "United States"
order by population DESC
limit 2 offset 2;




