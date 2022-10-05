-- ! 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order.
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;


-- ! 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. 
SELECT countries.name AS Country_name, count(cities.country_code) AS Total_number_of_cities FROM cities
JOIN countries ON cities.country_code = countries.code
GROUP BY cities.country_code
ORDER BY count(cities.country_code) DESC;


-- ! 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. 
SELECT cities.name AS city_name, cities.population FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE countries.name = 'Mexico' 
AND cities.population > 500000
ORDER BY cities.population DESC;


-- ! 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order.
SELECT countries.name, languages.language, languages.percentage FROM languages
JOIN countries ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;


-- ! 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? 
SELECT countries.name, countries.surface_area, countries.population FROM countries
WHERE countries.surface_area < 501 
and countries.population > 100000;


-- ! 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years?
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' 
and countries.capital > 200 
and countries.life_expectancy > 75; 


-- ! 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population.
SELECT countries.name, cities.name, cities.population, cities.district FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE cities.population > 500000 
and countries.name = 'Argenand cities.district = 'Buenos Aires';


-- ! 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order.
SELECT countries.region, COUNT(countries.name) AS num_of_countries FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.name) DESC;


SELECT * FROM cities;
SELECT * FROM countries;
SELECT * FROM languages;