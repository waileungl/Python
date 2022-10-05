INSERT INTO dojos (name, created_at, updated_at)
VALUES('San Jose', now(), now()), ('Seattle', now(), now()), ('New York', now(), now());

DELETE FROM dojos
WHERE id < 16;

INSERT INTO dojos (name, created_at, updated_at)
VALUES('William Liu', now(), now()), ('Mike Kok', now(), now()), ('Bob Liu', now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES('William', 'Liu', 26, 16, now(), now()), ('Mike', 'Kok', 24, 16, now(), now()), ('Bob', 'Liu', 30, 16, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES('Will', 'Lau', 21, 17, now(), now()), ('Miki', 'Guo', 29, 17, now(), now()), ('Alex', 'Huang', 40, 17, now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES('Vita', 'Pancakes', 20, 18, now(), now()), ('Meiqi', 'bae', 18, 18, now(), now()), ('Joyce', 'Yu', 20, 18, now(), now());

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE name = 'San Jose';

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE name = 'New York';

SELECT first_name, last_name, name AS dojo_name FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE first_name = 'Joyce';
