import requests
from b_db_utils import user_likes
# import classes for run function

# this function will enable the user to see all public posts via the Flask interface
def get_public_feed():
    url = 'http://127.0.0.1:5000/feed'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# this function will provide a json of all public and private entries that user has input
def get_username_entries(username):
    url = f'http://127.0.0.1:5000/{username}'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# TO COMPLETE provide user with a list of support resources
def support_hub():
    # url = 'http://127.0.0.1:5000/support_hub'
    # result = requests.get(url, headers={'content-type': 'application/json'})
    # return result.json()
    pass

# this function will enable the user to add a like a public entry in their feed
# and their username will also be added to the userlikes column on SQL and to the list of
# userlikes, as produced by the user_likes function in DB_utils.
def like_entry(username, post_id):
    url = f'http://127.0.0.1:5000/feed/{post_id}'
    result = requests.post(
        url, json={"userlike": username},
        headers={'content-type': 'application/json'})
    return result.json()

# # This function collects a user's journal entry from the terminal,
# # asks whether the entry should be public or private, and then sends
# # the data as JSON to the Flask API route POST /feed. The API then
# # stores the entry in the SQL database. If the request is successful,
# # the user is shown a confirmation message and the ID of their new post.
def create_post(username):
    print("\nCreate a New Post")
    post_content = input("Write your entry:\n> ")
    visibility = input("Make this public or private? (p/pr): ").lower()
    private_public = "public" if visibility == "p" else "private"
    entry_data = {"name": username,"post": post_content,"private_public": private_public}
    url = "http://127.0.0.1:5000/feed"
    result = requests.post(url, json=entry_data, headers={"content-type": "application/json"})
    response_data = result.json()
    if result.status_code == 201:
        print("\nYour post has been created successfully!")
        print("Post ID:", response_data["post_id"])
    else:
        print("\nSomething went wrong, please try again.")

def run():
    pass


# PRACTICE: run() function code for like/userlike functionality
username = input("What is your username? ")
list_of_userlikes = user_likes(1) # this function is from DB_utils
if username in list_of_userlikes:
    print("You have already liked this post.")
else:
    like_y_n = input("Would you like to like this post? Y or N: ").lower()
    if like_y_n == "y":
        response = like_entry(username, 1)
        print(f"Thank you, {username}, for liking this post:", response)