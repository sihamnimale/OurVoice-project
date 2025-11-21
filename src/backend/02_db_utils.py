import mysql.connector
from config import USER, PASSWORD, HOST

# Custom exception to handle database connection errors
class DbConnectionError(Exception):
    pass

# Private function to connect to the database
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


# function to obtain information from the DB (public entries)
def see_public_feed(user):
    pass

# function to obtain public and private posts from a specific user
def user_specific_posts(username):
    pass

# function that directs the user to our support hub
def support_hub():
    pass

# function to add an entry
def user_entry():
    pass

# function to add a like a public entry
def like_public_entry(new_likes):
    pass

# function to add a user like to a public entry
def user_like_public_entry(new_user_like):
    pass