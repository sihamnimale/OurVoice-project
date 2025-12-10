import mysql.connector
from a_config import USER, PASSWORD, HOST

#----------------------------------------------------------------------------
#                      CUSTOM EXCEPTIONS:
#----------------------------------------------------------------------------
# Custom exception to handle database connection errors.
class DbConnectionError(Exception):
    pass

#----------------------------------------------------------------------------
#                    DATABASE CONNECTION HELPERS:
#----------------------------------------------------------------------------
# Private function to connect to the database.
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

#----------------------------------------------------------------------------
#                  FETCHING POSTS FROM THE DATABASE:
#----------------------------------------------------------------------------
# Function connecting to the SQL DB to retrieve all public posts.
def see_public_feed():
    """
    Retrieves all public posts from the posts_table so they can be shown in
    the main feed. Private post are excluded.

    Returns: A list of rows representing public posts.
    """
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    db_connection.start_transaction()
    # The query specifies we only want public posts to be viewable on Flask.
    query = """SELECT * FROM posts_table
            WHERE private_public = 'public'"""
    cur.execute(query)
    posts = cur.fetchall()

    for post in posts:
        print(post)

    if db_connection:
        db_connection.close()

    return posts

# Function connecting to the SQL DB to retrieve public posts by the post_id.
# This function is necessary for the GET see_post_by_postid function in the API/server file, as
# it acts as a reroute to the POST like_pub_entry function, also found in the API/server file.
def see_post_by_id(post_id):
    """
    Gets one public post from the database using its post_id.
    Parameter: post_id (int): the ID of the post we want to look up.

    Returns: the post row if it exists and is public, otherwise None.
    """
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # The query specifies we only want public posts of a particular id to be viewable on Flask.
    query = """SELECT * FROM posts_table
                WHERE post_id = %s and private_public = 'public'"""
    cur.execute(query, (post_id,))
    post = cur.fetchone()

    if db_connection:
        cur.close()
        db_connection.close()

    return post

#----------------------------------------------------------------------------
#                RETRIEVING USER-SPECIFIC POSTS:
#----------------------------------------------------------------------------
# Function to obtain public and private posts from a specific user.
def user_specific_posts(username):
    """
    Retrieves both public and private posts for a given user, ordered
    from the most recent to the oldest.
    Parameters: username (str): Username whose posts we want to see.

    Returns: A list of post rows for that user.
    """
    db_name = "my_CFG_project_test_likes"
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    # Query both public and private posts for a specific user from the most recent posts to be viewed.
    db_connection.start_transaction()
    query = """
        SELECT * FROM posts_table
        WHERE name = %s
        ORDER BY post_id DESC
    """

    cur.execute(query, (username,))
    user_posts = cur.fetchall()
    
    if db_connection:
        cur.close()
        db_connection.close()
    return user_posts

#----------------------------------------------------------------------------
#                        CREATING NEW POSTS:
#----------------------------------------------------------------------------
# Function to add a new post into the SQL database.
def user_entry(entry_data, db_name="my_CFG_project_test_likes"):
    """
    Inserts a new post into the posts_table.
    entry_data should contain a dict:
    {
        "name": "username",
        "title": "title of the post"
        "post": "the content of the post",
        "private_public": "public" or "private"
        "hashtags": "hashtags"
    }

    Parameters: entry_data (dict): Dictionary with post details.
    db_name (str): Name of the DB to insert into.

    Returns: the ID of the newly created post.
    """
    connection = _connect_to_db(db_name)
    cursor = connection.cursor()
    sql = """
        INSERT INTO posts_table (name, title, post, private_public, likes, userlikes, hashtags)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (entry_data["name"], entry_data["title"], entry_data["post"], entry_data["private_public"],
              0, "", entry_data["hashtags"])
    cursor.execute(sql, values)
    connection.commit()
    new_post_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return new_post_id

#----------------------------------------------------------------------------
#                       LIKING A PUBLIC POST:
#----------------------------------------------------------------------------
# Function connecting to the SQL DB to change the likes and userlikes column in SQL.
def like_public_entry(userlike, post_id):
    """
    Updates the likes count for a given post and appends the username to the
     userlikes field.
     Parameters:  userlike (str): Username of the person liking the post.
     post_id (int): ID of the post being liked.

    Returns: the updated post row after the like has been applied.
    """
    db_name = 'my_CFG_project_test_likes'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    try:
        db_connection.start_transaction()
        # This query specifies we only want to update the likes and userlikes column on SQL
        # in the posts table.
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

#----------------------------------------------------------------------------
#                       CHECKING USER LIKES:
#----------------------------------------------------------------------------
# Function connecting to the SQL DB to retrieve userlikes ONLY, as a list.
# This is necessary for the clientside run(), to check if the user liking a particular
# Post has liked the post previously. If their username is in the list of userlikes,
# As produced by this function, they will not be able to like the post again.
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

#----------------------------------------------------------------------------
#                       POSTING AFFRIMATIONS TO THE DATABASE:
#----------------------------------------------------------------------------
# Function inserting a new row into the SQL DB that invludes an affirmation.
# This is necessary for us to store the affirmations given to the clients.

def insert_post_with_affirmation(affirmation, name=None, title=None, content=None,
                                 private_public="private", hashtags="", db_name="my_CFG_project_test_likes"):
    conn = None
    try:
        conn = _connect_to_db(db_name)
        cur = conn.cursor()
        # this query posts affirmations into the databse.
        sql = """
            INSERT INTO posts_table
            (name, title, post, private_public, likes, userlikes, hashtags, affirmation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, title, content, private_public, 0, "", hashtags, affirmation)
        cur.execute(sql, values)
        conn.commit()
        new_id = cur.lastrowid
        cur.close()
        return new_id
    except Exception as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()