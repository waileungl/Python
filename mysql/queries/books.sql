INSERT INTO users(name, created_at, updated_at)
VALUES('Jane Amsden', now(), now()), ('Emily Dixon', now(), now()), ('Theodore Dostoevsky', now(), now()), ('William Shapiro', now(), now()),  ('Lao Xiu', now(), now());

INSERT INTO books(title, num_of_pages, created_at, updated_at)
VALUES('C Sharp', 200, now(), now()), ('Java', 200, now(), now()), ('Python', 100, now(), now()), ('PHP', 80, now(), now()),  ('Ruby', 100, now(), now());

UPDATE books
SET title = 'C#'
WHERE id = 1;

UPDATE users
SET name = 'Bill'
WHERE id = 4;

INSERT INTO favorites(user_id, book_id)
VALUES(1, 1), (1, 2);

INSERT INTO favorites(user_id, book_id)
VALUES(2, 1), (2, 2), (2, 3);

INSERT INTO favorites(user_id, book_id)
VALUES(3, 1), (3, 2), (3, 3), (3, 4);

INSERT INTO favorites(user_id, book_id)
VALUES(4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

SELECT name, title, book_id FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN books ON books.id = favorites.book_id
WHERE book_id = 3;

DELETE FROM favorites
WHERE book_id = 3 LIMIT 1;

INSERT INTO favorites(user_id, book_id)
VALUES (5, 2);

SELECT title AS favorite_books FROM favorites
JOIN books ON books.id = favorites.book_id
WHERE user_id = 3;

SELECT name AS Ruby_Lover FROM favorites
JOIN users ON users.id = favorites.user_id
WHERE book_id = 5;

SELECT * FROM favorites;
SELECT * FROM books;
SELECT * FROM users;