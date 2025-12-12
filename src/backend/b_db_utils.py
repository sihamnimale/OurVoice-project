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


# INSERTING NEW USERS INTO THE USER TABLE IN THE DATABASE
def username_entry(entry_data):
    db_name="my_CFG_project"
    connection = _connect_to_db(db_name)
    cursor = connection.cursor()

    sql = """
            INSERT INTO users (username)
            VALUES (%s)
        """
    values = (entry_data["username"],)

    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

#RETRIEVING THE USERS FROM THE USER TABLE IN THE DATABASE
def get_usernames():
    db_name="my_CFG_project"
    connection = _connect_to_db(db_name)
    cursor = connection.cursor()

    sql = """
            SELECT username FROM users
        """

    cursor.execute(sql)
    usernames = cursor.fetchall()
    cursor.close()
    connection.close()

    for user in usernames:
        usernames = [username[0] for username in usernames]

    return usernames


#----------------------------------------------------------------------------
#                  FETCHING POSTS FROM THE DATABASE:
#----------------------------------------------------------------------------
# Function connecting to the SQL DB to retrieve all public posts.
def see_public_feed():
    """
    Retrieves all public posts from the journal_entries table so they can be shown in
    the main feed. Private posts are excluded.

    Returns: A list of rows representing public posts.
    """
    db_name = 'my_CFG_project'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    db_connection.start_transaction()
    # The query specifies we only want public posts to be viewable on Flask.
    query = """SELECT * FROM journal_entries
               WHERE private_public = 'public'
               ORDER BY post_id DESC"""
    cur.execute(query)
    posts = cur.fetchall()

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
    db_name = 'my_CFG_project'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # The query specifies we only want public posts of a particular id to be viewable on Flask.
    query = """SELECT * FROM journal_entries
               WHERE post_id = %s AND private_public = 'public'"""
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
    db_name = "my_CFG_project"
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    # Query both public and private posts for a specific user from the most recent posts to be viewed.
    db_connection.start_transaction()
    query = """
        SELECT * FROM journal_entries
        WHERE username = %s
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
def user_entry(entry_data, db_name="my_CFG_project"):
    """
    Inserts a new post into the journal_entries table.
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
        INSERT INTO journal_entries (username, title, post, private_public, likes, user_likes, hashtags)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        entry_data["username"],          # maps to username column
        entry_data["title"],
        entry_data["post"],
        entry_data["private_public"],
        0,                           # likes
        "",                          # user_likes
        entry_data["hashtags"]
    )
    cursor.execute(sql, values)
    connection.commit()
    new_post_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return new_post_id

#----------------------------------------------------------------------------
#                       LIKING A PUBLIC POST:
#----------------------------------------------------------------------------
# Function connecting to the SQL DB to change the likes and user_likes column in SQL.
def like_public_entry(userlike, post_id):
    """
    Updates the likes count for a given post and appends the username to the
     user_likes field.
     Parameters:  userlike (str): Username of the person liking the post.
     post_id (int): ID of the post being liked.

    Returns: the updated post row after the like has been applied.
    """
    db_name = 'my_CFG_project'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    try:
        db_connection.start_transaction()
        # This query specifies we only want to update the likes and user_likes column on SQL
        # in the journal_entries table.
        query = """UPDATE journal_entries 
                   SET likes = likes + 1,
                       user_likes = CONCAT(user_likes, %s, " ")
                   WHERE post_id = %s"""

        cur.execute(query, (userlike, post_id))
        db_connection.commit()

        # this is a further query to return the particular liked post
        query_post = """SELECT * FROM journal_entries WHERE post_id = %s"""
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
# Function connecting to the SQL DB to retrieve user_likes ONLY, as a list.
# This is necessary for the clientside run(), to check if the user liking a particular
# Post has liked the post previously. If their username is in the list of user_likes,
# As produced by this function, they will not be able to like the post again.
# This function therefore helps prevent users from liking posts repeatedly.
def user_likes(post_id):
    db_name = 'my_CFG_project'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()

    db_connection.start_transaction()
    # this query requests just the user_likes for a particular post
    query = """SELECT user_likes FROM journal_entries WHERE post_id = %s"""
    cur.execute(query, (post_id,))
    userlikes = cur.fetchone()

    if db_connection:
        cur.close()
        db_connection.close()

    if userlikes is None:
        return []

    # as the user_likes in SQL are a string, the data needs to be returned as a list
    return userlikes[0].split()

#----------------------------------------------------------------------------
#                       POSTING AFFIRMATIONS TO THE DATABASE:
#----------------------------------------------------------------------------
# Function inserting a new row into the SQL DB that includes an affirmation.
# This is necessary for us to store the affirmations given to the clients.

def attach_affirmation_to_post(post_id, affirmation, db_name="my_CFG_project"):
    
    conn = None
    try:
        conn = _connect_to_db(db_name)
        cur = conn.cursor()

        sql = "UPDATE journal_entries SET affirmation = %s WHERE post_id = %s"
        cur.execute(sql, (affirmation, post_id))
        conn.commit()

        cur.close()
        return True

    except Exception as e:
        if conn:
            conn.rollback()
        print("Error attaching affirmation:", e)
        return False

    finally:
        if conn:
            conn.close()
