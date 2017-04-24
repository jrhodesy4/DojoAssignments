SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM address
JOIN customer
ON address.address_id = customer.address_id 
WHERE address.city_id = 312;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

SELECT actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

SELECT customer.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM city
JOIN address
ON city.city_id = address.city_id
JOIN customer
ON address.address_id = customer.address_id
WHERE city.city_id = 1 AND customer.store_id = 1 OR city.city_id = 42 AND customer.store_id = 1 OR city.city_id = 312 AND customer.store_id = 1 OR city.city_id = 459 AND customer.store_id = 1;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE '%Behind%';

SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Drama' AND film.rental_rate = 2.99;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE CONCAT(actor.first_name, ' ', actor.last_name) = 'SANDRA KILMER' AND category.name = 'Action';




