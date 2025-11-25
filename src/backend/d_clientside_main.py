import requests
from b_db_utils import user_likes
# import classes for run function

# this function will enable the user to see all public posts via the Flask interface
def get_public_feed():
    url = 'http://127.0.0.1:5000/feed'
    result = requests.get(url, headers={'content-type': 'application/json'})
    return result.json()

# TO COMPLETE will provide a json of all public and private entries that user has input
def get_username_entries(username):
    # result = requests.get(
    #     f'http://127.0.0.1:5000/{username}',headers={'content-type': 'application/json'})
    # return result.json()
    pass

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