SELECT users.first_name, users.last_name, user2.first_name AS friend_first, user2.last_name AS friend_last
FROM mydb.users
LEFT JOIN friendships 
ON users.id = friendships.user_id
LEFT JOIN users AS user2
ON user2.id = friendships.friend_id;