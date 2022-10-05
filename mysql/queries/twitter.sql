SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 2;