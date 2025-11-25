import mysql.connector
from a_config import USER, PASSWORD, HOST

# custom exception to handle database connection errors
class DbConnectionError(Exception):
    pass

# private function to connect to the database
def _connect_to_db(db_name):
    # Connects to the MySQL database with the given name.
    # Returns a connection object.
    try:
        connect = mysql.connector.connect(
            host=HOST,               # MySQL server hostname
            user=USER,               # MySQL username from config
            password=PASSWORD,       # MySQL password from config
            database=db_name         # Name of the database to connect
        )
        return connect

    except Exception:
        raise DbConnectionError("Database connection failed.")

# function connecting to the SQL DB to retrieve all public posts
def see_public_feed():
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # the query specifies we only want public posts to be viewable on Flask
    query = """SELECT * FROM posts_table
            WHERE private_public = 'public'"""
    cur.execute(query)
    posts = cur.fetchall()

    for post in posts:
        print(post)

    if db_connection:
        db_connection.close()

    return posts

# function connecting to the SQL DB to retrieve public posts by the post_id.
# this function is necessary for the GET see_post_by_postid function in the API/server file, as
# it acts as a reroute to the POST like_pub_entry function, also found in the API/server file.
def see_post_by_id(post_id):
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # the query specifies we only want public posts of a particular id to be viewable on Flask
    query = """SELECT * FROM posts_table
                WHERE post_id = %s and private_public = 'public'"""
    cur.execute(query, (post_id,))
    post = cur.fetchone()

    if db_connection:
        cur.close()
        db_connection.close()

    return post

# TO COMPLETE function to obtain public and private posts from a specific user
def user_specific_posts(username):
    pass

# TO COMPLETE function that directs the user to our support hub
def support_hub():
    pass

# TO COMPLETE function to add an entry
def user_entry():
    pass

# function connecting to the SQL DB to change the likes and userlikes column in SQL
def like_public_entry(userlike, post_id):
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    try:
        db_connection.start_transaction()
        # this query specifies we only want to update the likes and userlikes column on SQL
        # in the posts table
        query = """UPDATE posts_table 
            SET likes = likes + 1,
            userlikes = CONCAT(userlikes, %s, " ")
            WHERE post_id = %s"""

        cur.execute(query, (userlike, post_id))
        db_connection.commit()

        # this is a further query to return the particular liked post
        query_post = """SELECT * FROM posts_table WHERE post_id = %s"""
        cur.execute(query_post, (post_id,))
        liked_post = cur.fetchone()
        return liked_post

    except Exception as e:
        db_connection.rollback()
        raise e

    finally:
        cur.close()
        db_connection.close()

# function connecting to the SQL DB to retrieve userlikes ONLY, as a list.
# this is necessary for the clientside run(), to check if the user liking a particular
# post has liked the post previously. If their username is in the list of userlikes,
# as produced by this function, they will not be able to like the post again.
# This function therefore helps prevent users from liking posts repeatedly.
def user_likes(post_id):
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # this query requests just the userlikes for a particular post
    query = """SELECT userlikes FROM posts_table WHERE post_id = %s"""
    cur.execute(query, (post_id,))
    userlikes = cur.fetchone()

    if db_connection:
        cur.close()
        db_connection.close()

    if userlikes is None:
        return []

    # as the userlikes in SQL are a string, the data needs to be returned as a list
    return userlikes[0].split()