from flask import Flask, jsonify, request
# from db_utils import ...

app = Flask(__name__)

# a welcoming message
@app.route('/welcome')
def welcome():
    return "[welcome message]"

# get all public entries feed info in the database
@app.route('/feed')
def public_feed():
    # return jsonify(see_public_feed() - name of function in db_utils)
    pass

# get public and private entries for that user by their username
@app.route('/<username>')
def username_entries(username):
    # try:
    #     entries_by_username = user_specific_posts(username) (user_specific_posts = function from db_utils)
    #     print(entries_by_username)
    #     return jsonify(entries_by_username)
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 500
    pass

# provides access to our support hub
@app.route('/support_hub')
def support_hub():
    # return jsonify(support_hub() - name of function in db_utils)
    pass

# add public entry
@app.route('/feed', methods=['POST'])
def add_public_entry():
    # public_entry = request.get_json()
    # try:
    #     user_entry(public_entry) - name of function in db_utils
    #     return jsonify({'status': 'success', 'message': 'Entry added.'})
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 400
    pass

# add a like to a public entry
@app.route('/feed', methods=['POST'])
def like_public_entry():
    # likes = request.get_json()
    # user_likes = request.get_json()
    # try:
    #     like_public_entry(like_pub_entry)
    #     return jsonify({'status': 'success', 'message': 'Like added.'})
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 400
    pass

# add a user like to a public entry
@app.route('/feed', methods=['POST'])
def user_like_pub_entry():
    # user_likes = request.get_json()
    # try:
    #     user_like_public_entry(user_likes)
    #     return jsonify({'status': 'success', 'message': 'User like added.'})
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 400
    pass

# so flask will automatically restart when you make code changes
if __name__ == '__main__':
    app.run(debug=True)