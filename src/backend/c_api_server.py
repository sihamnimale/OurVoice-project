from flask import Flask, jsonify, request, redirect, url_for
from b_db_utils import like_public_entry, see_public_feed, see_post_by_id

app = Flask(__name__)

# a welcoming message to the user
@app.route('/welcome')
def welcome():
    return "[welcome message]"

# establishing a route for the user to see all public posts
@app.route('/feed')
def public_feed():
    return jsonify(see_public_feed())


# TO COMPLETE get public and private entries for that user by their username
@app.route('/<username>')
def username_entries(username):
    # try:
    #     entries_by_username = user_specific_posts(username) (user_specific_posts = function from db_utils)
    #     print(entries_by_username)
    #     return jsonify(entries_by_username)
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 500
    pass

# TO COMPLETE provides access to our support hub
@app.route('/support_hub')
def support_hub():
    # return jsonify(support_hub() - name of function in db_utils)
    pass

# TO COMPLETE add public entry
@app.route('/feed', methods=['POST'])
def add_public_entry():
    # public_entry = request.get_json()
    # try:
    #     user_entry(public_entry) - name of function in db_utils
    #     return jsonify({'status': 'success', 'message': 'Entry added.'})
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 400
    pass


# establishing a GET route for the user to see public posts by the post_id.
# This is a necessary rereroute to the below like_pub_entry function, which is a POST route.
# Without this, everytime the user refreshes '/feed/<int:post_id>', the like_public_entry function
# would also be triggered meaning a user could like a post by continually refreshing
# the '/feed/<int:post_id>'. The reroute occurs in the return line using redirect and url_for.
# This see_post_by_postid function simply retrieves a post by its ID, using the see_post_by_id
# function from DB_utils.
@app.route('/feed/<int:post_id>', methods=['GET'])
def see_post_by_postid(post_id):
    post = see_post_by_id(post_id)
    return jsonify(post)

# establishing a POST route to enable a user to like to a public entry (see description above)
@app.route('/feed/<int:post_id>', methods=['POST'])
def like_pub_entry(post_id):
    data = request.json # to retrieve the username of the person liking the post
    if not data or "userlike" not in data:
        return jsonify({"error": "Username required"}), 400
    userlike = data["userlike"]
    try:
        # from DB_utils, this function changes the SQL DB with a like and userlike
        like_public_entry(userlike, post_id)
        # reroute to GET function/route above
        return redirect(url_for('see_post_by_postid', post_id=post_id))
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# so flask will automatically restart when you make code changes
if __name__ == '__main__':
    app.run(debug=True)