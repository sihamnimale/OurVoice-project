from flask import Flask, jsonify, request, redirect, url_for
from b_db_utils import like_public_entry, see_public_feed, see_post_by_id, user_entry, user_specific_posts
from support_hub_data import resources
from wellness_resources import wellness_and_career_resources


app = Flask(__name__)

#----------------------------------------------------------------------------
#                          GENERAL INFORMATION
#----------------------------------------------------------------------------

"""
This file contains all Flask API routes used to communicate between the
client-side application (d_clientside_main.py) and the SQL database.

It handles the full pathway of user interaction, including:

MAIN FUNCTIONALITY:
- displaying the public feed (GET /feed)
- creating new public or private posts (POST /feed)
- retrieving all posts belonging to a specific user (GET /<username>)
- retrieving a single post by ID (GET /feed/<post_id>)
- handling likes on public posts (POST /feed/<post_id>)
- ensuring users cannot repeatedly like posts by redirecting after liking

SUPPORT FEATURES:
- returning Support Hub resources as JSON (GET /support_hub)
- returning Wellness and Career resources as JSON (GET /wellness_career)

ARCHITECTURE NOTES:
- this API layer acts as a bridge between the SQL queries in b_db_utils.py 
  and the client-side menu system in d_clientside_main.py
- routes return data in JSON format so they can be interpreted cleanly
  by the command-line interface

PORT BEHAVIOUR (IMPORTANT FOR MAC USERS):
- port 5000 frequently became unavailable on macOS due to background 
  system services occupying the port (e.g., ControlCentre, AirPlay Receiver)
- this caused JSONDecodeError issues on the client side
- switching the Flask server to port 5001 resolved the issue consistently
- port 5001 works smoothly across macOS and Windows machines
- This ensures consistent behaviour across all contributors’ devices 
and for anyone running the client application, including our project marker.

Overall, this file forms the backbone of the web API, enabling all
database communication and user interactions within OurVoice.
"""

#----------------------------------------------------------------------------
#                     WELCOME ROUTE
#----------------------------------------------------------------------------
# A welcoming message to the user.
@app.route('/welcome')
def welcome():
    return "[welcome message]"

#----------------------------------------------------------------------------
#                     PUBLIC FEED ROUTE (GET)
#----------------------------------------------------------------------------
# Establishing a route for the user to see all public posts.
@app.route('/feed')
def public_feed():
    """
    Returns all public posts stored in the database.
    Calls see_public_feed() from b_db_utils.
    """
    return jsonify(see_public_feed())

#----------------------------------------------------------------------------
#                     USER-SPECIFIC POSTS (GET)
#----------------------------------------------------------------------------
# Route to get both public and private entries for that user by their username.
@app.route('/<username>')
def username_entries(username):
    """
    Retrieves all posts (public + private) made by a given user.
    Parameters: username (str): username whose posts we are retrieving.

    Returns: JSON list of post rows.
    """
    try:
        # User_specific_posts function from db_utils.
        entries_by_username = user_specific_posts(username)
        print(entries_by_username)
        return jsonify(entries_by_username)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

#----------------------------------------------------------------------------
#                     SUPPORT HUB RESOURCES
#----------------------------------------------------------------------------
# Provides access to our support hub.
@app.route('/support_hub')
def support_hub_resources():
    """
    Returns all support hub categories and resources as JSON.
    """
    try: 
        return jsonify(resources) # return resources dict as JSON
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

#----------------------------------------------------------------------------
#                WELLNESS + CAREER RESOURCES
#----------------------------------------------------------------------------
# Provides access to our wellness and career hub.
@app.route('/wellness_career')
def wellness_career_resources_route():
    """
    Returns wellness and career resources as JSON.
    """
    try:
        return jsonify(wellness_and_career_resources)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

#----------------------------------------------------------------------------
#                 CREATE NEW POST (PUBLIC / PRIVATE)
#----------------------------------------------------------------------------
# Route to handle creating a new public or private entry.
@app.route('/feed', methods=['POST'])
def add_public_entry():
    """
    Inserts a new post into the database.

    Expects JSON in the format:
        {
            "name": username,
            "title": title_string,
            "post": post_content,
            "private_public": "public" or "private",
            "hashtags": "..."
        }

        Returns: 201 response+ JSON containing new post ID on success,
        otherwise an error message.
        """
    entry_data = request.get_json()
    if not entry_data:
        return jsonify({"error": "No data provided"}), 400
    try:
        new_post_id = user_entry(entry_data)
        return jsonify({
            "status": "success",
            "message": "Entry added.",
            "post_id": new_post_id
        }), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

#----------------------------------------------------------------------------
#                   VIEW A POST BY ID (GET)
#----------------------------------------------------------------------------
@app.route('/feed/<int:post_id>', methods=['GET'])
def see_post_by_postid(post_id):
    """
    Establishing a GET route for the user to see public posts by the post_id.

    This is a necessary reroute to the below like_pub_entry function, which is a POST route.
    Without this, every time the user refreshes '/feed/<int:post_id>', the like_public_entry
    function would also be triggered, meaning a user could like a post by continually
    refreshing the '/feed/<int:post_id>'.
    The reroute occurs in the return line using redirect and url_for.

    This see_post_by_postid function simply retrieves a post by its ID, using the
    see_post_by_id function from DB_utils.
    """
    post = see_post_by_id(post_id)
    return jsonify(post)

#----------------------------------------------------------------------------
#                   LIKE A PUBLIC POST (POST)
#----------------------------------------------------------------------------
# Establishing a POST route to enable a user to like to a public entry (see description above).
@app.route('/feed/<int:post_id>', methods=['POST'])
def like_pub_entry(post_id):
    data = request.json # to retrieve the username of the person liking the post
    if not data or "userlike" not in data:
        return jsonify({"error": "Username required"}), 400
    userlike = data["userlike"]
    try:
        # From DB_utils, this function changes the SQL DB with a like and userlike.
        like_public_entry(userlike, post_id)
        # Reroute to GET function/route above
        return redirect(url_for('see_post_by_postid', post_id=post_id))
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# So flask will automatically restart when you make code changes
if __name__ == '__main__':
    app.run(debug=True, port=5001)
