DROP DATABASE IF EXISTS my_CFG_project_test_likes;
CREATE DATABASE my_CFG_project_test_likes;
USE my_CFG_project_test_likes;

CREATE TABLE posts_table (
	post_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(50),
    post VARCHAR(50),
    private_public VARCHAR(20),
    likes INTEGER,
    userlikes VARCHAR(250)
);

INSERT INTO posts_table 
(post_id, name, post, private_public, likes, userlikes)
VALUES
(1, "test", "test", "public", 0, "");

SELECT * FROM posts_table;